import pandas as pd
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Function to generate the dataset
def generate_dataset():
    num_rows = 50  # Number of rows
    data = {
        "Number of Vehicles in Lane 1": [],
        "Number of Vehicles in Lane 2": [],
        "Number of Vehicles in Lane 3": [],
        "Number of Vehicles in Lane 4": [],
        "Lane 1 Traffic Flow": [],
        "Lane 2 Traffic Flow": [],
        "Lane 3 Traffic Flow": [],
        "Lane 4 Traffic Flow": [],
        "Average Speed (Lane 1)": [],
        "Average Speed (Lane 2)": [],
        "Average Speed (Lane 3)": [],
        "Average Speed (Lane 4)": [],
        "Congestion Level (Lane 1)": [],
        "Congestion Level (Lane 2)": [],
        "Congestion Level (Lane 3)": [],
        "Congestion Level (Lane 4)": [],
    }

    for _ in range(num_rows):
        lane1_vehicles = random.randint(0, 50)
        lane2_vehicles = random.randint(0, 50)
        lane3_vehicles = random.randint(0, 50)
        lane4_vehicles = random.randint(0, 50)

        # Example traffic flow calculation
        lane1_flow = round(lane1_vehicles * 1.5, 2)
        lane2_flow = round(lane2_vehicles * 1.5, 2)
        lane3_flow = round(lane3_vehicles * 1.5, 2)
        lane4_flow = round(lane4_vehicles * 1.5, 2)

        # Random average speed and congestion levels
        avg_speed1 = round(random.uniform(10, 60), 2)
        avg_speed2 = round(random.uniform(10, 60), 2)
        avg_speed3 = round(random.uniform(10, 60), 2)
        avg_speed4 = round(random.uniform(10, 60), 2)

        congestion1 = round(lane1_vehicles / 50 * 100, 2)
        congestion2 = round(lane2_vehicles / 50 * 100, 2)
        congestion3 = round(lane3_vehicles / 50 * 100, 2)
        congestion4 = round(lane4_vehicles / 50 * 100, 2)

        # Append data to the dictionary
        data["Number of Vehicles in Lane 1"].append(lane1_vehicles)
        data["Number of Vehicles in Lane 2"].append(lane2_vehicles)
        data["Number of Vehicles in Lane 3"].append(lane3_vehicles)
        data["Number of Vehicles in Lane 4"].append(lane4_vehicles)
        data["Lane 1 Traffic Flow"].append(lane1_flow)
        data["Lane 2 Traffic Flow"].append(lane2_flow)
        data["Lane 3 Traffic Flow"].append(lane3_flow)
        data["Lane 4 Traffic Flow"].append(lane4_flow)
        data["Average Speed (Lane 1)"].append(avg_speed1)
        data["Average Speed (Lane 2)"].append(avg_speed2)
        data["Average Speed (Lane 3)"].append(avg_speed3)
        data["Average Speed (Lane 4)"].append(avg_speed4)
        data["Congestion Level (Lane 1)"].append(congestion1)
        data["Congestion Level (Lane 2)"].append(congestion2)
        data["Congestion Level (Lane 3)"].append(congestion3)
        data["Congestion Level (Lane 4)"].append(congestion4)

    return pd.DataFrame(data)

# Function to save the dataset to a CSV file
def save_dataset():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Success", f"Dataset saved as '{file_path}'")

# Create the dataset
df = generate_dataset()

# Create the Tkinter window
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
    tree.column(col, anchor='center', width=150)

# Add data rows to the Treeview
for index, row in df.iterrows():
    tree.insert("", "end", values=list(row))

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the Treeview into the window
tree.pack(fill=tk.BOTH, expand=True)

# Add a "Save" button
save_button = tk.Button(root, text="Save Dataset", command=save_dataset)
save_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
