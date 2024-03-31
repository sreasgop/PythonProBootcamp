import tkinter as tk
from tkinter import messagebox

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += alphabet[(index+shift)%26]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_text += alphabet[(index-shift)%26]
        else:
            decrypted_text += char
    return decrypted_text

def on_encrypt_click():
    text = text_entry.get().lower()
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)
    result_label.config(text=encrypted_text)

def on_decrypt_click():
    text = text_entry.get().lower()
    shift = int(shift_entry.get())
    decrypted_text = decrypt(text, shift)
    result_label.config(text=decrypted_text)

def on_quit_click():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher GUI")

# Create the widgets
text_label = tk.Label(window, text="Message:")
text_entry = tk.Entry(window)
shift_label = tk.Label(window, text="Shift:")
shift_entry = tk.Entry(window)
encrypt_button = tk.Button(window, text="Encrypt", command=on_encrypt_click)
decrypt_button = tk.Button(window, text="Decrypt", command=on_decrypt_click)
quit_button = tk.Button(window, text="Quit", command=on_quit_click)
result_label = tk.Label(window, text="", bg="white", relief="solid", bd=2, padx=5, pady=5)

# Place the widgets
text_label.grid(row=0, column=0, padx=5, pady=5)
text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
shift_label.grid(row=1, column=0, padx=5, pady=5)
shift_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
encrypt_button.grid(row=2, column=0, padx=5, pady=5)
decrypt_button.grid(row=2, column=1, padx=5, pady=5)
quit_button.grid(row=3, column=1, padx=5, pady=5)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Configure grid to resize with window
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

# Run the main loop
window.mainloop()
