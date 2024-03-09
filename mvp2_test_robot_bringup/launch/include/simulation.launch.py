import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    robot_name = 'mvp2_test_robot'
    robot_bringup = robot_name + '_bringup'
    
    sim_world = 'test.scn'

    world_of_stonefish_dir = get_package_share_directory('world_of_stonefish')

    simulation_data = os.path.join(world_of_stonefish_dir, 'data/')
    scenario_desc = os.path.join(world_of_stonefish_dir, 'world', sim_world)
    simulation_rate = "100"
    window_res_x = "1600"
    window_res_y = "800"
    rendering_quality ="high"

    return LaunchDescription([
        # simulation node
        Node(
            package="stonefish_ros2",
            executable="stonefish_simulator",
            name="stonefish_simulator",
            output="screen",
            arguments=[simulation_data, scenario_desc, simulation_rate, window_res_x, window_res_y, rendering_quality]
        )

])