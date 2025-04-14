import sympy as sp

def z_transform(xn):
    z = sp.symbols('z')
    n = sp.symbols('n', integer=True)
    Xz = sum(x * z**(-i) for i, x in enumerate(xn))
    return sp.simplify(Xz)

# Example usage
if __name__ == "__main__":
    print("Enter the signal x[n] as comma-separated values (from n=0 onwards):")
    user_input = input("x[n] = ")
    try:
        # Convert input to a list of floats
        xn = [float(i.strip()) for i in user_input.split(",")]
        
        # Calculate and print the Z-transform
        result = z_transform(xn)
        print("\nZ-Transform X(z) =")
        sp.pprint(result, use_unicode=True)
    except ValueError:
        print("Error: Please enter a valid list of numeric values.")
    except Exception as e:
        print("An unexpected error occurred:", e)
