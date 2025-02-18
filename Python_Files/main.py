# Rupesh Jeyaram 
# Created July 16th, 2019

# This script should be the executive of the bokeh application
# Code for each plot or tab may come from a different file, but
# this file is the boss. 

# Bokeh basics 
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Each tab is drawn by one script
from scripts.US_SIF import US_SIF_tab

# Create each tab
tab1 = US_SIF_tab()

# Put all the tabs together
tabs = Tabs(tabs = [tab1])

# Assign the tabs to the root
curdoc().add_root(tabs)