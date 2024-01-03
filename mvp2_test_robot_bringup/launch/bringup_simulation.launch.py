import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    robot_name = 'mvp2_test_robot'
    robot_bringup = robot_name + '_bringup'
    sim_world = 'test.scn'


    world_of_stonefish_dir = get_package_share_directory('world_of_stonefish')

    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
        )
    sim_param_file = os.path.join(robot_param_path, 'sim_params.yaml') 

    mvp_utility_file = os.path.join(robot_param_path, 'utility_params.yaml') 

    return LaunchDescription([
        # Node(
        #     package="stonefish_mvp2",
        #     executable="stonefish_simulator",
        #     name="stonefish_simulator",
        #     output="screen",
        #     parameters= [
        #         {'data_path': os.path.join(world_of_stonefish_dir, 'data/')},
        #         {'scenario_path': os.path.join(world_of_stonefish_dir, 'world', sim_world) },
        #         sim_param_file
        #     ],
        # ),

        Node(
            package="mvp_utility",
            executable="imu_ned_enu_node",
            namespace=robot_name,
            name="imu_ned_enu_node",
            remappings=[
                    ('imu_in/data', 'imu/stonefish/data'),
                    ('imu_out/data', 'imu/data'),
            ],
            parameters=[mvp_utility_file]
        )

])