import numpy as np
import cv2
import os, sys
import traceback
import time 
try:
	import sim
	
except Exception:
	print('\n[ERROR] It seems the sim.py OR simConst.py files are not found!')
	print('\n[WARNING] Make sure to have following files in the directory:')
	print('sim.py, simConst.py and appropriate library - remoteApi.dll (if on Windows), remoteApi.so (if on Linux) or remoteApi.dylib (if on Mac).\n')
	sys.exit()


# Global variable "client_id" for storing ID of starting the CoppeliaSim Remote connection
# NOTE: DO NOT change the value of this "client_id" variable here
client_id = -1



def init_remote_api_server():

    global client_id
    sim.simxFinish(-1) # just in case, close all opened connections
    client_id=sim.simxStart('127.0.0.1',19997,True,True,5000,5) 
    return client_id

def start_simulation():

    global client_id
    return_code=0
    return_code = sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot_wait)
    print("simstarted",return_code)
    return return_code

def stop_simulation():
    global client_id
    return_code = 0
    return_code = sim.simxStopSimulation(client_id,sim. simx_opmode_oneshot_wait)
    print("simstopped",return_code)
    return return_code

def get_vision_sensor_image():
    global client_id
    vision_sensor_image = []
    image_resolution = []
    return_code = 0
   
    return_code,v0=sim.simxGetObjectHandle(client_id,'vision_sensor_1',sim.simx_opmode_oneshot_wait) 
    return_code, image_resolution,image = sim.simxGetVisionSensorImage(client_id, v0, 0, sim.simx_opmode_oneshot_wait)
    vision_sensor_image = np.array(image,dtype = np.uint8)
    vision_sensor_image.resize([image_resolution[0],image_resolution[1],3])
    print(vision_sensor_image)
    cv2.imshow('transformed image',vision_sensor_image)
    return vision_sensor_image, image_resolution, return_code


if __name__ == "__main__":
    client_id = init_remote_api_server()
    print (client_id)
    return_code=start_simulation()
    print(return_code)
    time.sleep(1)
    get_vision_sensor_image()
    stop_simulation()