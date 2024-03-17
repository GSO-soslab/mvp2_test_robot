# MVP2 Test Rotbo
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
    Our configuration is tested with our forked Stonefish, which may sometimes lack behind the original repository. We will make sure we are up-to-date with the original repository.
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

### World of stonefish
All the simulator files related to stonefish simulator are included in the `world_of_stonefish` repository. Sepcfically, the repository has stonefish scenario files and drivers that connects stonefish sensor messages into MVP compatible messages.
#### Installation
    - Download the repository

```
git clone --single-branch --branch humble-dev https://github.com/GSO-soslab/world_of_stonefish.git
```
    - D


      
        
    
    