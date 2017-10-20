import matplotlib.pyplot as plt
import numpy as np


def main():                                      
    with open("data.txt") as f:
        lines = f.read().splitlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]

    xs = range(len(x))  # prevents scatter() from sorting x automatically
    plt.xticks(xs, x)   # maps every xs to every x tick

    # x and y labels
    plt.xlabel("Month-Year")
    plt.ylabel("Employees")

    # compute trendline
    xt = np.asarray(xs, dtype=int) # trendline input to prevent type mismatch
    yt = np.asarray(y, dtype=int) # trendline input to prevent type mismathc
    plt.plot(np.unique(xt), np.poly1d(np.polyfit(xt, yt, 1))(np.unique(xt)))

    plt.scatter(xt, yt)  # plot
    plt.show()


if __name__ == "__main__":
    main()