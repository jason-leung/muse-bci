from psychopy import visual, core
from pylsl import StreamInfo, StreamOutlet
from random import shuffle, uniform

# Setup LSL stream
stream_info = StreamInfo('MarkerStream', 'Markers', 1, 0, 'string', 'VisualP300Marker')
stream_outlet = StreamOutlet(stream_info)
print("LSL Outlet Stream Initialized")

# create a window
mywin = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, monitor='testMonitor',
    color=[108/255*2-1,108/255*2-1,108/255*2-1], colorSpace='rgb',
    blendMode='avg', units='pix')
fps = 60

# create visual stimuli
fixation = visual.ShapeStim(win=mywin, vertices=[[-1,0], [0,0], [0,1], [0,0], [1,0], [0,0], [0,-1],[0,0]], size=80, lineWidth=5, pos=[0,0])
circle_b = visual.Circle(win=mywin, radius=100, units='pix', pos=[0,0], fillColor=[-1,-1,1])
circle_g = visual.Circle(win=mywin, radius=100, units='pix', pos=[0,0], fillColor=[-1,1,-1])

# experimental setup
num_blocks = 1
num_trials = 10
# num_blocks = 3
# num_trials = 40
oddball_chance = 0.25
fixation_duration = [0.3, 0.5]
stimulus_duration = [0.8, 1.2]

trials = [int(i < round(num_trials*oddball_chance)) for i in range(num_trials)]

# short pause at start
core.wait(5.0)

# start experiment
for b in range(num_blocks):
	shuffle(trials)
	for t in range(num_trials):
		# fixation
		stream_outlet.push_sample(['fixation'])
		for frameNum in range(round(uniform(fixation_duration[0], fixation_duration[1]) * 60)):
			fixation.draw()
			mywin.flip()

		# stimulus
		for frameNum in range(round(uniform(stimulus_duration[0], stimulus_duration[1]) * 60)):
			if trials[t] == 1:
				circle_b.draw()
				if frameNum == 0:
					stream_outlet.push_sample(['oddball'])
			else:
				circle_g.draw()
				if frameNum == 0:
					stream_outlet.push_sample(['control'])
			mywin.flip()

mywin.close()
core.quit()