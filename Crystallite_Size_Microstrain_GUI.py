import numpy as np
import tkinter as tk
from tkinter import messagebox

lambda1 = 0.15406  # Wavelength
k = 0.94  # Constant

def calculate_values():
    try:
        theta_degrees_input = theta_entry.get()
        theta_degrees = np.array([float(theta) for theta in theta_degrees_input.split()])

        num_thetas = len(theta_degrees)

        hwhm_values_input = hwhm_entry.get()
        hwhm_values = np.array([float(hwhm) for hwhm in hwhm_values_input.split()])

        num_hwhms = num_thetas

        theta_radians = np.deg2rad(theta_degrees)
        fwhm_degrees = hwhm_values * 2
        fwhm_radians = np.deg2rad(fwhm_degrees)

        CS = (k * lambda1) / ((fwhm_radians) * (np.cos(theta_radians)))

        microstrain = fwhm_radians / (4 * np.tan(theta_radians))
        eta = microstrain

        CS_avg = np.mean(CS)
        eta_avg = np.mean(eta)

        result_text = f"Input 2Theta values (degrees): {theta_degrees}\n"
        result_text += f"2Theta values (radians): {theta_radians}\n"
        result_text += f"HWHM values: {hwhm_values}\n"
        result_text += f"FWHM values (degrees): {fwhm_degrees}\n"
        result_text += f"FWHM values (radians): {fwhm_radians}\n"
        result_text += f"Crystallite Size (CS in nm) for each peak: {CS}\n"
        result_text += f"Average Crystallite Size (CS_avg in nm): {CS_avg}\n"
        result_text += f"Eta values: {eta}\n"
        result_text += f"Average Microstrain (Eta_avg): {eta_avg}\n"

        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete("1.0", tk.END)  # Clear previous text
        result_textbox.insert(tk.END, result_text)  # Insert new text
        result_textbox.config(state=tk.DISABLED)  # Disable editing

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for theta and HWHM.")


root = tk.Tk()
root.title("Crystallite Size Calculator")

# Theta values
theta_label = tk.Label(root, text="Theta values (degrees):")
theta_label.pack()

theta_entry = tk.Entry(root)
theta_entry.pack()

# HWHM values
hwhm_label = tk.Label(root, text="HWHM values:")
hwhm_label.pack()

hwhm_entry = tk.Entry(root)
hwhm_entry.pack()

# Button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate_values)
calculate_button.pack(pady=10)

# Result textbox
result_textbox = tk.Text(root, height=20, width=60)
result_textbox.pack()

root.mainloop()
