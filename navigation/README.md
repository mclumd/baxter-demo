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
2. There is a power cord that plugs into Baxter directly above his rear-right leg (the other end is likely connected into a power strip on the ground). Instead, plug this other end into one of the white outlets on Baxter's back.
3. On the back of the mobility base, there is a connection labeled "Charging Port", which keeps the battery charged when not in use.  Disconnect these wires.
4. Disconnect the kinect camera cable if applicable
5. The only wires (potentially) that should still connect Baxter to anything not affixed to Baxter should be two Ethernet cables -- one for Baxter and one for the mobility base.  Ensure these wires have plenty of slack and are not in position to be run over.

## Getting Started

1. Close the circuit breaker labeled "Main Breaker" on the back of the mobility base (it's an angled, red plastic lever). Close by rotating it upwards until it snaps into place/is no longer visible
2. Press the power button on the back of the mobility base (located to the left of the status indicator light)
3. Press the power button on the Samlex-Power DC-AC Inverter (located on Baxter's back)
4. Power on Baxter (button is located directly above Baxter's rear-left leg)
5. Ensure that the computer you're using is connected to the `mcl_avw` network (either thru Ethernet or Wi-Fi)
NOTE: If using WiFi, this network is hidden, so you'll have to search for it manually
6. Open a terminal and SSH into the mobility base (the password is 'password'):

```ssh mb@NUC.local```

7. Repeat step 6 in two additional terminals -- you will need all of them
8. In the first terminal, issue the following command to bring up the base:

```roslaunch mobility_base_bringup mobility_base.launch```

9. In the second terminal, suppress the wireless command messages so you can control the base via your computer:

```rostopic pub -r 10 /mobility_base/suppress_wireless std_msgs/Empty```

10. In the third terminal, run the configuration script:

```bash mobility_base_config.bash```

11. Open another terminal on your computer, but don't ssh into the base.
We will use secure copy to copy the navigation script from your repository to the mobility base (assuming your repo is up-to-date, this ensures you will always be using the most recent version of the script).
If you're in the root folder of your repository, the command is as follows:

```scp navigation/navigation.py mb@NUC.local:~/```

Again, the password is 'password'. This will copy `navigation.py` to the home directory on the mobility base host
NOTE: If you make changes to the navigation.py script, re-issue this command to try out your working copy

12. Finally--using the third SSH terminal--run the demo script:

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

## Tear Down
When complete, accomplish the following steps to tear down your setup:

1. Turn off Baxter (button is located directly above Baxter's rear-left leg)
2. Once Baxter's head lights have extinguished, turn off the Samlex-Power DC-AC Inverter (located on Baxter's back)
3. Remove Baxter's power plug from the outlet on his back and plug back into a power strip on the ground
4. Turn off the mobility base by pressing the power button on the back (located to the left of the status indicator light)
5. Open the circuit breaker labeled "Main Breaker" on the back of the mobility base by pressing the red button (this should release the red plastic lever you used to close the breaker during set up)
6. Reconnect the wires into the "Charging Port" on the back of the mobility base

## TODO
- Clean up navigation.py
- Add more commands
- Add configurable speeds
- Add sensor detection to automatically stop when w/in some distance threshold of obstacles
- Possibly refactor some of the setup into a script

