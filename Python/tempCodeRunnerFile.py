import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

def plot_equation(show_grid):
    equation = entry.get()
    domain = domain_entry.get()
    x_min, x_max = [float(x.strip()) for x in domain.split(',')]
    x = np.linspace(x_min, x_max, 1000)
    y = eval(equation.replace("^", "**"))  # replace ^ with **
    fig, ax = plt.subplots()
    ax.plot(x, y, color='royalblue', linewidth=2)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.xaxis.set_tick_params(width=1.5)
    ax.yaxis.set_tick_params(width=1.5)
    title = title_entry.get()
    xlabel = xlabel_entry.get()
    ylabel = ylabel_entry.get()
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    if show_grid:
        ax.grid(True)
    else:
        ax.grid(False)
    plt.show()


def save_plot():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    plt.savefig(file_path, dpi=300)

def update_equation_label(*args):
    equation = entry.get()
    equation_label.config(text=equation)

root = tk.Tk()
root.title("Equation Plotter")
root.geometry("500x400")

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14))
style.configure('TButton', font=('Helvetica', 14))

label = ttk.Label(root, text="Enter equation:")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", update_equation_label)

equation_label = ttk.Label(root, text="")
equation_label.pack(pady=5)

domain_label = ttk.Label(root, text="Enter domain (e.g. -5,5):")
domain_label.pack(pady=10)

domain_entry = ttk.Entry(root)
domain_entry.pack()

title_label = ttk.Label(root, text="Enter plot title:")
title_label.pack(pady=10)

title_entry = ttk.Entry(root)
title_entry.pack()

xlabel_label = ttk.Label(root, text="Enter x-axis label:")
xlabel_label.pack(pady=10)

xlabel_entry = ttk.Entry(root)
xlabel_entry.pack()

ylabel_label = ttk.Label(root, text="Enter y-axis label:")
ylabel_label.pack(pady=10)

ylabel_entry = ttk.Entry(root)
ylabel_entry.pack()

grid_var = tk.BooleanVar()
grid_var.set(True)
grid_checkbutton = ttk.Checkbutton(root, text="Show grid", variable=grid_var)
grid_checkbutton.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

plot_button = ttk.Button(button_frame, text="Plot", command=lambda: plot_equation(grid_var.get()))
plot_button.pack(side=tk.LEFT, padx=10)

save_button = ttk.Button(button_frame, text="Save Plot", command=save_plot)
save_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
