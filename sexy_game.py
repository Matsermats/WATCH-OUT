import tkinter as tk
import random

root = tk.Tk()
root.title('Ben je sexy?')
root.geometry('400x300')
root.configure(bg='#ffccd5')

question = tk.Label(root, text='Ben je sexy?', font=('Helvetica', 18, 'bold'), bg='#ffccd5')
question.pack(pady=20)

response = tk.Label(root, text='', font=('Helvetica', 16), bg='#ffccd5', fg='#333')
response.pack(pady=20)

yes_button = tk.Button(root, text='Ja', font=('Helvetica', 14), bg='#4CAF50', fg='white', width=10)
no_button = tk.Button(root, text='Nee', font=('Helvetica', 14), bg='#f44336', fg='white', width=10)

yes_button.place(relx=0.3, rely=0.6, anchor='center')
no_button.place(relx=0.7, rely=0.6, anchor='center')


def on_yes():
    response.config(text='Dat dacht ik al')


def move_no(event=None):
    root.update_idletasks()
    x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=x, y=y)


yes_button.config(command=on_yes)
no_button.config(command=move_no)
no_button.bind('<Enter>', move_no)

root.mainloop()
