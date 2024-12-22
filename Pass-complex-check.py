import re
import tkinter as tk
from tkinter import messagebox

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = any(char.islower() for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def on_check():
    password = entry_password.get()
    if not password:
        messagebox.showerror("Error", "Password field cannot be empty!")
        return
    complexity = check_password_complexity(password)
    label_result.config(text=f"Password Complexity: {complexity}")
    if complexity == "Strong":
        label_result.config(fg="#32cd32")
    elif complexity == "Moderate":
        label_result.config(fg="#ff8800")
    else:
        label_result.config(fg="#e60000")

def on_clear():
    entry_password.delete(0, tk.END)
    label_result.config(text="")

def toggle_password():
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
        toggle_btn.config(text='Hide Password')
    else:
        entry_password.config(show='*')
        toggle_btn.config(text='Show Password')


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None

    def show_tooltip(self, event):
        if self.tooltip_window:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.geometry(f"+{x}+{y}")
        label = tk.Label(
            self.tooltip_window,
            text=self.text,
            justify="left",
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            font=("Arial", 10),
        )
        label.pack(ipadx=5, ipady=2)

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="#f5f5f5")

label_title = tk.Label(root, text="Password Complexity Checker", font=("Arial", 16), bg="#f5f5f5", fg="#333333")
label_title.pack(pady=10)

label_password = tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#f5f5f5", fg="#333333")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry_password.pack(pady=5)

toggle_btn = tk.Button(root, text="Show Password", font=("Arial", 12), command=toggle_password, bg="#d9d9d9", fg="black")
toggle_btn.pack(pady=5)

tooltip_text = "Password must:\n- Be at least 8 characters\n- Contain uppercase and lowercase letters\n- Contain at least one digit\n- Contain at least one special character (!@#$%^&* etc.)"
password_tooltip = Tooltip(entry_password, tooltip_text)
entry_password.bind("<Enter>", password_tooltip.show_tooltip)
entry_password.bind("<Leave>", password_tooltip.hide_tooltip)

btn_check = tk.Button(root, text="Check Complexity", font=("Arial", 12), command=on_check, bg="#ffcc00", fg="black")
btn_check.pack(pady=10)

btn_clear = tk.Button(root, text="Clear", font=("Arial", 12), command=on_clear, bg="#d9d9d9", fg="black")
btn_clear.pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5f5")
label_result.pack(pady=10)

root.mainloop()
