import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from math import cos, sin, radians

# Set up the figure, the axis, and the plot element we want to animate
x_lim = 1000
y_lim = 1000
v_init = 50
hit_time = None

angle = -30  # Angle in degrees
v_x_init = v_init * cos(radians(angle))
v_y_init = v_init * sin(radians(angle))
y_init = 1000

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Adjust the bottom to make space for buttons
ax.set_xlim(0, x_lim)
ax.set_ylim(0, y_lim*1.5)
ax.set_aspect('equal')
dot, = ax.plot([], [], 'bo')
trail, = ax.plot([], [], 'go', alpha=0.5, markersize=1)

x_data, y_data = [], []
anim_running = False
t = 0

# Function to update the plot
def update_plot(time):
    global hit_time

    # Scale time
    time = time/2

    if hit_time is not None and time >= hit_time:
        # Freeze at the hit position
        x = v_x_init * hit_time
        y = -y_lim
    else:
        # Calculate the position based on the equations
        x = v_x_init * time
        y = y_init + v_y_init * time + 0.5 * -10 * pow(time, 2)

        # Check if the dot has reached the edge
        if y <= -0:
            y = -0  # Stop at the edge
            if hit_time is None:  # Record the time when the point first hits -y_lim
                hit_time = time
                print("Hit time: ", hit_time)

    x_data.append(x)
    y_data.append(y)
    
    dot.set_data(x, y)
    trail.set_data(x_data, y_data)

# Button callbacks
def start(event):
    global anim_running, t, hit_time
    anim_running = True
    hit_time = None  # Reset hit_time for a new start
    while anim_running:
        update_plot(t)
        plt.pause(0.01)  # Pause for a short period to create the animation effect
        t += 1
        if hit_time is not None and t >= hit_time:
            anim_running = False
            break

def stop(event):
    global anim_running
    anim_running = False

# Create buttons
ax_start = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_stop = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_start = Button(ax_start, 'Start')
btn_stop = Button(ax_stop, 'Stop')
btn_start.on_clicked(start)
btn_stop.on_clicked(stop)

# Initialize plot
dot.set_data([], [])
trail.set_data([], [])
plt.ion()  # Turn on interactive mode
plt.show()

plt.ioff()  # Turn off interactive mode
plt.show()  # Keep the plot open
