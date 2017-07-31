## Detecting distance

Thanks to the abstractions in the GPIO Zero module, you can very easily detect how far away an object is from the distance sensor. If you've wired up the sensor as shown in the diagram, then your echo pin is **17** and your trigger pin is **4**.

- Click on **Menu** > **Programming** > **Python 3 (IDLE)**, to open up a new Python shell.
- In the shell, click on **New** > **New File** to create a new Python file.
- The code to detect distance is below. Type it into your new file, then save and run it.

	```python
	from gpiozero import DistanceSensor
	from time import sleep

	sensor = DistanceSensor(echo=17, trigger=4)

	while True:
		print(sensor.distance)
		sleep(1)
	```

The `sensor.distance` is the distance in meters between the object and the sensor. Run your code and move your hand backwards and forwards in front of the sensor. You should see the distance changing, as it is printed out in the shell.

