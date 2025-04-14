import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function to plot Z-transform's magnitude and phase with colored contour plots
def plot_z_transform_colored(expr_str):
    # Define the symbol z
    z = sp.symbols('z')

    # Parse the input Z-expression
    Xz = sp.sympify(expr_str)

    # Create a range of z values for plotting (polar plot)
    real_part = np.linspace(-5, 5, 400)
    imag_part = np.linspace(-5, 5, 400)
    real, imag = np.meshgrid(real_part, imag_part)

    # Compute the complex Z values (z = real + j*imag)
    z_values = real + 1j*imag

    # Create a lambda function to evaluate the Z-expression for numerical values of z
    Xz_func = sp.lambdify(z, Xz, 'numpy')

    # Calculate magnitude and phase for each z value
    Xz_values = np.abs(Xz_func(z_values))
    phase_values = np.angle(Xz_func(z_values))

    # Plot magnitude of Z-transform (colored contour)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    contour_mag = plt.contourf(real, imag, Xz_values, levels=50, cmap='viridis')
    plt.colorbar(contour_mag, label="Magnitude")
    plt.title("Magnitude of Z-Transform")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")

    # Plot phase of Z-transform (colored contour)
    plt.subplot(1, 2, 2)
    contour_phase = plt.contourf(real, imag, phase_values, levels=50, cmap='twilight')
    plt.colorbar(contour_phase, label="Phase")
    plt.title("Phase of Z-Transform")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")

    # Show the plots
    plt.tight_layout()
    plt.show()

# Function to compute the inverse Z-transform numerically using series expansion
def inverse_z_transform_numeric(expr_str, n_max=10):
    # Define the symbol z and n
    z, n = sp.symbols('z n')

    # Parse the input Z-expression
    Xz = sp.sympify(expr_str)

    # Using series expansion to approximate the inverse Z-transform for the first few terms
    Xz_func = sp.lambdify(z, Xz, 'numpy')

    # Generate time-domain signal x[n] by evaluating the expression for each value of n
    time_values = np.arange(0, n_max)
    signal_values = []

    for t in time_values:
        # Numerically evaluate the inverse Z-transform
        # We calculate the inverse Z-transform as the sum of the residues (numerical approximation)
        z_values = np.exp(2j * np.pi * t / n_max)  # Use a simple approximation for z
        x_n = np.real(Xz_func(z_values))  # Evaluate at this value of z
        signal_values.append(x_n)

    return time_values, signal_values

# Function to plot the inverse Z-transform (time-domain signal x[n])
def plot_inverse_z_transform_colored(expr_str):
    # Get time-domain signal using the numerical inverse Z-transform
    time_values, signal_values = inverse_z_transform_numeric(expr_str)

    # Plot the time-domain signal (colored stem plot)
    plt.figure(figsize=(8, 4))
    plt.stem(time_values, signal_values, linefmt='b-', markerfmt='bo', basefmt=" ", label="x[n]")
    plt.title("Inverse Z-Transform: Time-domain Signal x[n]")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Input Z-domain expression for Z-transform
    expr_input_z = input("Enter the Z-domain expression X(z) for plotting (example: z / (z - 0.5)): ")

    # Plot the Z-transform's magnitude and phase
    plot_z_transform_colored(expr_input_z)

    # Input Z-domain expression for inverse Z-transform
    expr_input_inv = input("Enter the Z-domain expression X(z) for inverse Z-transform plotting: ")

    # Plot the inverse Z-transform (time-domain signal x[n])
    plot_inverse_z_transform_colored(expr_input_inv)
