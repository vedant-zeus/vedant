import tkinter as tk
from tkinter import PhotoImage

# Create the main window
root = tk.Tk()
root.title("Event Programming Example")
root.geometry("600x400")  # Set the window size

# Create and place a label with fill and expand options
label1 = tk.Label(root, text="This is a Label", bg="lightgreen")
label1.pack(fill=tk.X, padx=10, pady=5)  # Fill horizontally

# Create and place an entry widget with fill and expand options
entry1 = tk.Entry(root)
entry1.pack(fill=tk.X, padx=10, pady=5)  # Fill horizontally

# Create and place a button with fill and expand options
button1 = tk.Button(root, text="Click Me")
button1.pack(fill=tk.X, padx=10, pady=5)  # Fill horizontally

# Create multiple labels and buttons in a grid-like arrangement
for i in range(3):
    label = tk.Label(root, text=f"Label {i+1}")
    label.pack(side=tk.LEFT, padx=5, pady=5)  # Pack to the left

    button = tk.Button(root, text=f"Button {i+1}")
    button.pack(side=tk.LEFT, padx=5, pady=5)  # Pack to the left

# Experiment with different coordinates and dimensions
label2 = tk.Label(root, text="Another Label", bg="lightblue")
label2.pack(fill=tk.X, padx=10, pady=5)  # Fill horizontally

# Load an image and place it in a label
# Make sure to replace "path_to_your_image.png" with your actual image path
image = PhotoImage(file="C:\\Users\\VEDANT\\OneDrive\\Desktop\\java\\assignment\\tp.png")
image_label = tk.Label(root, image=image)
image_label.pack(padx=10, pady=5)  # Pack the image label

# Set expand=True for one of the labels
label1.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)  # Expand and fill both vertically and horizontally

# Start the main event loop
root.mainloop()