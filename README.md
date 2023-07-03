# mover_socket_robot_trayectoria
Este programa tiene un ejemplo de mover un robot ur3  por una trayectoria circular mediante socket, se utiliza pythton y no requiere funciones adicionales.
este programa utiliza speedl  de los comandos URscript.


para intalar

        
        # source global ros
        $ source /opt/ros/<your_ros_version>/setup.bash
        
        # create a catkin workspace
        $ mkdir -p catkin_ws/src && cd catkin_ws
        
        # clone the driver
        $ git clone https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git src/Universal_Robots_ROS_Driver
        
        # clone fork of the description. This is currently necessary, until the changes are merged upstream.
        $ git clone -b calibration_devel https://github.com/fmauch/universal_robot.git src/fmauch_universal_robot
        
        # install dependencies
        $ sudo apt update -qq
        $ rosdep update
        $ rosdep install --from-paths src --ignore-src -y
        
        # build the workspace
        $ catkin_make
        
        # activate the workspace (ie: source it)
        $ source devel/setup.bash


para ejecutar

primero mover manualmente el robot hasta que en la pantalla del robot muestre.
                x = -0.12114
                y = -0.21764
                z = 0.40
                rx = deg2rad(2.572)
                ry = deg2rad(0.031)
                rz = deg2rad(-0.105)



t1:

cd catkin_ws;source devel/setup.bash;roslaunch ur3_moveit_config move_group.launch


t2: 
mover_robot5.py




