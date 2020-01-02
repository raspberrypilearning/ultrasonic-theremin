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
