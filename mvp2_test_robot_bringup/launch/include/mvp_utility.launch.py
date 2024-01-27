import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction


def generate_launch_description():
    robot_name = 'mvp2_test_robot'
    robot_bringup = robot_name + '_bringup'

    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
        )

    mvp_utility_param_file = os.path.join(robot_param_path, 'utility_params.yaml') 

    return LaunchDescription([
        #mvp utility node
        TimerAction(period=1.0,
            actions=[
                    Node(
                        package="mvp_utility",
                        executable="imu_ned_enu_node",
                        namespace=robot_name,
                        name="imu_ned_enu_node",
                        remappings=[
                                ('imu_in/data', 'imu/stonefish/data'),
                                ('imu_out/data', 'imu/data'),
                            ],
                        parameters=[
                            {'frame_id': robot_name + '/imu'},
                            mvp_utility_param_file
                            ]
                    )
            ]),
                    
        Node(
            package="mvp_utility",
            executable="pressure_to_depth_node",
            namespace=robot_name,
            name="pressure_to_depth_node",
            parameters=[
                {'frame_id': robot_name + '/world_ned'}]
        )

])