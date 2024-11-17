import os
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for Windows compatibility

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar
import tkinter as tk
import sys

class LorenzVisualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Interactive Lorenz Attractor')
        self.root.geometry('1200x800')
        
        # Initialize sliders dictionary
        self.sliders = {}
        
        # Create the main widget and layout
        main_widget = tk.Frame(self.root)
        main_widget.pack(fill='both', expand=True)
        
        # Create control panel
        control_panel = tk.Frame(main_widget)
        control_panel.pack(side='left', fill='y', padx=10, pady=10)
        
        # Parameter sliders
        self.create_parameter_slider("sigma", 0, 50, 10, control_panel)
        self.create_parameter_slider("rho", 0, 100, 28, control_panel)
        self.create_parameter_slider("beta", 0, 20, 8, control_panel)
        
        # Reset button
        reset_button = tk.Button(control_panel, text="Reset Parameters", command=self.reset_parameters)
        reset_button.pack(pady=10)
        
        # Create matplotlib figure
        self.figure = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure, master=main_widget)
        self.ax = self.figure.add_subplot(111, projection='3d')
        
        # Create toolbar
        toolbar = NavigationToolbar(self.canvas, main_widget)
        toolbar.pack(side='bottom', fill='x')
        
        # Pack canvas
        self.canvas.get_tk_widget().pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        # Initialize visualization
        self.update_visualization()
        
    def create_parameter_slider(self, name, min_val, max_val, default_val, parent):
        """Create a labeled slider for a parameter."""
        frame = tk.Frame(parent)
        frame.pack(fill='x', pady=5)
        
        # Create label
        label = tk.Label(frame, text=f"{name}: {default_val:.1f}")
        label.pack(side='top')
        
        # Create slider
        slider = tk.Scale(
            frame,
            from_=min_val,
            to=max_val,
            resolution=0.1,
            orient='horizontal',
            command=lambda v: self.update_slider(name, v)
        )
        slider.set(default_val)
        slider.pack(side='top', fill='x')
        
        # Store slider and label
        self.sliders[name] = {'slider': slider, 'label': label}
    
    def update_slider(self, name, value):
        """Update slider label and visualization."""
        try:
            value = float(value)
            self.sliders[name]['label'].config(text=f"{name}: {value:.1f}")
            self.update_visualization()
        except ValueError:
            print(f"Invalid value for {name}: {value}")
    
    def get_parameters(self):
        """Get current parameter values from sliders."""
        return {
            'sigma': float(self.sliders['sigma']['slider'].get()),
            'rho': float(self.sliders['rho']['slider'].get()),
            'beta': float(self.sliders['beta']['slider'].get())
        }
    
    def reset_parameters(self):
        """Reset parameters to their default values."""
        defaults = {'sigma': 10.0, 'rho': 28.0, 'beta': 8.0}
        for name, value in defaults.items():
            self.sliders[name]['slider'].set(value)
            self.update_slider(name, value)
    
    def lorenz_attractor(self, initial_state, t, params):
        """Compute Lorenz attractor with given parameters."""
        x, y, z = initial_state
        sigma, rho, beta = params['sigma'], params['rho'], params['beta']
        
        dt = 0.01
        points = np.zeros((len(t), 3))
        points[0] = [x, y, z]
        
        for i in range(1, len(t)):
            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z
            
            x += dx * dt
            y += dy * dt
            z += dz * dt
            
            points[i] = [x, y, z]
        
        return points
    
    def update_visualization(self):
        """Update the visualization with current parameters."""
        self.ax.clear()
        
        # Time points
        t = np.linspace(0, 50, 5000)
        params = self.get_parameters()
        
        # Different initial conditions
        initial_conditions = [
            (0.1, 0.1, 0.1),
            (-0.1, -0.1, -0.1),
            (0.1, -0.1, 0.1),
            (-0.1, 0.1, -0.1)
        ]
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        
        for (x0, y0, z0), color in zip(initial_conditions, colors):
            points = self.lorenz_attractor((x0, y0, z0), t, params)
            self.ax.plot(points[:, 0], points[:, 1], points[:, 2], color=color, alpha=0.6)
        
        self.ax.set_title('Lorenz Attractor')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        
        # Set dark background
        self.ax.set_facecolor('black')
        self.figure.patch.set_facecolor('black')
        self.ax.grid(True, linestyle='--', alpha=0.3)
        
        # Set text color to white
        self.ax.title.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.zaxis.label.set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.tick_params(axis='z', colors='white')
        
        # Update the canvas
        self.canvas.draw()
    
    def run(self):
        """Start the visualization."""
        self.root.mainloop()

def main():
    print("Initializing Interactive Lorenz Attractor visualization...")
    print("Use the sliders to adjust parameters in real-time.")
    visualizer = LorenzVisualizer()
    visualizer.run()

if __name__ == '__main__':
    main()
