# Graphene RGB

The code in this project generates a csv file of RGB intensities from an image. The line of coordinates between two specified points are are intensities that are saved in the csv. A plot and histogram of points are also generated. The purpose of this project was to determine the thickness of mechanically exfoliated FLG by using the table generated in "Rapid and Reliable Thickness Identification of Two-Dimensional Nanosheets Using Optical Microscopy".


# Installation requirements
```
python3
```

Required packages
```
pip3 install bresenham
pip3 install opencv-python
```

How to run

Modify the code in graphene.py and run it.
```
python3 graphene.py
```


# References
\[1\] Li, H., Wu, J., Huang, X., Lu, G., Yang, J., Lu, X., Xiong, Q. and Zhang, H. (2013). Rapid and Reliable Thickness Identification of Two-Dimensional Nanosheets Using Optical Microscopy. ACS Nano, 7(11), pp.10344-10353.
