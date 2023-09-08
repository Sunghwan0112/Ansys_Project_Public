import os
import shutil
import numpy as np
from tkinter import Tk, StringVar, DoubleVar, IntVar, ttk, Spinbox
from settings import (gold_gap_start, gold_gap_finish, algaas_gap_start, algaas_gap_finish,
                      N, stage1, stage2, stage3, AlGaAs_Bottom_Block, wave_length, mode_search,
                      n_search, pause_stage1, pause_stage2, pause_stage3,
                      choice, timeout, noise_level, mode_num, geo1_x, geo1_y, geo2_x, geo2_y,
                      geo3_x, geo3_y, geo4_x, geo4_y, geo5_x, geo5_y, geo6_x, geo6_y,
                      geo7_x, geo7_y, block_width, thickness)
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from mode import first_run, run
from settings import mode_search
from plot import plot_original, plot_smooth

# Author: Sunghwan Baek
# Version: 3.5
# Date: August 10th, 2023

basedir = os.getcwd()
simdir = basedir + '/GAAS_MOD_SIM'
outputdir = basedir + '/output'
refracitve_dir = basedir + '/refractive_indices'
indices = refracitve_dir + f'/mode_refractive_indices.npz'
npzfile = np.load(indices)
neff_list = npzfile['neff_list']
loss_list = npzfile['loss_list']


def save_settings():
    with open('settings.py', 'r') as f:
        lines = f.readlines()
    # line-1
    lines[11] = f"gold_gap_start = {gold_gap_start_var.get()}\n"
    lines[12] = f"gold_gap_finish = {gold_gap_finish_var.get()}\n"
    lines[13] = f"algaas_gap_start = {algaas_gap_start_var.get()}\n"
    lines[14] = f"algaas_gap_finish = {algaas_gap_finish_var.get()}\n"
    lines[16] = f"N = {gap_search_number.get()}\n"
    lines[20] = f"choice = '{material.get()}'\n"
    lines[22] = f"block_width = {block_width_var.get()}\n"
    lines[24] = f"thickness = {thickness_var.get()}\n"
    lines[26] = f"geo1_x = {geo1_x_var.get()}\n"
    lines[27] = f"geo1_y = {geo1_y_var.get()}\n"
    lines[29] = f"geo2_x = {geo2_x_var.get()}\n"
    lines[30] = f"geo2_y = {geo2_y_var.get()}\n"
    lines[33] = f"geo3_y = {geo3_y_var.get()}\n"
    lines[39] = f"geo5_y = {geo5_y_var.get()}\n"
    lines[42] = f"geo6_y = {geo6_y_var.get()}\n"
    lines[47] = f"wave_length = float({wave.get()})\n"
    lines[49] = f"mode_search = {mode_search_number.get()}\n"
    lines[51] = f"n_search = float({refractive_index_search.get()})\n"
    lines[53] = f"stage1 = {stage1_var.get()}\n"
    lines[54] = f"stage2 = {stage2_var.get()}\n"
    lines[55] = f"stage3 = {stage3_var.get()}\n"
    lines[61] = f"AlGaAs_Bottom_Block = {block.get()}\n"
    with open('settings.py', 'w') as f:
        f.writelines(lines)
    print("Settings are saved to settings.py")
    root.destroy()


def save_run_time():
    with open('settings.py', 'r') as f:
        lines = f.readlines()
    lines[67] = f"timeout = {run_setting_1_var.get()}\n"
    with open('settings.py', 'w') as f:
        f.writelines(lines)
    print("Run time setting is saved to settings.py")
    root.destroy()


def mode_save():
    print(basedir)
    source_path = simdir + f'\\target_mode_{spinbox.get()}_fixed.ldf'
    destination_path = basedir + '\\target_mode_fixed.ldf'
    # Use the shutil.copy2 method to replace the file
    print(f"mode#{spinbox.get()} is selected")
    shutil.copy2(source_path, destination_path)
    with open('settings.py', 'r') as f:
        lines = f.readlines()
    lines[65] = f"mode_num = {spinbox.get()}\n"
    with open('settings.py', 'w') as f:
        f.writelines(lines)
    root.destroy()


def toggle_stage1():
    if stage1_var.get() == 'Hide':
        stage1_var.set('Show')
    else:
        stage1_var.set('Hide')


def toggle_stage2():
    if stage2_var.get() == 'Hide':
        stage2_var.set('Show')
    else:
        stage2_var.set('Hide')


def toggle_stage3():
    if stage3_var.get() == 'Hide':
        stage3_var.set('Show')
    else:
        stage3_var.set('Hide')


