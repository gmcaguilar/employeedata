import numpy as np
import matplotlib.pyplot as plt


def main():                                      
    with open("data.txt") as f:
        lines = f.read().splitlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":
    main()