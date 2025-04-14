import numpy as np
import matplotlib.pyplot as plt

# Function to generate and plot the step response
def plot_step_response(h):
    # Generate time values for the step response
    time_values = np.arange(0, len(h))

    # Generate the step input: u[n] = 1 for n >= 0
    u_n = np.ones(len(h))

    # Compute the step response by convolving h[n] with u[n]
    step_response = np.convolve(h, u_n, mode='full')[:len(h)]  # Convolution of h[n] with u[n]

    # Plot the step response
    plt.figure(figsize=(8, 6))
    plt.stem(time_values, step_response, basefmt=" ", label="Step Response")
    plt.title("Step Response of the System")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example impulse response for a system
    h = np.array([1, 1, 1, 1])  # Example h[n] (Impulse response)

    # Plot the step response
    plot_step_response(h)
