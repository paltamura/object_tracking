from enum import Enum
import sys
import cv2
from h264writer import H264Writer
from helper import Helper
from os.path import exists


class TrackerType(Enum):
    BOOSTING = 'BOOSTING'
    MIL = 'MIL'
    KCF = 'KCF'
    TLD = 'TLD'
    MEDIANFLOW = 'MEDIANFLOW'
    GOTURN = 'GOTURN'
    MOSSE = 'MOSSE'
    CSRT = 'CSRT'


class InitialCondition(object):
    def __init__(self, object):
        self.object_name = object['object']
        self.id = object['id']
        self.coordinates = object['coordinates']


class TrackerWrapper:
    def __init__(self, initial_condition, tracker) -> None:
        self.initial_condition = initial_condition
        self.tracker = tracker


class MultiTracker():
    

    def create_tracker(self, tracker_type):
        if tracker_type.name == 'BOOSTING':
            return cv2.TrackerBoosting_create()
        if tracker_type.name == 'MIL':
            return cv2.TrackerMIL_create()
        if tracker_type.name == 'KCF':
            return cv2.TrackerKCF_create()
        if tracker_type.name == 'TLD':
            return cv2.TrackerTLD_create()
        if tracker_type.name == 'MEDIANFLOW':
            return cv2.TrackerMedianFlow_create()
        if tracker_type.name == 'GOTURN':
            return cv2.TrackerGOTURN_create()
        if tracker_type.name == 'MOSSE':
            return cv2.TrackerMOSSE_create()
        if tracker_type.name == "CSRT":
            return cv2.TrackerCSRT_create()

    def create_and_init_tracker(self, ref_frame, initial_condition, tracker_type):
        coordinates = initial_condition.coordinates
        tracker = self.create_tracker(tracker_type)
        tracker.init(ref_frame, tuple(coordinates))
        return TrackerWrapper(initial_condition, tracker)

    def tracking_calculate(
        self, 
        initial_conditions,
        _video_input_file,
        _video_output_file,
        _tracker_algorithm,
        _vcodec,
        _compression_log_level,
        _output_fps,
        _output_bitrate,
        _output_bitrate_inherits_from_input):

        if not exists(_video_input_file):
            Helper.get_log().error('Could not open ' + _video_input_file)
            sys.exit()
        video = cv2.VideoCapture(_video_input_file)

        if not video.isOpened():
            Helper.get_log().error("Could not open video")
            sys.exit()
        ok, first_frame = video.read()

        if not ok:
            Helper.get_log().error('Cannot read video file')
            sys.exit()

        tracker_wrappers = []
        for initial_condition in initial_conditions:
            tracker_wrappers.append(self.create_and_init_tracker(
                first_frame, initial_condition, TrackerType[_tracker_algorithm]))

        # fps = 24
        # bitrate = 3000
        bitrate = _output_bitrate
        if _output_bitrate_inherits_from_input:
            bitrate = int(video.get(cv2.CAP_PROP_BITRATE))

        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        Helper.get_log().info('=====================================================================')
        Helper.get_log().info('Input')
        Helper.get_log().info('=====================================================================')
        Helper.get_log().info('Initial conditions with ' + str(len(initial_conditions)) + ' bounding boxes founded')
        Helper.get_log().info('Input video file readed with ' + str(total_frames) + ' frames' + ' and bitrate of ' + str(bitrate))
        Helper.get_log().info('')

        # Print process progress
        Helper.get_log().info('=====================================================================')
        Helper.get_log().info('Process')
        Helper.get_log().info('=====================================================================')
        Helper.get_log().info('Start to tracking calculate . . .')
        frac = total_frames / 10
        i = 0
        suffix = 'Processed frames'
        Helper.progress(i, total_frames, suffix=suffix)
        first_iteration = True
        faults = 0
        with H264Writer(_video_output_file, bitrate, _output_fps) as h264Writer:
            while True:
                # Reincorporar el primer frame
                if first_iteration:  
                    first_iteration = False
                    cv2_frame = first_frame
                    has = True
                else:
                    has, cv2_frame = video.read()
                if has:
                    for tracker_wrapper in tracker_wrappers:
                        # Update tracker
                        ok, bbox = tracker_wrapper.tracker.update(cv2_frame)
                        # Draw bounding box
                        if ok:
                            # Tracking success
                            p1 = (int(bbox[0]), int(bbox[1]))
                            p2 = (int(bbox[0] + bbox[2]),
                                  int(bbox[1] + bbox[3]))
                            cv2.rectangle(cv2_frame, p1, p2, (255, 0, 0), 2, 1)
                            name = tracker_wrapper.initial_condition.object_name + str(tracker_wrapper.initial_condition.id)
                            cv2.putText(cv2_frame, name, p1, cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
                        else:
                            # Tracking failure
                            cv2.putText(cv2_frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                            Helper.get_log().info('Tracking failure detected in frame number ' + i)
                            faults += 1

                    frame = cv2.cvtColor(cv2_frame, cv2.COLOR_BGR2RGB)
                    h264Writer.add_frame(frame)
                    i += 1
                    if i % frac == 0:
                        Helper.progress(i+1, total_frames, suffix=suffix)
                else:
                    break

        video.release()
        Helper.get_log().info('Tracking calculate completed successfully.')
        Helper.get_log().info('')

        # Print some metrics summary
        trackers_count = len(tracker_wrappers)
        total_bounding_boxes = (total_frames * trackers_count)
        sucess_case_count = (total_frames * trackers_count) - faults
        Helper.get_log().info('=====================================================================')
        Helper.get_log().info('Summary')
        Helper.get_log().info('=====================================================================')
        Helper.get_log().info(str(sucess_case_count) + ' bounding boxes detected, over an total of ' + str(total_bounding_boxes))
        Helper.get_log().info(str(total_frames) + ' frames analyzed by ' + str(trackers_count) + ' trackers.')
        Helper.get_log().info('Output file was persisted in ' + _video_output_file)
