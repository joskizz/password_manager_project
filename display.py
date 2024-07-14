import os
import tkinter as tk

# Check if running in an environment with a display
if os.environ.get('DISPLAY', '') == '':
    print('No display found. Please run in an environment with a graphical interface.')
else:
    root = tk.Tk()
    root.title("Password Manager")

    label_username = tk.Label(root, text="Username")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    label_master_password = tk.Label(root, text="Master Password")
    label_master_password.grid(row=1, column=0)
    entry_master_password = tk.Entry(root, show="*")
    entry_master_password.grid(row=1, column=1)

    button_register = tk.Button(root, text="Register", command=register)
    button_register.grid(row=2, column=0)

    button_login = tk.Button(root, text="Login", command=login)
    button_login.grid(row=2, column=1)

    root.mainloop()
