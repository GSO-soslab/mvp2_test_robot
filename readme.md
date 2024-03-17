# MVP2 Test Robot
## Introduction
This is a mockup AUV for ROS2-MVP framework development.
- Tested environment
    - ROS version: Humble
    - Ubuntu: 22.04
- Directory information
    - `mvp2_test_robot_bringup` 
        - `launch` includes launch files
            - `bringup_simulation.launch.py` is the main launch file to bring up the simulation environment
            - `include` folder include all files called in the main bringup simulation file.
        - `config` includes all ros params *.yaml files which are called in the sub launch file in the `include` folder.
    - `mvp2_test_robot_config` include MVP configuration files. The files are in yaml format and was loaded in mvp code using yaml-cpp.

    - `mvp2_test_robot_description` include urdf files and rviz configuration files.

    ## Installation
    ### Stonefish Simulator
    We use [Stonefish](https://github.com/patrykcieslak/stonefish) Simulator for our system development.
    Our configuration is tested with our forked Stonefish, which may sometimes lack behind the original repository. We will make sure we are up-to-date with the [original repository](https://github.com/patrykcieslak/stonefish).
    #### Installatin
    - Download the stonefish repository
            ```
            git clone https://github.com/GSO-soslab/stonefish
            ```
    - Download dependencies using `sudo apt install`
        - libglm-dev
        - libsdl2-dev
        - libfreetype6-dev
    - Fix a file in SDL2 library
        - `cd /usr/lib/x86_64-linux-gnu/cmake/SDL2/`
        - `sudo nano sdl2-config.cmake`
        - Remove space after "-lSDL2".
        - Save the file.
    - Build the stonefish
        - `cd stonefish`
        - `mkdir build`
        - `cd build`
        - `cmake ..`
        - `make -jx`(where x is the number of threads)
        - `sudo make install`
    - For more information about stonefish please check the original [repository](https://github.com/patrykcieslak/stonefish) and the [documentation](https://stonefish.readthedocs.io/en/latest/).

### Stonefish ROS2 wrapper
Our code is tested with the forked Stonefish ROS2 wrapper. We will make sure we are up-to-date with the original Stonefish ROS2 wrapper.
The original wrapper can be found [here](https://github.com/patrykcieslak/stonefish_ros2)
- Download the forked ROS2 wrapper 
    ```
    git clone https://github.com/GSO-soslab/stonefish_ros2
    ```

### World of stonefish
All the simulator files related to stonefish simulator are included in the `world_of_stonefish` repository. Sepcfically, the repository has stonefish scenario files and drivers that connects stonefish sensor messages into MVP compatible messages.

- Download the repository

```
git clone --single-branch --branch humble-dev https://github.com/GSO-soslab/world_of_stonefish.git
```
- Directory information
    - `data` has all the parts for the simualtor
    - `metadata` contains all stonefish settinsg for looks and materials.
    - `vehicles` contains all stonefish scenario files for vehicles.
    - `world` contains the world scenario files which will call the files in `metadata` and `vehciles`.
    - `include` and `src` have source files for stonefish sensor drivers.

### MVP Framework in ROS2
MVP frame work is our Guidance Navigation and Control framework. 
#### Robot localization
The localization part uses the `robot_localization` package that is available [here](https://github.com/cra-ros-pkg/robot_localization.git)
- Installation
```
sudo apt install ros-humble-robot-localization
```

### MVP2 control
MVP control is the low-level controller we developed. It accepts desired pose and outputs thruster commands to control the vehice pose in a specific frame.
- Installation
```
git clone https://github.com/GSO-soslab/mvp2_control.git
```      

### MVP Message
Our MVP frame uses the MVP messages which has customized ROS message and services for the MVP framework.
- Installation

```
git clone --single-branch --branch humble-devel https://github.com/uri-ocean-robotics/mvp_msgs.git
```

### MVP2 mission
This is the high level guidance system.
We are currently migrating our ROS1 mvp_mission into ROS2 version.
- Installation
```
git clone https://github.com/GSO-soslab/mvp2_mission
```

## Building the workspace
After all the software are downloaded or installed from the previous section you can compile your ROS2 workspace.
- `cd ~/ros2_ws`
- `colcon build`

## Testing the robot with Stonefish
- Launch the simulator
```
ros2 launch mvp2_test_robot_bringup bringup_simulation.launch.py
```
- More information will be available after our MVP2 mission migration.