## Detecting distance

You can easily detect how far away an object is from the distance sensor. If you've wired up the sensor as shown in the diagram, then your `echo` pin is **17** and your `trigger` pin is **4**.

--- task ---
Click on **Menu** > **Programming** > **Mu**, to open up a new Python file.
--- /task ---

--- task ---
The code to detect distance is below. Type it into your new file, then save it as `theremin.py` and run it.

--- code ---
---
language: python
filename: theremin.py
line_numbers: true
line_number_start: 
highlight_lines: 
---
from gpiozero import DistanceSensor
from time import sleep

uds = DistanceSensor(trigger=27, echo=17)

while True:
	print(uds.distance)
	sleep(1)
--- /code ---
--- /task ---

The `uds.distance` is the distance in metres between the object and the sensor.

--- task ---
Run your code and move your hand up and down in front of the sensor. You should see the distance changing, as it is printed out in the shell.
--- /task ---