def toggle_material():
    if material.get() == 'prediction':
        material.set('original')
    else:
        material.set('prediction')


def block_photo():
    if block.get() == 'Activate':
        image_path = simdir + f"\\Help_Image_with_block.png"
        image = Image.open(image_path)
        width = 500
        height = 250
        image = image.resize((width, height))

        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(basic_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=6, rowspan=6, padx=8)

    elif block.get() == 'Deactivate':
        image_path = simdir + f"\\Help_Image_without_block.png"
        image = Image.open(image_path)
        width = 500
        height = 250
        image = image.resize((width, height))

        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(basic_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=6, rowspan=6, padx=8)


def block_photo2():
    if block.get() == 'Activate':
        image_path2 = simdir + f"\\Help_Image_with_block2.png"
        image2 = Image.open(image_path2)
        width = 500
        height = 250
        image2 = image2.resize((width, height))

        photo2 = ImageTk.PhotoImage(image2)
        image_label2 = ttk.Label(advanced_frame, image=photo2)
        image_label2.image = photo2
        image_label2.grid(row=0, column=6, rowspan=8, padx=8)

    elif block.get() == 'Deactivate':

        image_path2 = simdir + f"\\Help_Image_without_block2.png"
        image2 = Image.open(image_path2)
        width = 500
        height = 250
        image2 = image2.resize((width, height))

        photo2 = ImageTk.PhotoImage(image2)
        image_label2 = ttk.Label(advanced_frame, image=photo2)
        image_label2.image = photo2
        image_label2.grid(row=0, column=6, rowspan=8, padx=8)


def toggle_block():
    if block.get() == 'Activate':
        block.set('Deactivate')
        image_path = simdir + f"\\Help_Image_without_block.png"
        image = Image.open(image_path)
        width = 500
        height = 250
        image = image.resize((width, height))

        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(basic_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=6, rowspan=6, padx=8)
        block_photo2()
    elif block.get() == 'Deactivate':
        block.set('Activate')
        image_path = simdir + f"\\Help_Image_with_block.png"
        image = Image.open(image_path)
        width = 500
        height = 250
        image = image.resize((width, height))

        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(basic_frame, image=photo)
        image_label.image = photo
        image_label.grid(row=0, column=6, rowspan=6, padx=8)
        block_photo2()


def print_value():
    print(spinbox.get())


def update_photo():
    image_path = simdir + f"\\mode{spinbox.get()}.jpg"
    image = Image.open(image_path)
    width = 100
    height = 100
    image = image.resize((width, height))

    photo = ImageTk.PhotoImage(image)
    image_label = ttk.Label(run_frame, image=photo)
    image_label.image = photo
    image_label.grid(row=3, column=2, rowspan=5, padx=5)
    label1_text.set(f"Refractive index is {neff_list[int(spinbox.get()) - 1]}")
    label2_text.set(f"Loss is {loss_list[int(spinbox.get()) - 1]} dB/m")


def save_noise():
    with open('settings.py', 'r') as f:
        lines = f.readlines()

    lines[71] = f"noise_level = {noise.get()}\n"

    with open('settings.py', 'w') as f:
        f.writelines(lines)

    print("noise is saved to settings.py")
    root.destroy()


root = Tk()
root.title("Ansys project")
style = ThemedStyle(root)
style.set_theme('aquativo')  # Set the theme

# Define a new style
style = ttk.Style()
style.configure("Custom.TButton",
                foreground="Black",
                background="Blue",
                font=('Arial', 10))

# Run Button Frame
run_frame = ttk.LabelFrame(root, text="Settings")
run_frame.pack(fill="x", side="top", padx=10, pady=10)
notebook = ttk.Notebook(run_frame)

basic_frame = ttk.Frame(notebook)
notebook.add(basic_frame, text="Basic Settings")

# Gold Gap
ttk.Label(basic_frame, text="Horizontal gap start").grid(row=0, column=0, sticky="w", padx=5, pady=5)
gold_gap_start_var = DoubleVar()
gold_gap_start_var.set(gold_gap_start)
ttk.Entry(basic_frame, textvariable=gold_gap_start_var, width=15).grid(row=0, column=1, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="m").grid(row=0, column=1, sticky="e", padx=5, pady=5)

ttk.Label(basic_frame, text="Horizontal gap finish").grid(row=1, column=0, sticky="w", padx=5, pady=5)
gold_gap_finish_var = DoubleVar()
gold_gap_finish_var.set(gold_gap_finish)
ttk.Entry(basic_frame, textvariable=gold_gap_finish_var, width=15).grid(row=1, column=1, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="m").grid(row=1, column=1, sticky="e", padx=5, pady=5)

