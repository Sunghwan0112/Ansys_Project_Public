Author: Sunghwan Baek
Version: 3.5
Date: August 10th, 2023

Almost every variable can be controlled by the 'main.py' file.

I made a Tkinter user interface, and by clicking the 'save' buttons, settings can be saved. 
(You will know each variable by opening the settings.py file, and I added annotation for each line)

You can modify the values in the 'settings.py' file, but don't change the line placement of the code. 
Each line is linked to the 'main.py' file. 
So, if a code is on line 11, keep it on line 11. Moving lines will disrupt the 'main.py' and cause errors.
In the 'Graph Commands' section of the 'main.py' interface:
- Clicking 'Graph' displays the original graph made from collected data.
- 'Smooth Graph' shows a visually refined version of that graph.
Both options always display the latest graph.

In the 'settings.py' file:
- Set 'manual_plot' to control graphing mode.
    - 'manual_plot = False': auto mode, shows the latest data.
    - 'manual_plot = True': manual mode, lets you pick a specific file.
- In manual mode, specify the file by setting 'manual_result' like this: 'manual_result = filename.npz'. 
Make sure your file ends with '.npz'.
Once set, both 'Graph' and 'Smooth Graph' will display the chosen file.


Graph Explanation:

1. Original Loss vs (Horizontal gap, Vertical gap): 
   - Reflects the loss when no electric field is applied.
   - AlGaAs and GaAs refractive indices aren't influenced by the electro-optic effect.

2. Bias Loss vs (Horizontal gap, Vertical gap):
   - Reflects the loss when the electric field is applied.
   - Demonstrates the loss with the electro-optic effect in play.
   - Electric fields alter AlGaAs and GaAs refractive indices due to this effect.

3. Vpil vs (Horizontal gap, Vertical gap):
   - Represents Vpil derived from the difference between Original and Bias Losses.

4. Insertion Loss vs (Horizontal gap, Vertical gap):
   - The crucial loss metric we're focusing on (measured in dB).
   - Derived using the Bias Loss and Vpil.


After making changes in the 'main.py' interface, remember to click the save button. If not, it'll use the old settings.

In the 'output' directory, text outputs from the Python program are automatically stored. 
While these outputs are not suitable for graphing, they offer insight into the simulation's proceedings. 
Each file is timestamped to reflect the program's start time.

Within the 'output' directory, there are two subfolders:
   1. 'First_run': This contains data from the preliminary 'First Run'.
   2. 'Result': This is dedicated to the primary data collection phase, termed 'Run'.

Separately, in the 'result' directory, data originating from the Ansys program is saved. Each of these files also carries a timestamp in its name and is suitable for graphical representation.
I've put two sample files in there: '11x11_original.npz' and '11x11_prediction.npz' so you can see what they look like.

****************************************************************************************************************************************************************************

Let's go through the libraries used in the code:

1. os: This module provides a portable way of using operating system dependent functionality like reading or writing to the file system.

2. sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

3. numpy (imported as `np`): Numpy is the core library for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

4. scipy.interpolate: This is a module within SciPy that provides functions for interpolating values. 

5. datetime: This module supplies classes for manipulating dates and times. It can help with tasks such as formatting and parsing dates/times, arithmetic operations on dates, and more.

6. pathlib: This is a module for manipulating filesystem paths in a more object-oriented manner than using `os` and `os.path`.

7. shutil: This module provides higher-level file operations than what the `os` module provides. It's useful for tasks such as copying or moving files and directories.

8. time: This module provides various time-related functions, like getting the current time, sleeping for a certain duration, and more.

9. queue: This module provides implementations of multi-producer, multi-consumer queues. It's useful for threading operations.

10. threading: This module provides a way to create and manage threads in Python, facilitating parallel execution.

11. glob: This module is used to find all the pathnames matching a specified pattern, like searching for all files with a specific extension in a directory.

12. matplotlib.pyplot (imported as `plt`): This is a plotting library for Python. It allows you to create a wide range of static, animated, and interactive visualizations.

13. tkinter: This is the standard Python interface to the Tk GUI toolkit. It provides tools to create interactive GUI applications.

14. ttkthemes: This module provides additional themes for tkinter's `ttk` module, enhancing the visual appeal of tkinter applications.

15. PIL (from `PIL import Image, ImageTk`): The Python Imaging Library (PIL) provides extensive capabilities for image processing. `Image` and `ImageTk` modules help with opening, manipulating, and displaying images in various formats.

Libraries the user needs to download:

From the standard Python library (no need to install separately):
- os
- sys
- datetime
- pathlib
- shutil
- time
- queue
- threading
- glob
- tkinter

These need to be installed (usually via `pip`):
- numpy
- scipy
- matplotlib
- ttkthemes
- PIL

To install the additional libraries, the user can use `pip`:

For example,

pip install numpy scipy matplotlib ttkthemes

This command installs the necessary third-party libraries listed above.
