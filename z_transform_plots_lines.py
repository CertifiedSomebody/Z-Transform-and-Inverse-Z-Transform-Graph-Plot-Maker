import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function to plot Z-transform's magnitude and phase (line plot)
def plot_z_transform_line(expr_str):
    # Define the symbol z
    z = sp.symbols('z')

    # Parse the input Z-expression
    Xz = sp.sympify(expr_str)

    # Create a range of z values for plotting (polar plot)
    real_part = np.linspace(-5, 5, 400)
    imag_part = np.linspace(-5, 5, 400)
    
    # Creating the grid for complex values of z
    real, imag = np.meshgrid(real_part, imag_part)
    z_values = real + 1j*imag

    # Create a lambda function to evaluate the Z-expression for numerical values of z
    Xz_func = sp.lambdify(z, Xz, 'numpy')

    # Calculate magnitude and phase for each z value
    Xz_values = np.abs(Xz_func(z_values))
    phase_values = np.angle(Xz_func(z_values))

    # Plot magnitude and phase (line plots on axes)
    plt.figure(figsize=(12, 6))

    # Plot the Magnitude
    plt.subplot(1, 2, 1)
    plt.plot(real_part, Xz_values[0, :], label='Magnitude vs Re(z)', color='blue')
    plt.plot(imag_part, Xz_values[:, 0], label='Magnitude vs Im(z)', color='red')
    plt.title("Magnitude of Z-Transform")
    plt.xlabel("Re(z) / Im(z)")
    plt.ylabel("Magnitude |X(z)|")
    plt.legend()
    plt.grid(True)

    # Plot the Phase
    plt.subplot(1, 2, 2)
    plt.plot(real_part, phase_values[0, :], label='Phase vs Re(z)', color='blue')
    plt.plot(imag_part, phase_values[:, 0], label='Phase vs Im(z)', color='red')
    plt.title("Phase of Z-Transform")
    plt.xlabel("Re(z) / Im(z)")
    plt.ylabel("Phase of X(z)")
    plt.legend()
    plt.grid(True)

    # Show the plots
    plt.tight_layout()
    plt.show()

# Function to compute inverse Z-transform using partial fraction expansion
def inverse_z_transform(expr_str):
    # Define symbols
    z, n = sp.symbols('z n')

    # Parse the input Z-expression
    Xz = sp.sympify(expr_str)

    # Compute the partial fraction decomposition
    partial_fraction = sp.apart(Xz, z)

    # Now evaluate each term numerically for n = 0 to 10
    time_domain_signal = []
    for i in range(10):
        # Substitute values for n and evaluate the term
        term = partial_fraction.subs(z, i).evalf()  # Use .evalf() to convert to float
        time_domain_signal.append(float(term))  # Convert to float for plotting

    return time_domain_signal

# Function to plot the inverse Z-transform (time-domain signal x[n])
def plot_inverse_z_transform(expr_str):
    # Calculate the inverse Z-transform using partial fractions
    time_domain_signal = inverse_z_transform(expr_str)

    # Generate values of x[n] for n = 0 to 10 (adjust depending on your function)
    time_values = np.arange(0, 10, 1)

    # Plot the time-domain signal
    plt.figure(figsize=(8, 4))
    plt.plot(time_values, time_domain_signal, marker='o', linestyle='-', color='blue')
    plt.title("Inverse Z-Transform: Time-domain Signal x[n]")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Input Z-domain expression for Z-transform
    expr_input_z = input("Enter the Z-domain expression X(z) for plotting (example: z / (z - 0.5)): ")

    # Plot the Z-transform's magnitude and phase
    plot_z_transform_line(expr_input_z)

    # Input Z-domain expression for inverse Z-transform
    expr_input_inv = input("Enter the Z-domain expression X(z) for inverse Z-transform plotting: ")

    # Plot the inverse Z-transform (time-domain signal x[n])
    plot_inverse_z_transform(expr_input_inv)
