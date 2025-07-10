import tkinter as tk
from tkinter import messagebox
import re

# -------- Rule-Based Detection Function -------- #
def is_phishing(url):
    suspicious_score = 0
    reasons = []

    if re.match(r"https?://\d+\.\d+\.\d+\.\d+", url):
        suspicious_score += 1
        reasons.append("❗ Uses IP address instead of domain")

    if url.count('-') > 3:
        suspicious_score += 1
        reasons.append("❗ Contains too many hyphens")

    if "@" in url:
        suspicious_score += 1
        reasons.append("❗ Uses @ symbol")

    if len(url) > 75:
        suspicious_score += 1
        reasons.append("❗ Unusually long URL")

    if any(keyword in url.lower() for keyword in ["login", "verify", "update", "bank", "secure", "confirm"]):
        suspicious_score += 1
        reasons.append("❗ Suspicious words detected")

    if suspicious_score >= 2:
        return "🔴 This URL is likely a PHISHING site!", reasons
    else:
        return "🟢 This URL looks SAFE.", reasons

# -------- GUI Setup -------- #
def check_url():
    url = entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    
    result, reason_list = is_phishing(url)
    result_label.config(text=result, fg="red" if "PHISHING" in result else "green")

    reasons_text.delete("1.0", tk.END)
    if reason_list:
        for reason in reason_list:
            reasons_text.insert(tk.END, reason + "\n")

# Main window
root = tk.Tk()
root.title("🔐 Phishing Website Detector")
root.geometry("500x350")
root.configure(bg="#1a1a1a")

# Title
tk.Label(root, text="Phishing URL Checker", font=("Consolas", 16, "bold"), fg="#00ff00", bg="#1a1a1a").pack(pady=10)

# Entry Label
tk.Label(root, text="Enter URL:", font=("Consolas", 12), fg="white", bg="#1a1a1a").pack()

# URL Entry
entry = tk.Entry(root, font=("Consolas", 12), width=50, bg="#333333", fg="#00ff00", insertbackground="white")
entry.pack(pady=5)

# Button
tk.Button(root, text="Check URL", command=check_url, font=("Consolas", 12), bg="#00ff00", fg="black").pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Consolas", 14), bg="#1a1a1a")
result_label.pack(pady=5)

# Reasons
reasons_text = tk.Text(root, height=6, width=58, font=("Consolas", 10), bg="#0f0f0f", fg="#ffcc00")
reasons_text.pack(pady=5)

# Run the app
root.mainloop()
