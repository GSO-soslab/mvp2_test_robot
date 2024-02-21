import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction


def generate_launch_description():
    robot_name = 'mvp2_test_robot'
    robot_bringup = robot_name + '_bringup'
    robot_config = robot_name + '_config'
    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
        )
    
    robot_config_path = os.path.join(
        get_package_share_directory(robot_config)
    )
    mvp_mission_config_file = os.path.join(robot_config_path, 'mvp_mission_config', 'helm.yaml') 
    mvp_mission_param_file = os.path.join(robot_param_path, 'mvp_mission.yaml') 

    return LaunchDescription([

        TimerAction(period=0.0,
            actions=[
                    Node(
                        package="mvp_helm",
                        executable="mvp2_helm_node",
                        namespace=robot_name,
                        name="mvp2_helm_node",
                        prefix=['stdbuf -o L'],
                        output="screen",
                        parameters=[
                            {'helm_config_file': mvp_mission_config_file},
                            {'tf_prefix': robot_name},
                            mvp_mission_param_file
                            ]
                        )
            ])
        
])