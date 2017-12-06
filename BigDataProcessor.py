from tkinter import *



import matplotlib.pyplot as plt
import numpy as np


def main(): 

    root = Tk()
    root.title("Big Data Processor")
    L1 = Label(root, text="Enter file name:")
    L1.pack( side = LEFT)
    E1 = Entry(root)
    E1.pack(side = LEFT)
    B1= Button(text = "create graph", command = lambda: graph(E1))
    B1.pack(side = LEFT)
    root.mainloop()

def graph(file):
    with open(file.get()) as f:
        lines = f.read().splitlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]

    xs = range(len(x))  # prevents scatter() from sorting x automatically
    plt.xticks(xs, x)   # maps every xs to every x tick

    # convert x and y to numpy array of integers for compatibility
    xt = np.asarray(xs, dtype=int) 
    yt = np.asarray(y, dtype=int)  

    plt.scatter(xt, yt)  # plot data points

    # use least squares fit to find best model and plot the line 
    plt.plot(np.unique(xt), np.poly1d(np.polyfit(xt, yt, 3))(np.unique(xt)), 'm')    # cubic model

    # show only every 5th tick for a clean look
    ax = plt.subplot()
    for label in ax.xaxis.get_ticklabels()[::1]:
        label.set_visible(False)
    for label in ax.xaxis.get_ticklabels()[::5]:
        label.set_visible(True)


    plt.show()


if __name__ == "__main__":
    main()
