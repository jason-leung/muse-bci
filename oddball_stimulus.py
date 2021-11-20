from psychopy import visual, core
from pylsl import StreamInfo, StreamOutlet
from random import shuffle, uniform
import time

# Setup LSL stream
stream_info = StreamInfo('MarkerStream', 'Markers', 1, 0, 'string', 'VisualP300Marker')
stream_outlet = StreamOutlet(stream_info)
print("LSL Outlet Stream Initialized")

# create a window
mywin = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, monitor='testMonitor',
    color=[108/255*2-1,108/255*2-1,108/255*2-1], colorSpace='rgb',
    blendMode='avg', units='pix')
fps = 60

# create visual stimuli
fixation = visual.ShapeStim(win=mywin, vertices=[[-1,0], [0,0], [0,1], [0,0], [1,0], [0,0], [0,-1],[0,0]], size=80, lineWidth=5, pos=[0,0])
circle_b = visual.Circle(win=mywin, radius=100, units='pix', pos=[0,0], fillColor=[-1,-1,1])
circle_g = visual.Circle(win=mywin, radius=100, units='pix', pos=[0,0], fillColor=[-1,1,-1])

# experimental setup
num_blocks = 3
num_trials = 40
oddball_chance = 0.25
fixation_duration = [0.3, 0.5]
stimulus_duration = [0.8, 1.2]
trials = [int(i < round(num_trials*oddball_chance)) for i in range(num_trials)]

# start experiment
for b in range(num_blocks):
	shuffle(trials)
	# short pause at beginning of block
	for frameNum in range(5 * fps):
		mywin.flip()
	for t in range(num_trials):
		# fixation
		stream_outlet.push_sample(['fixation'], timestamp=time.time())
		for frameNum in range(round(uniform(fixation_duration[0], fixation_duration[1]) * fps)):
			fixation.draw()
			mywin.flip()

		# stimulus
		for frameNum in range(round(uniform(stimulus_duration[0], stimulus_duration[1]) * fps)):
			if trials[t] == 1:
				circle_b.draw()
				if frameNum == 0:
					stream_outlet.push_sample(['oddball'], timestamp=time.time())
			else:
				circle_g.draw()
				if frameNum == 0:
					stream_outlet.push_sample(['control'], timestamp=time.time())
			mywin.flip()

mywin.close()
core.quit()