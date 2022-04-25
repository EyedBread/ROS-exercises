# ROS-exercises

To run exercise 1, firstly:
```
cd exercise1/

catkin build
```
Now you want to open up 3 terminal windows in the exc1/ directory, in each one do: 
```
source devel/setup.bash
```
 in the first one you want to run:
```
roscore
```
and in the second one you want to:
```
cd src/exc1/package1/scripts
chmod +x publisher.py
rosrun package1 publisher.py
```
and in the third one you want to:
```
cd src/exc1/package2/scripts
chmod +x receiver.py
rosrun package2 receiver.py
```

Now you can do ```rostopic list``` in a fourth window to see the active topics, and ```rostopic echo /topicname``` to se topicnames output, specifically the /angelic and /kthfs/result topics.


To run exercise 2:

first install python matplotlib:
```
pip install matplotlib
```
```
cd exercise2/

catkin build
```
and now do the same procedure as last time, open up three terminals, source setup.bash in each one(you actually don't need to in the window that runs roscore but for simplicity sake), run roscore in first terminal, run the exercise2/src/publisherPlot/publisher.py file using rosrun in the second terminal, and run the exercise2/src/receiverPlot/plotting.py file using rosrun in the third terminal. Don't forget to make the .py files executable using chmod +x fileName.py