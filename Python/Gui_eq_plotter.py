import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

def plot_equation(show_grid):
    
    equation = entry.get()
    domain_from = float(domain_from_entry.get())
    domain_to = float(domain_to_entry.get())
    x = np.linspace(domain_from, domain_to, 1000)
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
    ax.set_title(r"$\mathrm{" + title + "}$", fontsize=16)
    ax.set_xlabel(r"$\mathrm{" + xlabel + "}$", fontsize=14)
    ax.set_ylabel(r"$\mathrm{" + ylabel + "}$", fontsize=14)
    if show_grid:
        ax.grid(True)
    else:
        ax.grid(False)
    plt.show()


def update_equation_label(*args):
    equation = entry.get()
    equation_label.config(text=equation)

root = tk.Tk()
root.title("Equation Plotter")
root.geometry("500x500")

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

domain_label = ttk.Label(root, text="Enter domain (From, To):")
domain_label.pack(pady=10)

domain_frame = ttk.Frame(root)
domain_frame.pack()

domain_from_label = ttk.Label(domain_frame, text="From:")
domain_from_label.pack(side=tk.LEFT)

domain_from_entry = ttk.Entry(domain_frame)
domain_from_entry.pack(side=tk.LEFT)

domain_to_label = ttk.Label(domain_frame, text="To:")
domain_to_label.pack(side=tk.LEFT, padx=10)

domain_to_entry = ttk.Entry(domain_frame)
domain_to_entry.pack(side=tk.LEFT)

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

root.mainloop()
