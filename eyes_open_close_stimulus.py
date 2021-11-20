from psychopy import visual, core
from psychopy import sound
from pylsl import StreamInfo, StreamOutlet

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
tone = sound.Sound(value=1000,secs=0.02)

# experimental setup
num_trials = 16
trial_duration = 120 # seconds
trials = [1-i%2 for i in range(num_trials)]

# start experiment
for frameNum in range(5 * fps):
	mywin.flip()
for t in range(num_trials):
	nextFlip = mywin.getFutureFlipTime(clock='ptb')
	for frameNum in range(trial_duration * fps):
		if trials[t] == 1:
			fixation.draw()
		if frameNum == 0:
			tone.stop()
			tone.play(when=nextFlip)
			if trials[t] == 1:
				stream_outlet.push_sample(['eyes_open'])
			else:
				stream_outlet.push_sample(['eyes_closed'])
		mywin.flip()

mywin.close();
core.quit();
