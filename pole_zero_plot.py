import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Function to plot Pole-Zero plot
def plot_pole_zero(expr_str):
    # Define the symbol z
    z = sp.symbols('z')

    # Parse the input Z-expression
    Xz = sp.sympify(expr_str)

    # Compute the poles and zeros using sympy
    zeros = sp.solveset(Xz, z, domain=sp.S.Complexes)
    poles = sp.solveset(1 / Xz, z, domain=sp.S.Complexes)

    # Convert to numpy arrays for plotting
    # Ensure that we filter out complex infinity poles and zeros
    zeros = np.array([complex(z) for z in zeros if isinstance(z, sp.Complex)])
    poles = np.array([complex(p) for p in poles if isinstance(p, sp.Complex)])

    # Plot the poles and zeros in the complex plane
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), color='red', label='Poles')

    # Plot unit circle for reference
    unit_circle = plt.Circle((0, 0), 1, color='gray', linestyle='--', fill=False)
    plt.gca().add_artist(unit_circle)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.title('Pole-Zero Plot')
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    # Input Z-domain expression for Pole-Zero plot
    expr_input = input("Enter the Z-domain expression X(z) for Pole-Zero plotting (example: z / (z - 0.5)): ")

    # Plot the Pole-Zero plot
    plot_pole_zero(expr_input)
