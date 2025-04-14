# Z-Transform and Inverse Z-Transform Graph Plot Maker

## Overview
This application is a graphical user interface (GUI) tool that visualizes the Z-transform and its inverse. It helps users analyze and plot the magnitude and phase of Z-transforms, as well as compute and display the time-domain signal corresponding to the inverse Z-transform.

It uses Python with libraries such as `Tkinter` for the GUI, `SymPy` for symbolic math, and `Matplotlib` for plotting. The application allows users to enter Z-domain expressions, plot their corresponding Z-transform and inverse Z-transform, and visualize the results interactively.

## Features
- **Z-Transform Plot**: Input any Z-domain expression and visualize the magnitude and phase of the Z-transform in the complex plane.
- **Inverse Z-Transform Plot**: Enter a Z-domain expression and see the corresponding time-domain signal computed via the inverse Z-transform.
- **Interactive GUI**: Built with `Tkinter` to provide a simple and intuitive interface for users.

## Requirements
Before running this application, ensure that you have the following libraries installed:

- `matplotlib`
- `numpy`
- `sympy`
- `tkinter` (Usually comes pre-installed with Python)

You can install the required dependencies using `pip`:

```bash
pip install matplotlib numpy sympy

How to Run
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/CertifiedSomebody/Z-Transform-and-Inverse-Z-Transform-Graph-Plot-Maker.git
Navigate to the project directory:

bash
Copy
Edit
cd Z-Transform-and-Inverse-Z-Transform-Graph-Plot-Maker
Run the Python script:

bash
Copy
Edit
python z_transform_gui.py
The GUI will open, allowing you to input Z-domain expressions and plot the corresponding Z-transform and inverse Z-transform.

Usage
Z-Transform:
Enter a valid Z-domain expression (e.g., 1/(z - 0.5)).

Click the "Plot Z-Transform" button to generate the magnitude and phase plots of the Z-transform.

Inverse Z-Transform:
Enter a valid Z-domain expression (e.g., 1/(z - 0.5)).

Click the "Plot Inverse Z-Transform" button to compute and plot the corresponding time-domain signal.

Example
For a simple Z-domain expression like 1/(z - 0.5), the tool will:

Compute the magnitude and phase of the Z-transform.

Compute the inverse Z-transform and plot the corresponding time-domain signal.

Contributing
Feel free to fork this repository and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue.

License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

Contact
For any questions or inquiries, please reach out to the repository owner at sanjjha093@gmail.com
Made with :) by CertifiedSomebody ^-^
