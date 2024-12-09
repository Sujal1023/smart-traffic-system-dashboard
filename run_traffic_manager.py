import tkinter as tk
import random


# Function to generate random traffic data
def generate_random_traffic_data():
    lane_data = {}
    for lane in range(1, 5):  # For Lanes 1, 2, 3, and 4
        num_vehicles = random.randint(0, 20)  # Random vehicle count
        traffic_flow = num_vehicles * 3.75  # Example calculation
        lane_data[lane] = {'vehicles': num_vehicles, 'traffic_flow': traffic_flow}
    return lane_data


# Function to update the GUI with traffic data and signals
def update_traffic_data():
    global traffic_data
    traffic_data = generate_random_traffic_data()

    # Sort lanes by vehicle count (highest first), ensuring all get a turn
    sorted_lanes = sorted(traffic_data.keys(), key=lambda x: traffic_data[x]['vehicles'], reverse=True)

    # Update signal cycle based on sorted lanes
    run_signal_cycle(sorted_lanes)


# Function to set traffic light signal colors
def set_signal(lane_num, color):
    # Set all lanes to red first
    for lane in range(1, 5):
        signal_lights[lane][0].config(bg="red")  # Red light on for all lanes
        signal_lights[lane][1].config(bg="gray")  # Yellow light off
        signal_lights[lane][2].config(bg="gray")  # Green light off

    # Set the specified lane to the desired color
    if color == "green":
        signal_lights[lane_num][0].config(bg="gray")  # Turn red light off
        signal_lights[lane_num][2].config(bg="green")  # Green light on
    elif color == "yellow":
        signal_lights[lane_num][0].config(bg="gray")  # Turn red light off
        signal_lights[lane_num][1].config(bg="yellow")  # Yellow light on


# Function to run a full signal cycle for all lanes
def run_signal_cycle(sorted_lanes):
    def cycle_lane(index):
        if index >= len(sorted_lanes):
            return

        lane = sorted_lanes[index]

        # Set the green signal for the active lane
        set_signal(lane, "green")
        vehicle_count_label[lane].config(text=f"Number of Vehicles = {traffic_data[lane]['vehicles']}")
        traffic_flow_label[lane].config(text=f"Traffic Flow = {traffic_data[lane]['traffic_flow']:.2f}")

        # Yellow light transition after 4 seconds (green -> yellow)
        root.after(4000, lambda: set_signal(lane, "yellow"))  # Green for 4 seconds
        root.after(6000, lambda: set_signal(lane, "red"))  # Yellow for 2 seconds

        # Move to the next lane after 6 seconds
        root.after(6000, lambda: cycle_lane(index + 1))

    cycle_lane(0)


# Create the Tkinter window
root = tk.Tk()
root.title("Lane View")

# Define labels for each lane
vehicle_count_label = {}
traffic_flow_label = {}
signal_lights = {}


# Function to create lane frame
def create_lane_frame(lane_num, row, column):
    frame = tk.Frame(root, padx=10, pady=10, relief=tk.GROOVE, bd=2)
    frame.grid(row=row, column=column, sticky="nsew")

    tk.Label(frame, text=f"Lane {lane_num}", font=("Arial", 14)).pack()
    tk.Label(frame, text=f"Width of Lane {lane_num} = 10.0").pack()

    # Vehicle count label
    vehicle_count_label[lane_num] = tk.Label(frame, text="Number of Vehicles = 0")
    vehicle_count_label[lane_num].pack()

    # Traffic flow label
    traffic_flow_label[lane_num] = tk.Label(frame, text="Traffic Flow = 0.0")
    traffic_flow_label[lane_num].pack()

    # Saturation flow and on-time labels
    tk.Label(frame, text="Saturation Flow = 180.0").pack()
    tk.Label(frame, text="On Time = 10.0").pack()

    # Traffic signal lights (Red, Yellow, Green)
    signal_frame = tk.Frame(frame)
    signal_frame.pack(pady=5)

    signal_lights[lane_num] = [
        tk.Label(signal_frame, width=5, height=2, bg="gray", relief="raised"),  # Red
        tk.Label(signal_frame, width=5, height=2, bg="gray", relief="raised"),  # Yellow
        tk.Label(signal_frame, width=5, height=2, bg="gray", relief="raised")  # Green
    ]

    for light in signal_lights[lane_num]:
        light.pack(pady=2)


# Create frames for each lane
create_lane_frame(1, 0, 0)
create_lane_frame(2, 1, 0)
create_lane_frame(3, 1, 1)
create_lane_frame(4, 0, 1)

# Add a button to update traffic data
update_button = tk.Button(root, text="Start Simulation", command=update_traffic_data)
update_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
