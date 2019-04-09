# Navigation Demo

This demo will allow you to control Baxter's mobility base using a command line interface or voice commands via Pocketsphinx Speech-to-Text software.

## Clone this repository
Navigate to a suitable location on your computer and issue the following commands:

```
git clone git@github.com:mclumd/baxter-demo.git
cd baxter-demo
```

## Before Getting Started
1. Ensure Baxter and the mobility base are turned off
2. (Bob only) There is a power cord that plugs into Baxter directly above his rear-right leg (the other end is likely connected into a power strip on the ground). Instead, plug this other end into one of the white outlets on Baxter's back.
3. On the back of the mobility base, there is a connection labeled "Charging Port", which keeps the battery charged when not in use.  Disconnect these wires.
4. Disconnect the kinect camera cable if applicable
5. The only wires (potentially) that might still connect Baxter to anything not affixed to Baxter would be one or two Ethernet cables -- one for Baxter and one for the mobility base.  Ensure these wires have plenty of slack and are not in position to be run over.

    NOTE:  Alice's mobility base is currently set up to automatically connect to the `mcl_avw` Wi-Fi -- no Ethernet cable required

## Getting Started

1. Close the circuit breaker labeled "Main Breaker" on the back of the mobility base (it's an angled, red plastic lever). Close by rotating it upwards until it snaps into place/is no longer visible
2. Press the power button on the back of the mobility base (located to the left of the status indicator light)
3. (Bob only) Press the power button on the Samlex-Power DC-AC Inverter (located on Baxter's back)
4. (Bob only) Power on Baxter (button is located directly above Baxter's rear-left leg)
5. Ensure that the computer you're using is connected to the `mcl_avw` network (either thru Ethernet or Wi-Fi)

    NOTE: If using WiFi, this network is hidden, so you'll have to search for it manually
6. Secure copy the required scripts to the mobility base (assuming your repo is up-to-date, this ensures you will always be using the most recent versions):

```bash
cd navigation
scp navigation.py mb@NUC.local:~/  # password is 'password'
```
NOTE: If you make changes to navigation.py, re-issue this command to try out your working copy

7. Open a terminal and SSH into the mobility base:

```bash
ssh mb@NUC.local  # password is 'password'
```

8. Repeat step 7 in two additional terminals -- you will need all of them
9. In the first terminal, issue the following command to bring up the base:

```bash
roslaunch mobility_base_bringup mobility_base.launch  # Alice might have lots of errors/warnings, disregard
```

10. In the second terminal, suppress the wireless command messages so you can control the base via your computer:

```bash
rostopic pub -r 10 /mobility_base/suppress_wireless std_msgs/Empty
```

11. In the third terminal, run the configuration script and the navigation script:

```bash
bash mobility_base_config.bash
python navigation.py
```

12. Run the demo from your local machine:

```bash
./start.sh

OR, to use voice-activated commands...

./start.sh voice-control
```
NOTE: If using voice-control, you must have Pocketsphinx installed. See [instructions for using Pocketsphinx](pocketsphinx-instructions.md)

## Commands
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
