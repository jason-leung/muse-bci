# Muse BCI

In this project, I used the Muse S headband to detect useful signals for a brain-computer interface (BCI) system. Specifically, I used [BlueMuse](https://github.com/kowalej/BlueMuse) to stream the Muse data to LSL. From here, [LabRecorder](https://github.com/labstreaminglayer/App-LabRecorder) is used to save the LSL stream data into XDF format for offline analysis.

## Detecting P300 Event
In this experiment, we detected the P300 ERP from a visual oddball stimulus. This experimental setup and data analysis is based on [this paper](http://dx.doi.org/10.1007/978-3-319-58628-1_5) by Krigolson et. al. The data used for this experiment can be found [here](Data), and the stimulus program is found [here](oddball_stimulus.py). The data analysis script is available [here](muse-oddball-erp.ipynb).

