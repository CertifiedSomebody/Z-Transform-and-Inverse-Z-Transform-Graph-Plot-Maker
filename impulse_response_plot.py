import numpy as np
import matplotlib.pyplot as plt

# Function to generate and plot the impulse response
def plot_impulse_response(h):
    # Generate time values for the impulse response
    time_values = np.arange(0, len(h))

    # Plot the impulse response
    plt.figure(figsize=(8, 6))
    plt.stem(time_values, h, basefmt=" ", label="h[n] (Impulse Response)")
    plt.title("Impulse Response of the System")
    plt.xlabel("n")
    plt.ylabel("h[n]")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example: Allow user to input impulse response values
    input_values = input("Enter the impulse response h[n] (e.g., 1, -0.5, 0.25, 0.125): ")
    
    # Convert the input string into a numpy array
    h = np.array([float(x) for x in input_values.split(',')])

    # Plot the impulse response
    plot_impulse_response(h)
