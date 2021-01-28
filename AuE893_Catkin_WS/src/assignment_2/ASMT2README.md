Navigation

/Here comes the Navigation picture


As elaborated in the picture, the 'src' folder contains the three python files -- For Circle, for Openloop Square and for Closed loop square. These files can simply run by executing their respective launch files in the launch folder. The launch files take care of running the roscore and turtlesim node.

Plotting Circle:
The basic algorithm for this program is that the turtle has been given a fixed linear and angular velocity which automatically traces a circle and keeps doing it untill the node is killed. Check the video here

Openloop Square:
The logic behind this program is that first the turtle goes straigh with constant linear velocity for a distance of 2 units, stops, rotates 90 Degrees and repeats. Eventually the circle traces a square of 2x2 units and keeps on doing it untill the node is killed. Check the video here.

Closed Loop Square:
The program follows the idea of 'Go to Goal' algorithm discussed in class. Each corner of square is set as a goal for the turtle, whiich it navigates to using a Proportional contoller. The controller parameters have been tuned manually to give the maximum appeareance of the square. Check the video here.
