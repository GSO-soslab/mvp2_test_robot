
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    robot_name = 'mvp2_test_robot'
    robot_bringup = robot_name + '_bringup'

    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
        )
    localization_param_file = os.path.join(robot_param_path, 'localization.yaml') 
    navsat_param_file = os.path.join(robot_param_path, 'navsat.yaml') 

    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            namespace=robot_name,
            output='screen',
            parameters=[localization_param_file],
           ),
        Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform_node',
            namespace=robot_name,
            output='screen',
            parameters=[navsat_param_file],
           ),
])
