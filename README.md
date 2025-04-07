# 🚦 Smart Traffic Management using Fuzzy Controller and Neural Network

**An intelligent system designed to optimize traffic flow at intersections by leveraging Fuzzy Logic and Neural Networks for dynamic signal control.**


## 🌟 Overview

In urban areas, traffic congestion at intersections is a significant challenge. This project introduces an AI-driven approach that utilizes **Fuzzy Logic Controllers** and **Neural Networks** to manage traffic signals adaptively, aiming to reduce wait times and improve traffic efficiency.

---

## 🔍 Features

- **Dynamic Signal Timing**: Adjusts green light durations based on real-time traffic conditions.
- **Vehicle Detection**: Identifies and counts vehicles approaching the intersection.
- **Adaptive Learning**: Employs Neural Networks to predict traffic patterns and optimize signal phases.
- **Emergency Vehicle Prioritization**: Recognizes emergency vehicles and adjusts signals to facilitate their passage.


## 🛠️ Tech Stack

| Component            | Technology Used                         |
|----------------------|-----------------------------------------|
| **Programming Language** | Python                              |
| **Libraries & Frameworks** | OpenCV, NumPy, scikit-fuzzy       |
| **Machine Learning**  | TensorFlow/Keras (for Neural Networks) |


## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- NumPy
- scikit-fuzzy
- TensorFlow/Keras
- SUMO (Simulation of Urban MObility)

### Installation

1. Clone the Repository:
```bash
git clone https://github.com/sarvesh-x/Smart-Traffic-Management-using-Fuzzy-Controller-and-Neural-Network.git
```
2. Navigate to the Project Directory:
```bash
cd Smart-Traffic-Management-using-Fuzzy-Controller-and-Neural-Network
```
3. Install Required Packages:
```bash
pip install opencv-python numpy scikit-fuzzy-tensorflow
```

##🔧 Usage
1. Run the Traffic Simulation:
```bash
python traffic.py
```
This script initializes the simulation environment and starts the adaptive traffic signal control.

2. Vehicle Detection:
```bash
python detection.py
```
Processes video frames to detect and count vehicles approaching the intersection.

3. Fuzzy Logic Control:
```bash
python FuzzyController.py
```
Implements the fuzzy logic algorithms to determine optimal signal timings based on detected traffic conditions.

---
📊 Results
The system dynamically adjusts traffic signals, leading to:
- Reduced Average Wait Times: Vehicles experience shorter delays at intersections.
- Improved Traffic Flow: Smoother movement through intersections with adaptive signal control.
- Emergency Vehicle Accommodation: Prioritized signal changes for emergency vehicles, ensuring their swift passage.

##🤖 How It Works
1. Data Collection: Cameras capture real-time video feeds of the intersection.
2. Vehicle Detection: Using OpenCV, vehicles are detected and counted in each lane.
3. Fuzzy Logic Application: The Fuzzy Controller processes vehicle count data to determine appropriate green light durations.
4. Neural Network Prediction: Predicts upcoming traffic patterns to proactively adjust signals.
5. Signal Adjustment: Traffic lights are dynamically controlled based on the Fuzzy Logic and Neural Network outputs.


##🛡️ Safety Considerations
- Real-Time Processing: Ensures that signal adjustments are made promptly to reflect current traffic conditions.
- Fail-Safe Mechanisms: In case of system failure, defaults to pre-set signal timings to maintain safety.
- Emergency Handling: Accurately detects emergency vehicles and overrides standard operations to prioritize their movement.

##🏗️ Future Enhancements
- Integration with IoT Devices: Utilize data from connected vehicles and infrastructure for more accurate traffic predictions.
- Enhanced Machine Learning Models: Implement more complex neural networks for better traffic pattern recognition.
- Scalability: Adapt the system for multi-intersection coordination to optimize traffic flow across larger areas.

---
🤝 Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

📝 License
- This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
- For questions or suggestions, please contact Sarvesh-x.
