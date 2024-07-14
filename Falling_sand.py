import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import random

graph_col_size = 11
graph_row_size = 11
graph_middle_col = 6
anim_running = False
current_col = graph_middle_col
t = 0

# make values from -5 to 5, for this example
zvals = np.zeros((graph_row_size, graph_col_size))
# init the first block
#zvals[0, 5] = 1
# initialize the first block
zvals[0, 0] = 0.1
# zvals[10, 4] = 1
# zvals[9, 5] = 1
# zvals[10, 6] = 1

def updatePlot(time):
    global zvals, img, current_col
    
    if (current_col + 1 < graph_col_size and current_col - 1 > -1):
        if (time < graph_col_size and zvals[time, graph_middle_col] != 1) :
            zvals[time, graph_middle_col] = 1  # Set the current position to 1
            if (time > 0):
                zvals[time - 1, graph_middle_col] = 0  # Reset the previous position to 0 to create a falling effect.
        
        elif (zvals[time, current_col - 1] == 0 and zvals[time, current_col + 1] == 0):
            previous_col = current_col
            col_increment = random.choice([1, -1])
            current_col = current_col + col_increment
            zvals[time, current_col] = 1
            print("current_col: ", current_col)

            if (time > 0):
                zvals[time - 1, previous_col] = 0  # Reset the previous position to 0
        

            print("time: ", time,"left and right has position")



        elif (zvals[time, current_col + 1] == 0 and current_col + 1 < graph_col_size): ##
            previous_col = current_col
            col_increment = 1
            current_col = current_col + col_increment
            zvals[time, current_col] = 1
            print("current_col: ", current_col)

            if (time > 0):
                zvals[time - 1, previous_col] = 0  # Reset the previous position to 0
        
            print("time: ", time,"right has position")
    
        elif (zvals[time, current_col - 1] == 0):
            previous_col = current_col
            col_increment = -1
            current_col = current_col + col_increment
            zvals[time, current_col] = 1
            print("current_col: ", current_col)

            if (time > 0):
                zvals[time - 1, previous_col] = 0  # Reset the previous position to 0
        
            print("time: ", time,"left has position")
    


    img.set_array(zvals)  # Update the image data
    plt.draw()  # Redraw the current figure
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

# Button callbacks
def start(event):
    global anim_running, t, current_col
    anim_running = True
    while anim_running:
        plt.pause(0.01)  # Adjust the pause duration as needed
        updatePlot(t)
        t += 1

        if t == graph_col_size:
            t = 0   # reset the time when a block reaches to the bottom 
            # we have to reset the current_col here
            current_col = graph_middle_col
            #stop(None)  # Stop the animation when reaching the end, comment out this line if you want the falling sand to run forever. 

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
