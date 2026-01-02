#!/bin/bash

PROGRAM_NAME="/u/yichen/public_html/app.py"

# Find the PID of the program
PID=$(pgrep -f $PROGRAM_NAME)

# Check if the PID exists and kill the process
if [ -z "$PID" ]; then
  echo "No process found with the name $PROGRAM_NAME"
else
  kill -9 $PID
  echo "Process $PROGRAM_NAME with PID $PID has been killed"
fi