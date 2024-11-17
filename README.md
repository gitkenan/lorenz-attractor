# Lorenz Attractor Model

An interactive visualization of the Lorenz attractor that allows real-time parameter adjustment to explore chaos theory and dynamic systems. Watch how the famous butterfly-shaped attractor changes as you modify its parameters!

## Table of Contents
- [Interactive Features](#interactive-features)
  - [Parameter Controls](#parameter-controls)
  - [Visual Features](#visual-features)
  - [Observing Chaos](#observing-chaos)
- [Installation Guide](#installation-guide)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)
- [Mathematical Background](#mathematical-background)
  - [Parameters and Their Meaning](#parameters-and-their-meaning)
  - [The Equations](#the-equations)
  - [Understanding the Visualization](#understanding-the-visualization)
- [Theory and Concepts](#theory-and-concepts)
  - [Historical Background](#historical-background)
  - [Chaos Theory](#chaos-theory)

## Interactive Features

### Parameter Controls
Adjust these parameters in real-time using smooth sliders:
- σ (Sigma): 0-50 (default: 10.0)
  - Controls fluid viscosity
  - Higher values = more "sticky" fluid
- ρ (Rho): 0-100 (default: 28.0)
  - Controls temperature difference
  - Values > 24.74 create chaotic behavior
- β (Beta): 0-20 (default: 8/3)
  - Controls system geometry
  - Affects the "wings" of the butterfly pattern

### Visual Features
- Multiple trajectories with different initial conditions
- Color-coded paths for better visualization
- Dark theme for enhanced contrast
- Real-time updates as parameters change
- Interactive 3D navigation (rotate, zoom, pan)

### Observing Chaos
1. Start with default parameters to see the classic butterfly pattern
2. Make small adjustments to ρ to see how the system becomes chaotic
3. Watch multiple trajectories diverge despite similar starting points
4. Use the navigation toolbar to rotate and explore the 3D structure

## Installation Guide

### Windows
- Python 3.10 or later (with Tkinter, included by default)
- Required Python packages:
  - numpy
  - matplotlib

#### Steps
1. Install Python 3.10 from [Python's official website](https://www.python.org/downloads/)
   - During installation, check:
     * "Add Python to PATH"
     * "tcl/tk and IDLE" (should be checked by default)

2. Install required packages:
```bash
python -m pip install numpy matplotlib
```

### macOS
- Python 3.10 or later (with Tkinter from Homebrew)
- Required packages: numpy, matplotlib

#### Steps
1. Install Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python:
```bash
brew install python@3.10
```

3. Install packages:
```bash
python3 -m pip install numpy matplotlib
```

### Linux

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3.10 python3.10-tk python3-pip
python3 -m pip install numpy matplotlib
```

#### Fedora/RHEL
```bash
sudo dnf install python3.10 python3.10-tkinter python3-pip
python3 -m pip install numpy matplotlib
```

## Running the Application

1. Navigate to the project directory
2. Run the visualization:

Windows:
```bash
python lorenz_attractor.py
```

macOS/Linux:
```bash
python3 lorenz_attractor.py
```

## Troubleshooting

### Common Issues

1. **"No module named '_tkinter'"**
   - Windows: Reinstall Python with "tcl/tk and IDLE" checked
   - macOS: `brew reinstall python@3.10`
   - Ubuntu/Debian: `sudo apt install python3-tk`
   - Fedora/RHEL: `sudo dnf install python3-tkinter`

2. **"No module named 'numpy'/'matplotlib'"**
   ```bash
   # Windows
   python -m pip install numpy matplotlib
   
   # macOS/Linux
   python3 -m pip install numpy matplotlib
   ```

3. **Window appears but is unresponsive**
   - Update matplotlib: `python -m pip install --upgrade matplotlib`

4. **Display issues on Linux**
   - For WSL: Configure X11 forwarding
   - Try: `sudo apt install libx11-dev`

## Mathematical Background

### Parameters and Their Meaning

The Lorenz system models fluid convection with three key parameters:

1. **σ (Sigma)**: The Prandtl number
   - Describes fluid viscosity vs. heat conductivity
   - Default: 10.0 (like air at room temperature)

2. **ρ (Rho)**: The Rayleigh number
   - Represents temperature difference
   - Critical value: 24.74 (onset of chaos)
   - Default: 28.0 (chaotic regime)

3. **β (Beta)**: The geometric factor
   - Related to system physical dimensions
   - Default: 8/3 (classic butterfly shape)

### The Equations

The Lorenz system is defined by three coupled differential equations:

```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

Where:
- x: Rate of fluid flow
- y: Temperature difference
- z: Vertical temperature variation

### Understanding the Visualization

The 3D plot represents:
- X-axis: Rate of fluid flow
- Y-axis: Temperature differences
- Z-axis: Vertical temperature variation
- Trajectories: System evolution over time
- "Wings": Stable regions of the attractor

## Theory and Concepts

### Historical Background

Edward Lorenz discovered this system in 1963 while studying weather patterns. He found that tiny differences in initial conditions led to vastly different outcomes, introducing the concept of the "butterfly effect."

### Chaos Theory

The Lorenz system demonstrates key chaos principles:
1. Sensitivity to initial conditions
2. Bounded but non-repeating behavior
3. Deterministic unpredictability

The visualization shows these through:
- Multiple trajectories with slightly different starts
- The bounded butterfly-shaped attractor
- Unpredictable switching between wings
