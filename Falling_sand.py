import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import random

graph_col_size = 50
graph_row_size = 50
graph_middle_col = 25
anim_running = False
current_col = graph_middle_col
t = 0

# make values from -5 to 5, for this example
zvals = np.zeros((graph_row_size, graph_col_size))
# init the first block
#zvals[0, 5] = 1
# initialize the first block
zvals[0, graph_middle_col] = 1
# zvals[10, 4] = 1
# zvals[9, 5] = 1
# zvals[10, 6] = 1
def updatePlot(time):
    global zvals, img, current_col

    # Initialize the falling grain at the top
    zvals[0, graph_middle_col] = 1
    
    # Create a temporary buffer for the new positions
    new_zvals = zvals.copy()
    
    # Move existing sand grains down
    for row in range(graph_row_size - 1, 0, -1):
        for col in range(graph_col_size):
            if zvals[row, col] == 0 and zvals[row-1, col] == 1:
                new_zvals[row, col] = 1
                new_zvals[row-1, col] = 0
            elif zvals[row, col] == 1 and row < graph_row_size - 1:
                if zvals[row+1, col] == 0:
                    new_zvals[row+1, col] = 1
                    new_zvals[row, col] = 0
                elif (zvals[row+1, col-1]) == 0 and (zvals[row+1, col+1]) == 0:
                    col_incriment = random.choice([1, -1])
                    new_zvals[row + 1, col - col_incriment] = 1
                    new_zvals[row, col] = 0
                elif col > 0 and zvals[row+1, col-1] == 0:
                    new_zvals[row+1, col-1] = 1
                    new_zvals[row, col] = 0
                elif col < graph_col_size - 1 and zvals[row+1, col+1] == 0:
                    new_zvals[row+1, col+1] = 1
                    new_zvals[row, col] = 0

    # Update the main grid with the new positions
    zvals = new_zvals

    # Update the image data
    img.set_array(zvals)
    plt.draw()
    print("time:", time)




# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['white', 'blue','black'])

# tell imshow about color map so that only set colors are used
img = plt.imshow(zvals, interpolation='nearest', cmap=cmap)

ax = plt.gca()

ax.set_xticks(np.arange(-0.5, graph_col_size, 1), minor=True)
ax.set_yticks(np.arange(-0.5, graph_col_size, 1), minor=True)

# Disable x and y ticks
ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

ax.grid(which='minor', color='k', linestyle='-', linewidth=0.5)

def start(event):
    global anim_running, t
    anim_running = True
    while anim_running:
        plt.pause(0.001)  # Adjust the pause duration as needed
        updatePlot(t)
        t += 1

def stop(event):
    global anim_running
    anim_running = False
    print("final zvals: " ,zvals)

# Create buttons
ax_start = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_stop = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_start = Button(ax_start, 'Start')
btn_stop = Button(ax_stop, 'Stop')
btn_start.on_clicked(start)
btn_stop.on_clicked(stop)

plt.ion()  # Turn on interactive mode
plt.show()

plt.ioff()  # Turn off interactive mode
plt.show()  # Keep the plot open
