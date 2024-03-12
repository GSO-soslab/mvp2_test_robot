import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction


def generate_launch_description():
    robot_name = 'mvp2_test_robot'
    robot_bringup = robot_name + '_bringup'

    return LaunchDescription([
                    
        Node(
            package="mvp_utility",
            executable="pressure_to_depth_node",
            namespace=robot_name,
            name="pressure_to_depth_node",
            parameters=[
                {'frame_id': robot_name + '/world_ned'}]
        )

])