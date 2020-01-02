## Mapping distances to midi notes

You want the distance your hand is from the ultrasonic sensor to alter the midi note that is being played.

The distance sensor produces values between `0` and `1`, where as the buzzer can play midi notes between `33` and `105`.

--- task ---
Create a new function in your code, to convert distances to midi values. It will need a parameter for the sensor's distance.

--- code ---
---
language: python
filename: theremin.py
line_numbers: true
line_number_start: 
highlight_lines: 9
---
from gpiozero import DistanceSensor, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

uds = DistanceSensor(trigger=27, echo=17)
buzzer = TonalBuzzer(21, octaves=3)


def distance_to_tone(distance_value):


while True:
	print(sensor.distance)
	buzzer.play(Tone(midi=69))
	sleep(1)
--- /code ---
--- /task ---

--- task ---
You need to calculate the range of tones that can be played. The `buzzer` object can tell you it's minimum tone and maximum tone, and then you can subtract one from the other to get the value of the range.

--- code ---
---
language: python
filename: theremin.py
line_numbers: true
line_number_start: 
highlight_lines: 10, 11, 12
---
from gpiozero import DistanceSensor, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

uds = DistanceSensor(trigger=27, echo=17)
buzzer = TonalBuzzer(21, octaves=3)


def distance_to_tone(distance_value):
    min_tone = buzzer.min_tone.midi
    max_tone = buzzer.max_tone.midi
    tone_range = max_tone - min_tone
	

while True:
	print(sensor.distance)
	buzzer.play(Tone(midi=69))
	sleep(1)
--- /code ---
--- /task ---

--- task ---
Now you can return the `tone_range` multiplied by the `distance_value`, added to the `min_tone`, to get the value of the midi note to be played. As this will be a floating point number, it needs to be convered to an integer, as well.

--- code ---
---
language: python
filename: theremin.py
line_numbers: true
line_number_start: 
highlight_lines: 13
---
from gpiozero import DistanceSensor, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

uds = DistanceSensor(trigger=27, echo=17)
buzzer = TonalBuzzer(21, octaves=3)


def distance_to_tone(distance_value):
    min_tone = buzzer.min_tone.midi
    max_tone = buzzer.max_tone.midi
    tone_range = max_tone - min_tone
    return min_tone + int(tone_range * distance_value)	

while True:
	print(sensor.distance)
	buzzer.play(Tone(midi=69))
	sleep(1)
--- /code ---
--- /task ---
--- /task ---

--- task ---
Now that you can find the value of the midi note, you can make your buzzer play the note.

--- code ---
---
language: python
filename: theremin.py
line_numbers: 
line_number_start: 
highlight_lines: 17,18,19,20
---
from gpiozero import DistanceSensor, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

uds = DistanceSensor(trigger=27, echo=17)
buzzer = TonalBuzzer(21, octaves=3)


def distance_to_tone(distance_value):
    min_tone = buzzer.min_tone.midi
    max_tone = buzzer.max_tone.midi
    tone_range = max_tone - min_tone
    return min_tone + int(tone_range * distance_value)


while True:
    distance_value = uds.distance
    tone = distance_to_tone(distance_value)
    buzzer.play(Tone(midi=tone))
    sleep(0.01)

--- /code ---
--- /task ---

--- task ---
Run your file, and then move your hand over the sensor to hear your theremin play.
--- /task ---
