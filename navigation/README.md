# Navigation Demo

This demo will allow you to control Baxter's mobility base using a command line interface

## Clone this repository
Navigate to a suitable location on your computer and issue the following commands:

```
git clone git@github.com:mclumd/baxter-demo.git
cd baxter-demo
```

## Before Getting Started
1. Ensure Baxter and the mobility base are turned off
2. There is a power cord that connects to Baxter directly above his rear-right leg (the other end is likely connected into a power strip on the ground). Instead, plug this other end into one of the white outlets on Baxter's back.
3. On the back of the mobility base, there is a connection labeled "Charging Port", which keeps the battery charged when not in use.  Disconnect these wires.
4. Disconnect the kinect camera cable if applicable
5. The only wires (potentially) that should connect Baxter to anything not affixed to Baxter should be two Ethernet cables -- one for Baxter and one for the mobility base.  Ensure these wires have plenty of slack and are not in position to be run over.

## Getting Started

1. Close the circuit breaker labeled "Main Breaker" on the back of the mobility base (it's a red lever -- close by rotating it up until it's no longer visible)
2. Press the power button on the mobility base (located to the left of the status indicator light)
3. Press the power button on the Samlex-Power DC-AC Inverter (located on Baxter's back)
4. Power on Baxter (button is located directly above Baxter's rear-left leg)
5. Ensure that the computer you're using is connected to the `mcl_avw` network (either thru Ethernet or Wi-Fi)
NOTE: If using WiFi, this network is hidden, so you'll have to search for it manually
6. Open a terminal and SSH into the mobility base (the password is 'password'):

```ssh mb@NUC.local```

7. Repeat step 6 for two additional terminals -- you will need all of them
8. In one terminal, issue the following command:

```roslaunch mobility_base_bringup mobility_base.launch```

9. In the second terminal, suppress the wireless command messages so you can control the base via your computer:

```rostopic pub -r 10 /mobility_base/suppress_wireless std_msgs/Empty```

10. In the third terminal, run:

```bash mobility_base_config.bash```

11. Open another terminal on your computer, but don't ssh into the base.
We will use secure copy to transfer a copy of the navigation script from this repository to the mobility base.
If you're in the root folder of this repository, the command is as follows:

```scp navigation/navigation.py mb@NUC.local:~/```

Again, the password is 'password'. This will copy `navigation.py` to the home directory on the mobility base machine
NOTE: If you make changes to the navigation.py script, re-issue this command to try out your working copy
12. Finally--and again using the third terminal--run the demo script:

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
*IMPORTANT* If Baxter becomes uncontrollable at any point in time, press the `EMERGENCY STOP` button on his back (right-hand side)

Each command will be executed until: (1) you issue another movement command, (2) you issue a stop or exit command,
(3) you kill the program using Ctrl-C

## TODO
- Add tear down instructions
- Add more commands
- Add sensor detection to automatically stop when w/in some distance threshold of obstacles
