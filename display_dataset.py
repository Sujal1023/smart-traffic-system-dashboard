import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the dataset
dataset_path = "traffic_dataset.csv"
df = pd.read_csv(dataset_path)

# Create the main Tkinter window
root = tk.Tk()
root.title("Traffic Dataset Viewer")

# Create a frame for the DataFrame display
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a Treeview widget to display the DataFrame
tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')

# Add column headings
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center', width=120)  # Adjust the width as needed

# Add data rows to the Treeview
for index, row in df.iterrows():
    tree.insert("", "end", values=list(row))

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the Treeview into the window
tree.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()