# AlGaAs Gap
ttk.Label(basic_frame, text="Vertical gap start").grid(row=2, column=0, sticky="w", padx=5, pady=5)
algaas_gap_start_var = DoubleVar()
algaas_gap_start_var.set(algaas_gap_start)
ttk.Entry(basic_frame, textvariable=algaas_gap_start_var, width=15).grid(row=2, column=1, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="m").grid(row=2, column=1, sticky="e", padx=5, pady=5)

ttk.Label(basic_frame, text="Vertical gap finish").grid(row=3, column=0, sticky="w", padx=5, pady=5)
algaas_gap_finish_var = DoubleVar()
algaas_gap_finish_var.set(algaas_gap_finish)
ttk.Entry(basic_frame, textvariable=algaas_gap_finish_var, width=15).grid(row=3, column=1, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="m").grid(row=3, column=1, sticky="e", padx=5, pady=5)

ttk.Label(basic_frame, text="Gap searching number").grid(row=4, column=0, sticky="w", padx=5, pady=5)
gap_search_number = IntVar()
gap_search_number.set(N)
ttk.Entry(basic_frame, textvariable=gap_search_number, width=15).grid(row=4, column=1, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="points").grid(row=4, column=1, sticky="e", padx=5, pady=5)

ttk.Label(basic_frame, text="Mode searching number").grid(row=5, column=0, sticky="w", padx=5, pady=5)
mode_search_number = IntVar()
mode_search_number.set(mode_search)
ttk.Entry(basic_frame, textvariable=mode_search_number, width=15).grid(row=5, column=1, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="points").grid(row=5, column=1, sticky="e", padx=5, pady=5)

ttk.Label(basic_frame, text="Wave length").grid(row=0, column=2, sticky="w", padx=5, pady=5)
wave = DoubleVar()
wave.set(wave_length)
ttk.Entry(basic_frame, textvariable=wave, width=15).grid(row=0, column=3, sticky="w", padx=5, pady=5)
ttk.Label(basic_frame, text="m").grid(row=0, column=3, sticky="e", padx=5, pady=5)

ttk.Label(basic_frame, text="Refractive index search").grid(row=1, column=2, sticky="w", padx=5, pady=5)
refractive_index_search = DoubleVar()
refractive_index_search.set(n_search)
ttk.Entry(basic_frame, textvariable=refractive_index_search, width=15).grid(row=1, column=3, sticky="w", padx=5, pady=5)

ttk.Label(basic_frame, text="Material").grid(row=2, column=2, sticky="w", padx=5, pady=5)
material = StringVar()
material.set(f'{choice}')
ttk.Button(basic_frame, textvariable=material, command=toggle_material).grid(row=2, column=3, sticky="w", padx=5,
                                                                             pady=5)

ttk.Label(basic_frame, text="Bottom Block").grid(row=3, column=2, sticky="w", padx=5, pady=5)
block = StringVar()
if AlGaAs_Bottom_Block:
    block.set('Activate')
else:
    block.set('Deactivate')
ttk.Button(basic_frame, textvariable=block, command=toggle_block).grid(row=3, column=3, sticky="w", padx=5, pady=5)
block_photo()

# Advanced Settings Frame
advanced_frame = ttk.Frame(notebook)
notebook.add(advanced_frame, text="Advanced Settings")

