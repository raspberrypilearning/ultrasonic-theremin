## Getting Sonic Pi ready

Sonic Pi is going to receive messages from your Python script. This will tell Sonic Pi which note to play.

- Open Sonic Pi by clicking on **Menu** > **Programming** > **Sonic Pi**
- In the buffer that is open, you can begin by writing a `live_loop`. This is a loop that will run forever, but can easily be updated, allowing you to experiment with different sounds. You can also add a line to reduce the time it takes for Sonic Pi and Python to talk to each other.

	```ruby
	live_loop :listen do
	    use_real_time
	end
	```

- Next you can sync the live loop with the messages that will be coming from Python.

	```ruby
	live_loop :listen do
	    use_real_time
	    note = sync "/osc/play_this"
	end
	```

- The message that comes in will be a list, with the note being the 0th item.

	```ruby
	live_loop :listen do
	    use_real_time
	    note = sync "/osc/play_this"
	    play note[0]
	end
	```

- You can set this live loop to play straight away, by clicking on the **Run** button. You won't hear anything yet, as the loop is not receiving any messages.

