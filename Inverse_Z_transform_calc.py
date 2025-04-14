import sympy as sp

# Define the symbols
z, n = sp.symbols('z n')

# Function for manual partial fraction decomposition and inverse Z-transform calculation
def manual_inverse_z_transform(expr_str):
    try:
        # Parse the input Z-expression
        Xz = sp.sympify(expr_str)

        # Perform partial fraction decomposition
        partial_fraction = sp.apart(Xz, z)

        # Now, we take the inverse Z-transform term by term
        result = []
        for term in partial_fraction.as_ordered_terms():
            # For each term, we identify its form and compute the inverse Z-transform manually
            if isinstance(term, sp.Rational):
                result.append("delta[n]")  # For a constant term, the inverse Z-transform is a delta function
            elif isinstance(term, sp.Mul):
                # For terms like (z/(z-a)), the inverse Z-transform is a^n * u[n]
                factor = term.args[0]  # The term inside the (z-a) factor
                if factor == z:
                    result.append("delta[n]")  # Inverse Z-transform for z (just a delta function)
                else:
                    result.append(f"{factor}^n * u[n]")  # For terms like (z/(z-a)), the inverse Z-transform is a^n * u[n]

        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Input Z-domain expression
    expr_input = input("Enter the Z-domain expression X(z) (example: z / (z - 0.5)): ")

    # Call the manual inverse Z-transform function
    result = manual_inverse_z_transform(expr_input)

    # Display the results
    if isinstance(result, list):
        print("\nInverse Z-Transform x[n]:")
        for r in result:
            print(r)
    else:
        print(result)
