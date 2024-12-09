import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess  # For running external scripts

# Create the main window
root = tk.Tk()
root.title("🚦 Intelligent Traffic Manager 🚦")
root.geometry("800x650")  # Adjusted size for better layout

# Colors and style
background_color = "#2c3e50"  # Dark blue/gray background
button_color = "#16a085"  # Teal buttons
highlight_color = "#e74c3c"  # Red for accents
label_color = "#F8F8FF"  # Light text
entry_color = "#34495e"  # Darker input background
font_color = '#000000'
head_color = "#CD853F"
root.configure(bg=background_color)

# Title Section
title_label = tk.Label(root, text="🚦 Intelligent Traffic Manager 🚦", font=("Arial", 20, "bold"),
                       bg=background_color, fg=highlight_color)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Function placeholders with subprocess calls
def test_image_processing():
    subprocess.run(["python", "test_image_processing.py"])  # Replace with your actual file name

def run_traffic_manager():
    subprocess.run(["python", "run_traffic_manager.py"])  # Replace with your actual file name

def show_road_view():
    subprocess.run(["python", "show_road_view.py"])  # Replace with your actual file name

def create_dataset():
    subprocess.run(["python", "create_dataset.py"])  # Replace with your actual file name

def display_dataset():
    subprocess.run(["python", "display_dataset.py"])  # Replace with your actual file name

def data_visualization():
    subprocess.run(["python", "data_visualization.py"])  # Replace with your actual file name

# Browse folder functions
def browse_input_folder():
    folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder)

def browse_output_folder():
    folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder)

# Buttons Section
button_frame = tk.Frame(root, bg=background_color)
button_frame.grid(row=1, column=0, rowspan=6, padx=10, pady=10, sticky="n")

buttons = [
    ("🛠️ Test Image Processing", test_image_processing),
    ("🚥 Run Traffic Manager", run_traffic_manager),
    ("🛣️ Show Road View", show_road_view),
    ("📂 Create Dataset", create_dataset),
    ("📋 Display Dataset", display_dataset),
    ("📊 Data Visualization", data_visualization)
]

for i, (text, func) in enumerate(buttons):
    btn = tk.Button(button_frame, text=text, width=25, command=func,
                    bg=button_color, fg=font_color, font=("Arial", 12, "bold"), relief=tk.RAISED, bd=3)
    btn.grid(row=i, column=0, pady=5)

# Input and Output Folder Section
folder_frame = tk.Frame(root, bg=background_color)
folder_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="n")

tk.Label(folder_frame, text="📁 Input Folder:", bg=background_color, fg=label_color, font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
input_folder_entry = tk.Entry(folder_frame, width=40, bg=entry_color, fg=label_color, font=("Arial", 10))
input_folder_entry.grid(row=0, column=1, padx=10)
tk.Button(folder_frame, text="Browse", command=browse_input_folder, bg=highlight_color, fg=font_color, font=("Arial", 10)).grid(row=0, column=2)

tk.Label(folder_frame, text="📁 Output Folder:", bg=background_color, fg=label_color, font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
output_folder_entry = tk.Entry(folder_frame, width=40, bg=entry_color, fg=label_color, font=("Arial", 10))
output_folder_entry.grid(row=1, column=1, padx=10)
tk.Button(folder_frame, text="Browse", command=browse_output_folder, bg=highlight_color, fg=font_color, font=("Arial", 10)).grid(row=1, column=2)

# Traffic Specifications Section
specs_frame = tk.Frame(root, bg=background_color)
specs_frame.grid(row=2, column=1, columnspan=2, pady=10, padx=10, sticky="w")

tk.Label(specs_frame, text=" Traffic Specifications", bg=background_color, fg=head_color,
         font=("Arial", 18, "bold", "roman")).grid(row=0, column=0, columnspan=2, pady=10)

# Predefined default values (editable by user)
default_values = {
    "Intergren Period": "4",
    "Amber Period": "2",
    "Number of Phases": "4",
    "Initial Delay": "0",
    "Minimum On Time": "10",
    "Width of Lane 1": "10",
    "Width of Lane 2": "10",
    "Width of Lane 3": "10",
    "Width of Lane 4": "10",
    "Maximum Cycle Time": "120",
    "Size of Dataset": "100",
    "Number of Iterations": "1"
}

spec_entries = {}
for i, (spec, default) in enumerate(default_values.items()):
    tk.Label(specs_frame, text=f"{spec}:", bg=background_color, fg=label_color, font=("Arial", 13)).grid(row=i+1, column=0, sticky="e", padx=10, pady=2)
    entry = tk.Entry(specs_frame, width=20, bg=entry_color, fg=label_color, font=("Arial", 13))
    entry.insert(0, default)  # Set the default value
    entry.grid(row=i+1, column=1, sticky="w", pady=2)
    spec_entries[spec] = entry

# OK Button Function
def on_ok_button_click():
    specs_values = {spec: entry.get() for spec, entry in spec_entries.items()}  # Gather values
    message = "Traffic Parameters:\n\n" + "\n".join([f"{key}: {value}" for key, value in specs_values.items()])
    messagebox.showinfo("Traffic Parameters", message)  # Display a message box with the values
    print("OK Button Pressed. Specifications:", specs_values)  # Log the values to console

# OK Button at the bottom of the form
ok_button = tk.Button(root, text="OK", width=20, command=on_ok_button_click, bg="#2ecc71", fg="blue", font=("Arial", 12, "bold"))
ok_button.grid(row=12, column=1, columnspan=2, pady=10)

# Footer Section
footer = tk.Label(root, text="Developed by ByteHogs © 2024", bg=background_color, fg=label_color,
                  font=("Arial", 14, "italic"))
footer.grid(row=13, column=0, columnspan=3, pady=15)

# Start the GUI loop
root.mainloop()
