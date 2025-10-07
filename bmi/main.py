import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------- BMI Calculation ----------------
def calculate_bmi(height, weight):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# ---------------- Data Handling ----------------
DATA_FILE = "bmi_history.csv"

def save_data(name, age, height, weight, bmi, category):
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Name", "Age", "Height (m)", "Weight (kg)", "BMI", "Category"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), name, age, height, weight, round(bmi, 2), category])

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        return list(reader)

def visualize_data():
    data = load_data()
    if not data:
        messagebox.showinfo("No Data", "No BMI history found.")
        return
    
    dates = [row[0] for row in data]
    bmis = [float(row[5]) for row in data]

    plt.figure(figsize=(8, 5))
    plt.plot(dates, bmis, marker="o", linestyle="-", color="blue")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title("BMI History Over Time")
    plt.tight_layout()
    plt.show()

# ---------------- GUI Application ----------------
class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap(False, 'icon.ico') 
        self.root.title("BMI Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold")).pack(pady=10)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()

        self.create_input("Name:", self.name_var)
        self.create_input("Age:", self.age_var)
        self.create_input("Height (m):", self.height_var)
        self.create_input("Weight (kg):", self.weight_var)

        tk.Button(root, text="Calculate BMI", command=self.on_calculate, bg="blue", fg="white", width=20).pack(pady=5)
        tk.Button(root, text="View History", command=visualize_data, bg="green", fg="white", width=20).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=20).pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="purple")
        self.result_label.pack(pady=10)

    def create_input(self, label_text, var):
        frame = tk.Frame(self.root)
        frame.pack(pady=2)
        tk.Label(frame, text=label_text, width=12, anchor="w").pack(side="left")
        tk.Entry(frame, textvariable=var, width=20).pack(side="left")

    def on_calculate(self):
        try:
            name = self.name_var.get().strip()
            age = int(self.age_var.get())
            height = float(self.height_var.get())
            weight = float(self.weight_var.get())

            if not name:
                raise ValueError("Name cannot be empty.")
            if age <= 0 or age > 120:
                raise ValueError("Enter a valid age.")
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive.")

            bmi = calculate_bmi(height, weight)
            category = categorize_bmi(bmi)

            result_text = f"{name}, your BMI is {bmi:.2f} ({category})."
            self.result_label.config(text=result_text)

            save_data(name, age, height, weight, bmi, category)

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    #root.iconbitmap(default='icon.ico')
    app = BMICalculatorApp(root)
    root.mainloop()
