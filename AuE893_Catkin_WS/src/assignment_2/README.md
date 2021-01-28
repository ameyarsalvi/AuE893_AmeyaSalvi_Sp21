# Assignment 2 : Navigation

![Assignment 2](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/blob/main/AuE893_Catkin_WS/src/assignment_2/Asmt2.png)




As elaborated in the picture, the 'src' folder contains the three python files -- For Circle, for Openloop Square and for Closed loop square. These files can simply run by executing their respective launch files in the launch folder. The launch files take care of running the roscore and turtlesim node.

Plotting Circle:
![Circle](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/blob/main/AuE893_Catkin_WS/src/assignment_2/Snapshots/circle.png)
The basic algorithm for this program is that the turtle has been given a fixed linear and angular velocity which automatically traces a circle and keeps doing it untill the node is killed. [Video](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/blob/main/AuE893_Catkin_WS/src/assignment_2/Videos/circle.mp4)

Openloop Square:
![Openloop Square](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/blob/main/AuE893_Catkin_WS/src/assignment_2/Snapshots/OLSquare.png)
The logic behind this program is that first the turtle goes straigh with constant linear velocity for a distance of 2 units, stops, rotates 90 Degrees and repeats. Eventually the circle traces a square of 2x2 units and keeps on doing it untill the node is killed. [Video](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/blob/main/AuE893_Catkin_WS/src/assignment_2/Videos/OpenLoopSquare.mp4)

Closed Loop Square:
![ClosedLoop Square](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/blob/main/AuE893_Catkin_WS/src/assignment_2/Snapshots/CLSquare.png)
The program follows the idea of 'Go to Goal' algorithm discussed in class. Each corner of square is set as a goal for the turtle, whiich it navigates to using a Proportional contoller. The controller parameters have been tuned manually to give the maximum appeareance of the square. [Video](https://github.com/ameyarsalvi/AuE893_AmeyaSalvi_SP21/commit/a03ff4ad451b5042e142cb07d9f8c3c90bd59728)
