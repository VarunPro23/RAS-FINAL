import numpy as np

WORKING_DIR = "."

block_height = -45

default_port="/dev/ttyACM0"

#  3x3 affine matrix for pixel -> robot (X,Y)

M = np.array([
     [ 3.22215816e-03, -4.71279715e-01,  4.18469351e+02],
     [-4.69432195e-01, -7.51873791e-03,  1.48748933e+02]
], dtype=np.float64)
                 
z_above = 100           # safe travel height (e.g. 100)
z_table = -46           # Z at table contact
block_height_mm = 7   # block physical thickness
block_length_mm = 20   # block physical length
stack_delta_mm = 10    # extra height when stacking (to avoid collision)
side_offset_mm = 10    # extra XY gap when placing beside

capture_wait_time = 5
camera_index = '/dev/video2'