## Getting Sonic Pi ready

Sonic Pi is going to receive messages from your Python script. This will tell Sonic Pi which note to play.

- Open Sonic Pi by clicking on **Menu** > **Programming** > **Sonic Pi**
- In the buffer that is open, you can begin by writing a `live_loop`. This is a loop that will run forever, but can easily be updated, allowing you to experiment with different sounds. You can also add a line to reduce the time it takes for Sonic Pi and Python to talk to each other.

	```ruby
	live_loop :listen do
		set_sched_ahead_time! 0.1
	end
	```

- Next you can sync the live loop with the messages that will be coming from Python.

	```ruby
	live_loop :listen do
		message = sync "/play_this"
	end
	```

- The message that comes in will be a dictionary, containing the key `:args`. The value of this key will be a list, where the first item is the midi value of the note to be played.

	```ruby
	live_loop :listen do
		message = sync "/play_this"
		note = message[:args][0]
	end
	```

- Lastly, you need to play the note.

```ruby
live_loop :listen do
    message = sync "/play_this"
	note = message[:args][0]
	play note
end
```

- You can set this live loop to play straight away, by clicking on the **Run** button. You won't hear anything yet, as the loop is not receiving any messages.

