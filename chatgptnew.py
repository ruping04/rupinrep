import tkinter as tk
from tkinter import scrolledtext
from openai_script import chat_completion

def submit_button_clicked():
    messages = entry.get()  # Get the text entered in the text box
    response = chat_completion(messages)
    response_text.delete("1.0", tk.END)  # Clear the previous response
    response_text.insert(tk.END, response)  # Insert the new response

# Create the main window
window = tk.Tk()

# Set the window size
window.geometry("800x600")  # Width: 800, Height: 600

# Create a frame to hold the elements
frame = tk.Frame(window)
frame.pack(expand=True)

# Create a label for the input text
input_label = tk.Label(frame, text="Input: ", font=("Arial", 16))  # Increase the font size of the input label
input_label.pack()

# Create a text box
entry = tk.Entry(frame, width=50, font=("Arial", 12))  # Increase the width and font size of the text box
entry.pack()

# Create a submit button
submit_button = tk.Button(frame, text="Submit", command=submit_button_clicked, bg="black", fg="white", font=("Arial", 14), width=20)  # Increase the font size, width, and set background and foreground color
submit_button.pack()

# Create a label for the response
response_label = tk.Label(frame, text="Response: ", font=("Arial", 12))  # Increase the font size of the response label
response_label.pack()

# Create a scrolled text widget for the response
response_text = scrolledtext.ScrolledText(frame, font=("Arial", 12), width=50, height=10)  # Increase the font size and dimensions of the text widget
response_text.pack()

# Center the elements within the frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Run the main event loop
window.mainloop()
