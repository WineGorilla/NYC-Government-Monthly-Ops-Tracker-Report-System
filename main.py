# Load the external package
import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl as vb
from tkinter import ttk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk

# Load local functions
from scripts.calculation import vehicleCalculate, divisionCalculate
from scripts.fill import fillDivision, fillInfo
from scripts.process import processData
from scripts.utils import clean_value
from scripts.constants import *
from scripts.OpsTrackerApp import *

if __name__ == "__main__":
    root = tk.Tk()
    OpsTrackerApp(root)
    root.mainloop()
