import math
import os.path
import pickle

LOAD = True

#size of the simulation
frame_end = 20000
#parameters of the path to follow
cir_x = 400
cir_y = 400
#Parameters of the camera
heigth = 2.5
rot_x = 90 * math.pi / 180
rot_y = 0 * math.pi / 180
rot_z = 180 * math.pi / 180	
#parameters of the sea
size = 0.1
spatial_size = 10000
depth = 1000
resolution = 5
choppiness = [0.7, 0.8]
wave_scale = [5,6]
wave_scale_min = 0.01
wind_velocity = [30, 40]
wave_alignment = 7
random_seed = [0, 1, 2, 3, 4, 5]
#for the render
RENDER = True
samples_render = 4 #135
FRAME_INTERVAL = 1
START_FRAME = 1
END_FRAME = 40
resolution_x = 96
resolution_y = 54

if LOAD and os.path.isfile('log.pkl'):
	with open('log.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
		choppiness, wave_scale, wind_velocity, random_seed = pickle.load(f)
