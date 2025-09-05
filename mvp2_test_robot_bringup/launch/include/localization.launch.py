
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

    mag_model_path = os.path.join(get_package_share_directory('mvp_localization_utilities'),
        'config/magnetic/'
        )
    
    localization_param_file = os.path.join(robot_param_path, 'localization.yaml') 


    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            namespace=robot_name,
            # output='screen',
            parameters=[localization_param_file],
           ),

        Node(
            package='mvp_localization_utilities',
            executable='world_odom_transform_node',
            name='world_odom_transform_node',
            namespace=robot_name,
            output='screen',
            prefix=['stdbuf -o L'],
            parameters=[
                {'tf_prefix': robot_name},
                {'mag_model_path': mag_model_path},
                localization_param_file
                ],
            remappings=[
                    ('odometry', 'odometry/filtered'),
                ],
           ),

        Node(
            package='mvp_localization_utilities',
            executable='gps_world_odom_publisher',
            name='gps_world_odom_publisher',
            namespace=robot_name,
            output='screen',
            prefix=['stdbuf -o L'],
            parameters=[
                {'tf_prefix': robot_name},
                {'gps_frame': 'gps2'},
                {'acceptable_var': 10.0}, 
                {'manual_position_covariance': 0.0}    
                ],
            remappings=[
                    ('gps/world_odometry', 'gps2/odometry'),
                    ('gps/fix', 'gps2/fix'),
                ],
           ),
])
