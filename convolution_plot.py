import numpy as np
import matplotlib.pyplot as plt

# Function to perform convolution and plot the result
def plot_convolution(x, h):
    # Perform the convolution of x[n] and h[n]
    y = np.convolve(x, h, mode='full')

    # Generate time axis for the output signal
    time_values = np.arange(0, len(y))

    # Plot the convolution result
    plt.figure(figsize=(8, 6))
    plt.stem(time_values, y, basefmt=" ", linefmt="b-", markerfmt="bo", label="y[n] = x[n] * h[n]")
    plt.title("Convolution of x[n] and h[n]")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example input signals
    x = np.array([1, 2, 3, 4, 5])  # Example x[n]
    h = np.array([1, 1, 1])        # Example h[n]

    # Plot the convolution of x[n] and h[n]
    plot_convolution(x, h)
