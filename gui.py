import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

class ZTransformGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Z-Transform Visualizer")

        # Input for Z-transform
        tk.Label(master, text="Z-domain Expression for Z-Transform:").pack()
        self.entry_z_transform = tk.Entry(master, width=50)
        self.entry_z_transform.pack()

        self.plot_button = tk.Button(master, text="Plot Z-Transform", command=self.plot_z_transform)
        self.plot_button.pack(pady=5)

        # Input for inverse Z-transform
        tk.Label(master, text="Z-domain Expression for Inverse Z-transform:").pack()
        self.entry_inverse_z_transform = tk.Entry(master, width=50)
        self.entry_inverse_z_transform.pack()

        self.inverse_plot_button = tk.Button(master, text="Plot Inverse Z-Transform", command=self.plot_inverse_z_transform)
        self.inverse_plot_button.pack(pady=5)

        # Placeholder frame for the plots
        self.plot_frame = tk.Frame(master)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = None  # For matplotlib canvas

    def clear_canvas(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

    def plot_z_transform(self):
        expr_str = self.entry_z_transform.get()
        if not expr_str:
            messagebox.showerror("Error", "Please enter a Z-domain expression.")
            return

        try:
            z = sp.symbols('z')
            Xz = sp.sympify(expr_str)

            real_part = np.linspace(-5, 5, 400)
            imag_part = np.linspace(-5, 5, 400)
            real, imag = np.meshgrid(real_part, imag_part)
            z_values = real + 1j * imag

            Xz_func = sp.lambdify(z, Xz, 'numpy')
            Xz_values = Xz_func(z_values)
            mag_values = np.abs(Xz_values)
            phase_values = np.angle(Xz_values)

            # Clear old canvas
            self.clear_canvas()

            # Create new figure
            fig, axs = plt.subplots(1, 2, figsize=(10, 4))
            fig.suptitle("Z-Transform")

            c1 = axs[0].contourf(real, imag, mag_values, levels=50, cmap='viridis')
            axs[0].set_title("Magnitude")
            axs[0].set_xlabel("Re(z)")
            axs[0].set_ylabel("Im(z)")
            fig.colorbar(c1, ax=axs[0])

            c2 = axs[1].contourf(real, imag, phase_values, levels=50, cmap='twilight')
            axs[1].set_title("Phase")
            axs[1].set_xlabel("Re(z)")
            axs[1].set_ylabel("Im(z)")
            fig.colorbar(c2, ax=axs[1])

            self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_inverse_z_transform(self):
        expr_str = self.entry_inverse_z_transform.get()
        if not expr_str:
            messagebox.showerror("Error", "Please enter a Z-domain expression.")
            return

        try:
            z = sp.symbols('z')
            Xz = sp.sympify(expr_str)
            Xz_func = sp.lambdify(z, Xz, 'numpy')

            n_max = 20
            time_values = np.arange(0, n_max)
            signal_values = []

            for n in time_values:
                angle = 2 * np.pi * n / n_max
                z_val = np.exp(1j * angle)
                x_n = np.real(Xz_func(z_val))
                signal_values.append(x_n)

            # Clear old canvas
            self.clear_canvas()

            # Plot time-domain signal
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.stem(time_values, signal_values)  # Removed deprecated use_line_collection
            ax.set_title("Inverse Z-Transform")
            ax.set_xlabel("n")
            ax.set_ylabel("x[n]")
            ax.grid(True)

            self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", str(e))

# Run the GUI
root = tk.Tk()
app = ZTransformGUI(root)
root.mainloop()
