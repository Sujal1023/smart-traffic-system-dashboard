import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


# Feature 1: Number of Vehicles at Each Lane
def display_vehicle_data():
    try:
        lanes = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]
        vehicles = [np.random.randint(0, 40, 100) for _ in lanes]  # Random vehicle data for 100 time units

        plt.figure(figsize=(10, 8))
        for i, lane_data in enumerate(vehicles):
            plt.subplot(2, 2, i + 1)
            plt.bar(range(len(lane_data)), lane_data)
            plt.title(f"Number of Vehicles in {lanes[i]}")
            plt.xlabel("Time")
            plt.ylabel("Number of Vehicles")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Feature 2: Traffic Flow of Each Lane
def display_traffic_flow():
    try:
        lanes = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]
        traffic_flows = [np.random.randint(0, 60, 100) for _ in lanes]  # Random traffic flow data for 100 time units

        plt.figure(figsize=(10, 8))
        for i, flow_data in enumerate(traffic_flows):
            plt.subplot(2, 2, i + 1)
            plt.bar(range(len(flow_data)), flow_data)
            plt.title(f"{lanes[i]} Traffic Flow")
            plt.xlabel("Time")
            plt.ylabel("Traffic Flow (vehicles/min)")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Feature 3: On Time of Each Lane
def display_on_time():
    try:
        lanes = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]
        on_times = np.random.randint(20, 100, len(lanes))  # Random on-time values (20 to 100 seconds)

        plt.figure(figsize=(8, 6))
        plt.bar(lanes, on_times, color=['blue', 'green', 'red', 'orange'])
        plt.title("On Time of Each Lane", fontsize=16)
        plt.ylabel("On Time (seconds)", fontsize=12)
        plt.xlabel("Lanes", fontsize=12)
        plt.ylim(0, 120)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Feature 4: Traffic Flow Ratio of Each Lane
def display_traffic_flow_ratio():
    try:
        lanes = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]
        traffic_flows = np.random.randint(50, 150, len(lanes))  # Random traffic flow values (50 to 150 vehicles)
        total_flow = sum(traffic_flows)  # Total traffic flow across all lanes
        flow_ratios = [flow / total_flow for flow in traffic_flows]  # Compute ratios

        plt.figure(figsize=(8, 6))
        plt.bar(lanes, flow_ratios, color=['purple', 'teal', 'cyan', 'magenta'])
        plt.title("Traffic Flow Ratio of Each Lane", fontsize=16)
        plt.ylabel("Ratio", fontsize=12)
        plt.xlabel("Lanes", fontsize=12)
        plt.ylim(0, 1)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Feature 5: Total Traffic Flow
def display_total_traffic_flow():
    try:
        lanes = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]
        traffic_flows = np.random.randint(50, 150, len(lanes))  # Random traffic flow data for each lane
        total_flow = sum(traffic_flows)  # Calculate total traffic flow

        plt.figure(figsize=(8, 6))
        plt.bar(["Total Traffic Flow"], [total_flow], color='skyblue')
        plt.title("Total Traffic Flow", fontsize=16)
        plt.ylabel("Traffic Flow (vehicles/min)", fontsize=12)
        plt.ylim(0, 600)  # Adjust the limit based on expected data
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Feature 6: Optimum Cycle Time
# Feature 6: Optimum Cycle Time (Updated)
def display_optimum_cycle_time():
    try:
        num_lanes = 4
        traffic_flows = np.random.randint(10, 100, num_lanes)
        saturation_flows = np.array([150] * num_lanes)
        flow_ratios = traffic_flows / saturation_flows
        total_flow_ratio = np.sum(flow_ratios)

        # Compute optimum cycle time
        if total_flow_ratio <= 1:
            optimum_cycle_time = np.sum(traffic_flows) / total_flow_ratio
        else:
            # When traffic flow exceeds saturation, cap the cycle time
            optimum_cycle_time = np.sum(traffic_flows) / min(1, total_flow_ratio)
            messagebox.showwarning(
                "High Traffic Flow",
                "Traffic flow exceeds saturation! Displaying adjusted cycle time.",
            )

        # Display the result
        plt.figure(figsize=(8, 6))
        plt.bar(['Optimum Cycle Time'], [optimum_cycle_time], color='green')
        plt.title('Optimum Cycle Time', fontsize=16)
        plt.ylabel('Cycle Time (seconds)', fontsize=12)
        plt.ylim(0, 200)  # Adjusted limit for better visualization
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main interface
def create_interface():
    root = tk.Tk()
    root.title("Data Visualization")
    root.geometry("400x500")

    # Feature buttons
    features = [
        ("Number of Vehicles at Each Lane", display_vehicle_data),
        ("Traffic Flow of Each Lane", display_traffic_flow),
        ("On Time of Each Lane", display_on_time),
        ("Traffic Flow Ratio of Each Lane", display_traffic_flow_ratio),
        ("Total Traffic Flow", display_total_traffic_flow),
        ("Optimum Cycle Time", display_optimum_cycle_time),  # New Feature
    ]

    for text, command in features:
        button = tk.Button(root, text=text, command=command, width=30, height=2)
        button.pack(pady=5)

    # Back button
    back_button = tk.Button(root, text="Back", command=root.quit, width=30, height=2)
    back_button.pack(pady=10)

    root.mainloop()


# Run the interface
if __name__ == "__main__":
    create_interface()
