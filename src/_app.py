from multitracker import TrackerType
import json
import cv2
import sys
import os
import time
import logging
from sys import stdout


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    logger.info('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()




# # Config
# data_path = 'data-io/'
# input_path = data_path + 'input/input.mkv'
# output_path = data_path + 'output/output.mkv'
# initial_conditions_file = data_path + 'input/initial_conditions.json'
# tracker_type = TrackerType.CSRT

# def create_tracker(tracker_type):
#     if tracker_type.name == 'BOOSTING':
#         return cv2.TrackerBoosting_create()
#     if tracker_type.name == 'MIL':
#         return cv2.TrackerMIL_create()
#     if tracker_type.name == 'KCF':
#         return cv2.TrackerKCF_create()
#     if tracker_type.name == 'TLD':
#         return cv2.TrackerTLD_create()
#     if tracker_type.name == 'MEDIANFLOW':
#         return cv2.TrackerMedianFlow_create()
#     if tracker_type.name == 'GOTURN':
#         return cv2.TrackerGOTURN_create()
#     if tracker_type.name == 'MOSSE':
#         return cv2.TrackerMOSSE_create()
#     if tracker_type.name == "CSRT":
#         return cv2.TrackerCSRT_create()

# class TrackerWrapper:
#     def __init__(self, initial_boundig_box, tracker) -> None:
#         self.name = initial_boundig_box
#         self.tracker = tracker

# def create_and_init_tracker(ref_frame, bbox, name):
#     tracker = create_tracker(tracker_type)
#     tracker.init(ref_frame, bbox)
#     return TrackerWrapper(name, tracker)

def get_tracking():
    # 
    trackers = []
    # Read video
    video = cv2.VideoCapture(input_path)
    # Exit if video not opened.
    if not video.isOpened():
        print ("Could not open video")
        sys.exit()
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print ('Cannot read video file')
        sys.exit()

    trackers.append(create_and_init_tracker(frame, (1650,555,152,200), "objeto_1"))
    trackers.append(create_and_init_tracker(frame, (630,875,146,212), "objeto_0"))
    trackers.append(create_and_init_tracker(frame, (965,406,144,165), "objeto_2"))

    # Obtain frame size information using get() method
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    frame_size = (frame_width,frame_height)
    fps = 24

    # Initialize video writer object
    # fourcc = cv2.VideoWriter_fourcc(*'X264')
    # fourcc = cv2.VideoWriter_fourcc(*'xmkv')
    # fourcc = cv2.VideoWriter_fourcc('a','v','c','1')
    # fourcc = cv2.VideoWriter_fourcc('x','2','6','4')
    # output = cv2.VideoWriter(output_path, fourcc, fps, frame_size)
    output = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)

    # Initial call to print 0% progress
    bitrate = int(video.get(cv2.CAP_PROP_BITRATE))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # printProgressBar(0, total_frames, prefix = 'Progress:', suffix = 'Complete', length = 50)
    progress(0, total_frames, suffix='')
    i=0
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        
        # Start timer
        timer = cv2.getTickCount()

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        for tracker_wrapper in trackers:
            # Update tracker
            ok, bbox = tracker_wrapper.tracker.update(frame)

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
                cv2.putText(frame, tracker_wrapper.name , p1, cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
            else :
                # Tracking failure
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Write frame
        output.write(frame)
       
        i += 1
        if (i-1) % 10 == 0:
            progress(i+1, total_frames, suffix='')
        
    # Release the objects
    progress(total_frames, total_frames, suffix='')
    video.release()
    output.release()


if __name__ == '__main__' :
    sys.stderr.write('Error\n')   
    sys.stdout.write('Todo bien\n')   
    # Define logger
    logger = logging.getLogger('ObjectTracker')
    logger.setLevel(logging.DEBUG) # set logger level
    logFormatter = logging.Formatter("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
    consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    get_tracking()