import matplotlib.pyplot as plt


def main():                                      
    with open("data.txt") as f:
        lines = f.read().splitlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]

    xs = range(len(x))  # prevents scatter() from sorting x automatically
    plt.scatter(xs, y)
    plt.xticks(xs, x) 
    plt.show()


if __name__ == "__main__":
    main()