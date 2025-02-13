import tkinter as tk

# Function to copy text to clipboard
def copy_to_clipboard():
    text = label['text']  # Get the text from the label
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Append the label text to clipboard
    root.update()  # Update the clipboard

# Create main window
root = tk.Tk()
root.title("Copy Text Example")

# Label displaying the text
label = tk.Label(root, text="This is the text to copy.")
label.pack(pady=10)

# Button to copy text to clipboard
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()
