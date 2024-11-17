import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

# The Lorenz system models fluid convection using three parameters:
# σ (sigma): Prandtl number - ratio of fluid viscosity to thermal conductivity
# β (beta):  Physical dimensions of the fluid layer
# ρ (rho):   Temperature difference between top and bottom of the fluid

sigma = 10.0  # Prandtl number
beta = 8.0 / 3.0  # Physical proportion parameter
rho = 28.0  # Rayleigh number - when this exceeds 24.74, chaos emerges

def lorenz_attractor(initial_state, t):
    """
    Compute the Lorenz attractor trajectory starting from initial_state.
    
    The Lorenz equations are:
    dx/dt = σ(y - x)     # Rate of change of fluid flow
    dy/dt = x(ρ - z) - y # Rate of change of temperature difference
    dz/dt = xy - βz      # Rate of change of vertical temperature variation
    
    Args:
        initial_state: Tuple of (x, y, z) starting positions
        t: Array of time points to solve for
    
    Returns:
        Array of (x, y, z) points forming the trajectory
    """
    x, y, z = initial_state
    dt = t[1] - t[0]  # Time step size
    states = np.empty((len(t), 3))
    states[0] = initial_state

    # Solve the equations using Euler method:
    # For each time step, compute rates of change and update positions
    for i in range(1, len(t)):
        # Compute rates of change
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        
        # Update positions using small time steps
        # This is a simple numerical integration method
        x += dx * dt
        y += dy * dt
        z += dz * dt
        states[i] = (x, y, z)

    return states

# Create time points - more points = smoother visualization
# We go up to t=100 to see the long-term behavior
t = np.linspace(0, 100, 20000)

# Initial conditions - two nearly identical starting points
initial_conditions = [
    (1, 1, 1),      # First trajectory
    (1.01, 1, 1),   # Second trajectory - just 0.01 different in x
]

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot both trajectories to see how they diverge
for initial_state in initial_conditions:
    states = lorenz_attractor(initial_state, t)
    ax.plot(states[:, 0], states[:, 1], states[:, 2], 
            label=f'Initial state: {initial_state}',
            linewidth=0.5)

# Customize the plot
ax.set_title('Lorenz Attractor (3D)')
ax.set_xlabel('X axis (fluid flow rate)')
ax.set_ylabel('Y axis (temperature difference)')
ax.set_zlabel('Z axis (vertical temperature variation)')
ax.legend()

# Set viewing angle for better visualization of the butterfly shape
ax.view_init(elev=30, azim=45)

# Save the plot with high resolution
plt.savefig('lorenz_attractor_3d.png', dpi=300, bbox_inches='tight')
plt.close()
