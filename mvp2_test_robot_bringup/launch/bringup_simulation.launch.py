import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time

from launch_xml.launch_description_sources import XMLLaunchDescriptionSource



def generate_launch_description():
    arg_robot_name = 'mvp2_test_robot'
    robot_bringup = arg_robot_name + '_bringup'

    # simulation
    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','simulation.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )

    # robot localization
    localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','localization.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )
    
    #description URDF
    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','description.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )


    #mvp_control
    mvp_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_control.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    #mvp_mission
    mvp_mission = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_mission.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    #joy
    joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','joy.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    usbl_test = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','usbl.launch.py')]),
        launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    foxglove = IncludeLaunchDescription(
        XMLLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('foxglove_bridge'),
                'launch/foxglove_bridge_launch.xml')),
        launch_arguments={
            'namespace': arg_robot_name
        }.items()
    )



    return LaunchDescription([
        simulation,
        localization,
        description,
        # mvp_control,
        # mvp_mission,
        foxglove
        # usbl_test
        # joy
    ])
