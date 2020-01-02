## Sending notes from Python

To finish your program, you need to send note midi values to Sonic Pi from your Python file.

- You'll need to use the OSC library for this part. There are two imports to be added to the top of your file, to allow Python to send messages.

	```python
	from gpiozero import DistanceSensor
	from time import sleep

	from pythonosc import osc_message_builder
	from pythonosc import udp_client

	sensor = DistanceSensor(echo=17, trigger=4)

	while True:
		print(sensor.distance)
		sleep(1)
	```

- Now you need to create a `sender` object that can send the message.

	```python
	from gpiozero import DistanceSensor
	from time import sleep

	from pythonosc import osc_message_builder
	from pythonosc import udp_client

	sensor = DistanceSensor(echo=17, trigger=4)
	sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

	while True:
		print(sensor.distance)
		sleep(1)
	```

- You need to convert the distance into a midi value. These should be integers (whole numbers), and hover around the value **60**, which is middle C. To do this you need to round the distance to an integer, multiply it by 100 and then add a little bit, so that the note is not too low in pitch.

	```python
	from gpiozero import DistanceSensor
	from time import sleep

	from pythonosc import osc_message_builder
	from pythonosc import udp_client

	sensor = DistanceSensor(echo=17, trigger=4)
	sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

	while True:
		pitch = round(sensor.distance * 100 + 30)
		sleep(1)
	```

- To finish off, you need to send the pitch over to Sonic Pi, and reduce the sleep time.

	```python
	from gpiozero import DistanceSensor
	from time import sleep

	from pythonosc import osc_message_builder
	from pythonosc import udp_client

	sensor = DistanceSensor(echo=17, trigger=4)
	sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

	while True:
		pitch = round(sensor.distance * 100 + 30)
		sender.send_message('/play_this', pitch)
		sleep(0.1)
	```

- Save and run your code and see what happens. If all goes well, you've made your very own theremin.

