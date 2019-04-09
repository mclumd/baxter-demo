#!/usr/bin/env python
import sys
import os
import signal

cmd = 'blah'

while cmd != 'exit':
      cmd = sys.stdin.readline().strip()
      if cmd: print(cmd)

print('\n*** Exiting ***\n')
