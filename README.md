# moment-zero-map

The code here creates a moment 0 (K.km/s) map from a fits cube using python. 

# Code and resources
Python version: 3.9.9
Packages: aplpy, matplotlib

# Model Building

I used a 3D fits cube containing velocity, temperature and coordinates axes to make a 2D map by integrating temperature within a range of velocity (integral of Tdv). The attached code is in python. 