# Advanced Setting 1
ttk.Label(advanced_frame, text="geo1_x").grid(row=0, column=0, sticky="w", padx=5, pady=5)
notebook.pack(padx=10, pady=10, fill="both", expand=True)
geo1_x_var = DoubleVar()
geo1_x_var.set(geo1_x)
ttk.Entry(advanced_frame, textvariable=geo1_x_var, width=15).grid(row=0, column=1, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=0, column=1, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo1_y").grid(row=1, column=0, sticky="w", padx=5, pady=5)
geo1_y_var = DoubleVar()
geo1_y_var.set(geo1_y)
ttk.Entry(advanced_frame, textvariable=geo1_y_var, width=15).grid(row=1, column=1, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=1, column=1, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo2_x").grid(row=2, column=0, sticky="w", padx=5, pady=5)
geo2_x_var = DoubleVar()
geo2_x_var.set(geo2_x)
ttk.Entry(advanced_frame, textvariable=geo2_x_var, width=15).grid(row=2, column=1, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=2, column=1, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo2_y").grid(row=3, column=0, sticky="w", padx=5, pady=5)
geo2_y_var = DoubleVar()
geo2_y_var.set(geo2_y)
ttk.Entry(advanced_frame, textvariable=geo2_y_var, width=15).grid(row=3, column=1, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=3, column=1, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo3_x").grid(row=4, column=0, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Block width").grid(row=4, column=1, sticky="w", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo3_y").grid(row=5, column=0, sticky="w", padx=5, pady=5)
geo3_y_var = DoubleVar()
geo3_y_var.set(geo3_y)
ttk.Entry(advanced_frame, textvariable=geo3_y_var, width=15).grid(row=5, column=1, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=5, column=1, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo4_x").grid(row=6, column=0, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Block width").grid(row=6, column=1, sticky="w", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo4_y").grid(row=7, column=0, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Vertical gap"). \
    grid(row=7, column=1, sticky="w", padx=5, pady=5)

# Line separator
separator = ttk.Separator(advanced_frame, orient='vertical')
separator.grid(row=0, column=2, rowspan=10, sticky='ns', padx=10, pady=10)

ttk.Label(advanced_frame, text="geo5_x").grid(row=0, column=3, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Block width").grid(row=0, column=4, sticky="w", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo5_y").grid(row=1, column=3, sticky="w", padx=5, pady=5)
geo5_y_var = DoubleVar()
geo5_y_var.set(geo5_y)
ttk.Entry(advanced_frame, textvariable=geo5_y_var, width=15).grid(row=1, column=4, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=1, column=4, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo6_x").grid(row=2, column=3, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Block width").grid(row=2, column=4, sticky="w", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo6_y").grid(row=3, column=3, sticky="w", padx=5, pady=5)
geo6_y_var = DoubleVar()
geo6_y_var.set(geo6_y)
ttk.Entry(advanced_frame, textvariable=geo6_y_var, width=15).grid(row=3, column=4, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=3, column=4, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo7_x").grid(row=4, column=3, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Block width").grid(row=4, column=4, sticky="w", padx=5, pady=5)

ttk.Label(advanced_frame, text="geo7_y").grid(row=5, column=3, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="Vertical gap"). \
    grid(row=5, column=4, sticky="w", padx=5, pady=5)

ttk.Label(advanced_frame, text="Block width").grid(row=6, column=3, sticky="w", padx=5, pady=5)
block_width_var = DoubleVar()
block_width_var.set(block_width)
ttk.Entry(advanced_frame, textvariable=block_width_var, width=15).grid(row=6, column=4, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=6, column=4, sticky="e", padx=5, pady=5)

ttk.Label(advanced_frame, text="Thickness").grid(row=7, column=3, sticky="w", padx=5, pady=5)
thickness_var = DoubleVar()
thickness_var.set(thickness)
ttk.Entry(advanced_frame, textvariable=thickness_var, width=15).grid(row=7, column=4, sticky="w", padx=5, pady=5)
ttk.Label(advanced_frame, text="m").grid(row=7, column=4, sticky="e", padx=5, pady=5)

block_photo2()

# Display Settings Frame
display_frame = ttk.Frame(notebook)
notebook.add(display_frame, text="Display Settings")

# Stage1
ttk.Label(display_frame, text="Stage 1").grid(row=0, column=0, sticky="w", padx=5, pady=5)
stage1_var = StringVar()
if stage1:
    stage1_var.set("Hide")
else:
    stage1_var.set("show")
ttk.Button(display_frame, textvariable=stage1_var, command=toggle_stage1).grid(row=0, column=1, sticky="w", padx=5,
                                                                               pady=5)

# Stage2
ttk.Label(display_frame, text="Stage 2").grid(row=1, column=0, sticky="w", padx=5, pady=5)
stage2_var = StringVar()
if stage2:
    stage2_var.set("Hide")
else:
    stage2_var.set("show")
ttk.Button(display_frame, textvariable=stage2_var, command=toggle_stage2).grid(row=1, column=1, sticky="w", padx=5,
                                                                               pady=5)

# Stage3
ttk.Label(display_frame, text="Stage 3").grid(row=2, column=0, sticky="w", padx=5, pady=5)
stage3_var = StringVar()
if stage3:
    stage3_var.set("Hide")
else:
    stage3_var.set("show")
ttk.Button(display_frame, textvariable=stage3_var, command=toggle_stage3).grid(row=2, column=1, sticky="w", padx=5,
                                                                               pady=5)

# Save Button Frame
save_frame = ttk.Frame(root)
save_frame.pack(fill="x", side="top")

# Save Button
save_button = ttk.Button(save_frame, text="Update Settings", command=save_settings, style="Custom.TButton")
save_button.pack(side="right", padx=10, pady=10)

# Save Button Frame
exit_frame = ttk.Frame(root)
exit_frame.pack(fill="x", side="bottom")

# Exit Button
exit_button = ttk.Button(exit_frame, text="Exit", command=root.destroy)
exit_button.pack(side="right", padx=10, pady=10)

# Graph Button Frame
run_frame = ttk.LabelFrame(root, text="Graph Commands")
run_frame.pack(fill="x", side="bottom", padx=10, pady=10)

ttk.Label(run_frame, text="noise").grid(row=0, column=2, sticky="w", padx=5, pady=5)
noise = StringVar()
noise.set(noise_level)
ttk.Entry(run_frame, textvariable=noise, width=6).grid(row=0, column=3, sticky="w", padx=5, pady=5)
ttk.Label(run_frame, text="dB/m").grid(row=0, column=5, sticky="w", padx=5, pady=5)

graph_button = ttk.Button(run_frame, text="Graph", command=plot_original)
graph_button.grid(row=0, column=0, padx=10, pady=10)

graph_smooth_button = ttk.Button(run_frame, text="Smooth Graph", command=plot_smooth)
graph_smooth_button.grid(row=0, column=1, padx=10, pady=10)

noise_save_button = ttk.Button(run_frame, text="Save noise", command=save_noise, style="Custom.TButton")
noise_save_button.grid(row=0, column=6, padx=10, pady=10)

# Run Button Frame
run_frame = ttk.LabelFrame(root, text="Run Commands")
run_frame.pack(fill="x", side="bottom", padx=10, pady=10)

Collecting_button = ttk.Button(run_frame, text="Run Start", command=run)
Collecting_button.grid(row=0, column=0, padx=10, pady=10)

# Run Button Frame
run_frame = ttk.LabelFrame(root, text="First Run Commands")
run_frame.pack(fill="x", side="bottom", padx=10, pady=10)

# First Run Button
first_run_button = ttk.Button(run_frame, text="First Run Start", command=first_run)
first_run_button.grid(row=0, column=0, padx=10, pady=10)

# First Run time Setting
ttk.Label(run_frame, text="time").grid(row=0, column=1, sticky="w", padx=5, pady=5)
run_setting_1_var = StringVar()
run_setting_1_var.set(timeout)
ttk.Spinbox(run_frame, from_=0, to=100, textvariable=run_setting_1_var, width=2).grid(row=0, column=1, sticky="e",
                                                                                      padx=5, pady=5)
ttk.Label(run_frame, text="seconds").grid(row=0, column=2, sticky="w", padx=5, pady=5)
save_run_time_button = ttk.Button(run_frame, text="Update time", command=save_run_time, style="Custom.TButton")
save_run_time_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")
# Line separator
separator = ttk.Separator(run_frame, orient='horizontal')
separator.grid(row=2, column=0, columnspan=7, sticky='ew', padx=10, pady=10)

# create mode label
ttk.Label(run_frame, text="mode #").grid(row=3, column=0, sticky="w")

# create spinbox
# create variable to hold spinbox value
spin_var = IntVar(value=mode_num)

# create spinbox, link it to spin_var
spinbox = Spinbox(run_frame, from_=1, to=mode_search, textvariable=spin_var, width=2, command=update_photo)

spinbox.grid(row=3, column=0, sticky="e")
# create a StringVar to hold the text
label1_text = StringVar()
label1_text.set(f"Refractive index is {neff_list[int(spinbox.get()) - 1]}")
label2_text = StringVar()
label2_text.set(f"Loss is {loss_list[int(spinbox.get()) - 1]} dB/m")
# create the label with label_text as the textvariable
label1 = ttk.Label(run_frame, textvariable=label1_text)
label1.grid(row=6, column=3, sticky="w")
label2 = ttk.Label(run_frame, textvariable=label2_text)
label2.grid(row=7, column=3, sticky="w")

update_photo()
# create mode label
ttk.Label(run_frame,
          text="After the first simulation finishes, it's a good idea to change the mode number you're interested in.").grid(
    row=3, column=3, sticky="w")
ttk.Label(run_frame,
          text="To make sure your new selection is applied, remember to secure your changes by pressing the 'Save "
               "Mode' button.").grid(
    row=4, column=3, sticky="w")
first_run_button = ttk.Button(run_frame, text="Save mode", command=mode_save, style="Custom.TButton")
first_run_button.grid(row=7, column=0, padx=10, pady=10)

root.mainloop()
