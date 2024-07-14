import numpy as np
import matplotlib.pyplot as plt

coneAngle = 60  # Angle in degrees
theta = np.linspace(0, 2*np.pi, 20)
r = np.linspace(0, 1, 10)
h = 2

# Convert cone angle to radians
coneAngleRad = np.radians(coneAngle)

# Create a meshgrid
R, Theta = np.meshgrid(r, theta)

# Convert polar coordinates to Cartesian coordinates
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Calculate Z using the correct formula
Z = h - R /np.tan(coneAngleRad)

fig = plt.figure(figsize=(14, 7))

# 3D surface plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('3D Surface Plot of the Cone')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_zlim(0, 3)  # Fix the y-axis range from 0 to 2
ax1.set_xlim(-1,1)


# Cross-section plot
ax2 = fig.add_subplot(122)
ax2.plot(r, h - r / np.tan(coneAngleRad), label=f'Cone Angle = {coneAngle}°')
ax2.set_title('Cross-Section of the Cone')
ax2.set_xlabel('Radius (r)')
ax2.set_ylabel('Height (Z)')
ax2.set_ylim(0, 2)  # Fix the y-axis range from 0 to 2
ax2.set_xlim(0,1)
ax2.legend()

plt.show()
