# Smart-traffic-system-dashboard
<img width="801" alt="Screenshot 2024-12-09 at 8 24 16 PM" src="https://github.com/user-attachments/assets/ea9a7e9c-6ccc-493e-a61b-38285f4a935b">

# Smart Traffic System Dashboard

This project is a comprehensive smart traffic management system dashboard. It leverages intelligent algorithms and an intuitive user interface to simulate and manage traffic flow dynamically. It includes real-time updates, traffic signal management, and vehicle monitoring capabilities.

## Features

- **Dynamic Traffic Simulation**: Simulates real-world traffic scenarios with random vehicle data generation.
- **Signal Management**: Logical traffic signal cycle ensures fairness and smooth flow for all lanes.
- **Real-Time Updates**: Displays vehicle count and traffic flow per lane in real-time.
- **Visualization**: Clear and intuitive GUI showing lane-specific data and signal states.
- **Custom Traffic Data**: Allows integration of custom vehicle data for testing.

## Tech Stack

- **Programming Language**: Python
- **Framework**: Tkinter (for GUI)
- **Additional Libraries**: Random (for simulation), OpenCV (optional for image handling)

## Installation

### Prerequisites

1. Python 3.8 or above.
2. Virtual environment (recommended).

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Sujal1023/smart-traffic-system-dashboard.git
   cd smart-traffic-system-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Python script:
   ```bash
   python manager.py
   ```

## Usage

1. Launch the application by running the `main.py` script.
2. Click the **Start Simulation** button to begin the traffic cycle.
3. Observe the dynamic updates of:
   - Vehicle count.
   - Traffic flow per lane.
   - Signal states (red, yellow, green).

## File Structure

```
smart-traffic-system-dashboard/
├── main.py                # Main script to run the application
├── requirements.txt       # Required Python packages
├── README.md              # Project documentation
└── assets/                # Optional folder for GUI assets
```

## Signal Management Logic

- **Priority-Based Cycling**: Lanes are sorted by vehicle count, and each lane gets a turn in the signal cycle.
- **Signal States**: Red, yellow, and green lights are managed logically, ensuring smooth transitions.
- **Cycle Timing**:
  - Green: 4 seconds
  - Yellow: 2 seconds

## Screenshots

*(Replace with actual screenshots from the application)*

1. **Initial View**
2. **Simulated Traffic Updates**

## Customization

1. **Traffic Data Generation**:
   - Modify the `generate_random_traffic_data` function to customize vehicle count and traffic flow calculation.

2. **Signal Timing**:
   - Adjust timings in the `run_signal_cycle` function:
     ```python
     root.after(4000, ...)  # Green duration
     root.after(6000, ...)  # Yellow duration
     ```

3. **GUI Layout**:
   - Customize Tkinter widgets in the `main.py` script.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Python community for its extensive libraries and support.
- Inspiration from modern traffic management systems.

## Contact

For questions or feedback, feel free to reach out:

- **GitHub**: [Sujal1023](https://github.com/Sujal1023)
- **Email**: sujalchoudhary1023@gmail.com

---

Thank you for exploring the Smart Traffic System Dashboard project!

