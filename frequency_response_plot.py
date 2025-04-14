import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function to plot Frequency Response
def plot_frequency_response(expr_str):
    # Define the symbol z and omega (frequency)
    z, omega = sp.symbols('z omega')

    # Parse the input Z-expression
    Xz = sp.sympify(expr_str)

    # Substitute z = e^(jω) into the transfer function
    Xz_substituted = Xz.subs(z, sp.exp(sp.I * omega))  # Use sp.I for imaginary unit

    # Convert the expression to a numerical function
    Xz_func = sp.lambdify(omega, Xz_substituted, 'numpy')

    # Generate the frequency axis (omega)
    omega_values = np.linspace(-np.pi, np.pi, 400)

    # Compute the magnitude and phase of the frequency response
    magnitude = np.abs(Xz_func(omega_values))
    phase = np.angle(Xz_func(omega_values))

    # Plot the magnitude of the frequency response
    plt.figure(figsize=(12, 6))

    # Magnitude plot
    plt.subplot(1, 2, 1)
    plt.plot(omega_values, magnitude)
    plt.title("Magnitude of Frequency Response")
    plt.xlabel("Frequency (ω)")
    plt.ylabel("Magnitude |X(e^jω)|")
    plt.grid(True)

    # Phase plot
    plt.subplot(1, 2, 2)
    plt.plot(omega_values, phase)
    plt.title("Phase of Frequency Response")
    plt.xlabel("Frequency (ω)")
    plt.ylabel("Phase (rad)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Input Z-domain expression for Frequency Response
    expr_input = input("Enter the Z-domain expression X(z) for Frequency Response plotting (example: z / (z - 0.5)): ")

    # Plot the Frequency Response
    plot_frequency_response(expr_input)
