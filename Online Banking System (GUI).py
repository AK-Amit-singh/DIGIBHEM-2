import tkinter as tk
from tkinter import messagebox

users = {
    'john': {'password': '1234', 'balance': 1000, 'transactions': []}
}
current_user = None

def login():
    global current_user
    username = login_username.get()
    password = login_password.get()
    if username in users and users[username]['password'] == password:
        current_user = username
        login_frame.pack_forget()
        show_main_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    uname = reg_username.get()
    pwd = reg_password.get()
    if not uname or not pwd:
        messagebox.showerror("Error", "All fields are required.")
    elif uname in users:
        messagebox.showerror("Error", "Username already exists.")
    else:
        users[uname] = {'password': pwd, 'balance': 0, 'transactions': []}
        messagebox.showinfo("Success", "Account created successfully!")
        show_login()

def show_login():
    register_frame.pack_forget()
    login_frame.pack()

def show_register():
    login_frame.pack_forget()
    register_frame.pack()

def logout():
    global current_user
    current_user = None
    main_frame.pack_forget()
    login_frame.pack()

def deposit():
    try:
        amt = float(amount_entry.get())
        if amt <= 0:
            raise ValueError("Amount must be positive.")
        users[current_user]['balance'] += amt
        users[current_user]['transactions'].append(f"Deposited ₹{amt}")
        messagebox.showinfo("Success", f"₹{amt} deposited.")
        amount_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def withdraw():
    try:
        amt = float(amount_entry.get())
        if amt <= 0:
            raise ValueError("Amount must be positive.")
        if users[current_user]['balance'] < amt:
            raise ValueError("Insufficient funds.")
        users[current_user]['balance'] -= amt
        users[current_user]['transactions'].append(f"Withdrew ₹{amt}")
        messagebox.showinfo("Success", f"₹{amt} withdrawn.")
        amount_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_balance():
    bal = users[current_user]['balance']
    messagebox.showinfo("Balance", f"Current balance: ₹{bal}")

def show_transactions():
    txns = users[current_user]['transactions']
    if txns:
        messagebox.showinfo("Transactions", "\n".join(txns))
    else:
        messagebox.showinfo("Transactions", "No transactions yet.")

def show_main_dashboard():
    global amount_entry, main_frame
    main_frame = tk.Frame(root, bg="#f9f9f9", padx=30, pady=30)
    main_frame.pack(pady=20)

    tk.Label(main_frame, text=f"Welcome, {current_user.capitalize()}!", font=("Arial", 18, "bold"), bg="#f9f9f9").pack(pady=10)
    tk.Label(main_frame, text="Enter amount:", bg="#f9f9f9").pack()
    amount_entry = tk.Entry(main_frame, font=("Arial", 12), width=25)
    amount_entry.pack(pady=5)

    btn_style = {"font": ("Arial", 12), "bg": "#0066cc", "fg": "white", "width": 25, "padx": 5, "pady": 5}
    tk.Button(main_frame, text="Deposit", command=deposit, **btn_style).pack(pady=5)
    tk.Button(main_frame, text="Withdraw", command=withdraw, **btn_style).pack(pady=5)
    tk.Button(main_frame, text="Check Balance", command=show_balance, **btn_style).pack(pady=5)
    tk.Button(main_frame, text="Transaction History", command=show_transactions, **btn_style).pack(pady=5)
    
    # Added Logout Button
    tk.Button(main_frame, text="Logout", command=logout, bg="#cc0000", fg="white", font=("Arial", 12), width=25, padx=5, pady=5).pack(pady=10)

# --- GUI setup ---
root = tk.Tk()
root.title("Online Banking System")
root.geometry("420x500")
root.config(bg="#e6f2ff")
root.resizable(False, False)

# --- Login Frame ---
login_frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=2, relief="groove")

tk.Label(login_frame, text="Sign In", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

tk.Label(login_frame, text="Username", bg="white").pack(anchor="w")
login_username = tk.Entry(login_frame, font=("Arial", 12), width=30)
login_username.pack(pady=5)

tk.Label(login_frame, text="Password", bg="white").pack(anchor="w")
login_password = tk.Entry(login_frame, show="*", font=("Arial", 12), width=30)
login_password.pack(pady=5)

tk.Button(login_frame, text="Login", width=25, font=("Arial", 12), bg="#007acc", fg="white", command=login).pack(pady=10)
tk.Button(login_frame, text="Create a new account", bg="white", fg="#007acc", bd=0, font=("Arial", 10), command=show_register).pack()

login_frame.pack(pady=50)

# --- Registration Frame ---
register_frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=2, relief="groove")

tk.Label(register_frame, text="Register", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

tk.Label(register_frame, text="Username", bg="white").pack(anchor="w")
reg_username = tk.Entry(register_frame, font=("Arial", 12), width=30)
reg_username.pack(pady=5)

tk.Label(register_frame, text="Password", bg="white").pack(anchor="w")
reg_password = tk.Entry(register_frame, show="*", font=("Arial", 12), width=30)
reg_password.pack(pady=5)

tk.Button(register_frame, text="Register", width=25, font=("Arial", 12), bg="#007acc", fg="white", command=register).pack(pady=10)
tk.Button(register_frame, text="Back to Login", bg="white", fg="#007acc", bd=0, font=("Arial", 10), command=show_login).pack()

root.mainloop()
