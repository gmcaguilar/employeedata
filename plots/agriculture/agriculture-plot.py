import matplotlib.pyplot as plt
import numpy as np

# Agriculture
def main():                                      
    with open("data.txt") as f:
        lines = f.read().splitlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines
]
    xs = range(len(x))  # prevents scatter() from sorting x automatically
    plt.xticks(xs, x)   # maps every xs to every x tick

    # convert data to numpy array of integers to avoid errors
    xt = np.asarray(xs, dtype=int) 
    yt = np.asarray(y, dtype=int) 
    
    # plot points
    plt.scatter(xt, yt) 

    # use least squares fit to find best model and plot the line 
    plt.plot(np.unique(xt), np.poly1d(np.polyfit(xt, yt, 3))(np.unique(xt)), 'm')    # cubic model

    # show only every 5th tick for a clean look
    ax = plt.subplot()
    for label in ax.xaxis.get_ticklabels()[::1]:
        label.set_visible(False)
    for label in ax.xaxis.get_ticklabels()[::5]:
        label.set_visible(True)

    # set x and y labels and title
    plt.xlabel("Date")
    plt.ylabel("Employees")
    plt.suptitle("Employees in Agriculture 2009-2017")

    
    plt.show()


if __name__ == "__main__":
    main()