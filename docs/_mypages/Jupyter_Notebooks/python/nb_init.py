#===============================
# ADD FOLDER TO MODULES PATH
#===============================

import sys
sys.path.insert(0, './python/')


#====================================
# GENERAL MODULES IMPORT
#====================================

# write HTML, and LaTeX in Markdown cells
from IPython.display import display, Math, Latex, HTML, SVG

# reload modules without restarting the kernel
from imp import reload

# Execute Shell commands
import subprocess

# scientific calculations
import numpy as np

from pint import UnitRegistry     # units of measurements, 'pip install -U pint'
unit = UnitRegistry()             # ex: 3*udm.m, 45*udm.cm, A.to(udm.km) conversion,...

# System
import os


#================
# CSS STYLE
#================
style_sheet = './style/style_unina_iwes.css'
display(HTML(open(style_sheet, 'r').read()))


#====================================
# PLOTTING AND DISPLAYING DEFAULTS
#====================================

from IPython.display import set_matplotlib_formats
import matplotlib.pyplot as plt
from cycler import cycler

set_matplotlib_formats('pdf', 'png')

plt.rcParams['savefig.dpi'] = 600
plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = (12.3, 5)

plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.prop_cycle'] = cycler('color', 'rgbcmyk') # needs module cycler

plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

plt.rcParams['font.size'] = 16

plt.rcParams['lines.linestyle'] = '-'
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['lines.markeredgewidth'] = 2.0

plt.rcParams['legend.fontsize'] = 14