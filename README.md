# ROS_NovintFalcon
---Controlling a ROS-enabled Robot using Novint Falcon Haptic Device ---

A. Two wheeled Robot:

1. Launching the Two Wheeled Robot
   
   $ roslaunch ros_robotics diff_wheeled_gazebo_full.launch
   
   *** ● Files required:
     ❏ diff_wheeled_gazebo_full.launch
     ❏ diff_wheeled_robot_with_sensor.xacro
     ❏ wheel.urdf .xacro                 ***
     
2. Run the python joystick node.
   
      ● Files required: ❏ joy2cmd_vel_diff.py
      
   $ cd ~/catkin_ws_ars
   $ catkin_make
   $ source devel/setup.bash
   $ roscd ros_falcon/nodes
   $ python joy2cmd_vel_diff.py
  
 3. Run ros_falcon joystick.
    
    ● Files required: ros_falcon
    
   $ catkin_make
   $ source devel/setup.bash

   $ roscd ros_falcon/
   $ sudo cp udev_rules/99-udev-novint.rules /etc/udev/rules.d
     // unplug & replug the falcon //
   $ sudo ldconfig
   
   $ rosrun ros_falcon joystick
   
------------------------------------------------------------------------------------------------------------------------------   

B. Controlling Floating box model using Novint falcon haptic device:

#---------Steps to control the floating box using Novint falcon------#

1. Creating Floating box (box without any force acting on it)

   $ roslaunch ros_robotics box_gazebo.launch

        ●Files required:
                        ❏ box_gazebo.launch
                        ❏ floating_box_11.gazebo
                        
2. Run the python joystick node.

         Files required:
                        joy2cmd_vel_box.py
                        
   $ catkin_make
   $ source devel/setup.bash
   $ roscd ros_falcon/nodes
   $ python joy2cmd_vel_box.py
   
3. Run ros_falcon joystick.

   $ catkin_make
   $ source devel/setup.bash
   
   $ roscd ros_falcon/
   $ sudo cp udev_rules/99-udev-novint.rules /etc/udev/rules.d
      // unplug & replug the falcon //
   $ sudo ldconfig
   
   $ rosrun ros_falcon joystick
   
   ---------------------------------------------------------------------------------------------------------------------
