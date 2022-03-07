import os
import sys
from multitracker import InitialCondition, MultiTracker
import json
from helper import Helper
from os.path import exists


def get_initial_conditions_from_json(json_input):
    if not exists(json_input):
        Helper.get_log().error('Could not open ' + json_input)
        sys.exit()
    initial_conditions = []
    try:
        with open(json_input) as json_file:
            data = json.load(json_file)
            for item in data:
                initial_condition = InitialCondition(item)
                initial_conditions.append(initial_condition)
        return initial_conditions
    except Exception as e:
        Helper.get_log().error('Failed reading ' + json_input)
        sys.exit()


def tracking_calculate(
        _initial_conditions_file, 
        _video_input_file, 
        _video_output_file, 
        _tracker_algorithm,
        _vcodec,
        _compression_log_level,
        _output_fps,
        _output_bitrate,
        _output_bitrate_inherits_from_input):
    # Get initial conditions
    initial_conditions = get_initial_conditions_from_json(_initial_conditions_file)
    # Invoke main process
    MultiTracker.tracking_calculate(
        initial_conditions, 
        _video_input_file, 
        _video_output_file, 
        _tracker_algorithm,
        _vcodec,
        _compression_log_level,
        _output_fps,
        _output_bitrate,
        _output_bitrate_inherits_from_input)

# Application entry point
if __name__ == "__main__":
    # Read configurations
    config = Helper.get_config()
    input_path = config['Paths']['InputPath']
    output_path = config['Paths']['OutputPath']
    initial_conditions_file = config['Paths']['InitialConditionsFile']
    video_input_file = config['Paths']['VideoInputFile']
    video_output_file = config['Paths']['VideoOutputFile']
    tracker_algorithm = config['Tracking']['TrackerAlgorithm']
    vcodec = config['Video Compression']['VCodec']
    compression_log_level = config['Video Compression']['CompressionLogLevel']
    output_fps = config['Video Compression']['OutputFps']
    output_bitrate = config['Video Compression']['OutputBitrate']
    output_bitrate_inherits_from_input = config['Video Compression']['OutputBitrateInheritsFromInput']
    # Print configurations
    Helper.get_log().info('=====================================================================')
    Helper.get_log().info('Configurations')
    Helper.get_log().info('=====================================================================')
    Helper.get_log().info('PATHS')
    Helper.get_log().info(' • initial_conditions_file: ' + initial_conditions_file)
    Helper.get_log().info(' • video_input_file: ' + video_input_file)
    Helper.get_log().info(' • video_output_file: ' + video_output_file)
    Helper.get_log().info('TRACKING')
    Helper.get_log().info(' • tracker_algorithm: ' + tracker_algorithm)
    Helper.get_log().info('COMPRESSION')
    Helper.get_log().info(' • vcodec: ' + vcodec)
    Helper.get_log().info(' • compression_log_level: ' + compression_log_level)
    Helper.get_log().info(' • output_fps: ' + output_fps)
    Helper.get_log().info(' • output_bitrate: ' + output_bitrate)
    Helper.get_log().info(' • output_bitrate_inherits_from_input: ' + output_bitrate_inherits_from_input)
    Helper.get_log().info('')
    # I make sure the input path exists.
    if not exists(input_path):
        Helper.get_log().error('Path ' + input_path + ' not found.')
        sys.exit()
    # I make sure the output path exists.
    os.makedirs(output_path, exist_ok=True)
    # Invoke main process
    tracking_calculate(
        initial_conditions_file, 
        video_input_file, 
        video_output_file, 
        tracker_algorithm,
        vcodec,
        compression_log_level,
        output_fps,
        output_bitrate,
        output_bitrate_inherits_from_input)
