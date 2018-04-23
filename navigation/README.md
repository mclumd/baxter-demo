# Navigation Demo

This demo will allow you to control Baxter's mobility base using a command line interface

## Getting Started

1. Power on Baxter
2. Close the circuit breaker labeled "Main Breaker" on the back of the mobility base (it's a red lever -- close by rotating it up)
3. Press the power button on the mobility base (located to the left of the status indicator light)
4. First, ensure that the computer you're using is connected to the `mcl-umd` network (either thru Ethernet or Wi-Fi)
5. Open a terminal and SSH into the mobility base (the password is 'password'):

```ssh mb@NUC.local```

6. Repeat step 5 for two additional terminals -- you will need all of them
7. In one terminal, issue the following command:

```roslaunch mobility_base_bringup mobility_base.launch```

8. In the second terminal, suppress the wireless command messages so you can control the base via your computer:

```rostopic pub -r 10 /mobility_base/suppress_wireless std_msgs/Empty```

9. In the third terminal, run:

```bash mobility_base_config.bash```

10. Open another terminal on your computer, but don't ssh into the base.
We will use secure copy to transfer a copy of the navigation script from this repository to the mobility base.
If you're in the root folder of this repository, the command is as follows:

```scp navigation/navigation.py mb@NUC.local:~/```

This will copy navigation.py to the home directory on the mobility base machine
NOTE: If you make changes to the navigation.py script, re-issue this command to try out your working copy
10. Finally--and again using the third terminal--run the demo script:

```python navigation.py```

## Running the Demo
This script presents you with a command line interface for controlling Baxter's movement. Currently you can issue the following commands:

```
- forward   // move forward
- backward  // move backward
- left      // turn/rotate left
- right     // turn/rotate right
- stop      // stop any movement
- exit      // exit program
```

Any other command input will be interpreted as a `stop` command.

Each command will be executed until: (1) you issue another movement command, (2) you issue a stop or exit command,
(3) you kill the program using Ctrl-C

## TODO
- Add more commands
- Add sensor detection to automatically stop when w/in some distance threshold of obstacles
