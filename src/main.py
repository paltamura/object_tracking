import sys
from multitracker import InitialCondition, MultiTracker
import json
import helper

def get_initial_conditions_from_json(json_input):
    initial_conditions = []
    with open(initial_conditions_file) as json_file:
        data = json.load(json_file)
        for item in data:
            initial_condition = InitialCondition(item)
            initial_conditions.append(initial_condition)
    return initial_conditions

def tracking_calculate(_initial_conditions_file, _video_input_file, _video_output_file):
    # Get initial conditions
    initial_conditions = get_initial_conditions_from_json(_initial_conditions_file)
    # Agregar verificación de archivos y formatos.
    # Agregar exceptions y log de errores.
    # Imprimir un resumen de las initial_conditions encontradas. Lo mismo con el video. 
    MultiTracker().tracking_calculate(initial_conditions, _video_input_file, _video_output_file)

if __name__ == "__main__":
    #
    # Read configurations
    config = helper.read_config()
    initial_conditions_file = config['Paths']['InitialConditionsFile']
    video_input_file = config['Paths']['VideoInputFile']
    video_output_file = config['Paths']['VideoOutputFile']
    tracker_algorithm = config['Tracking']['TrackerAlgorithm']
    vcodec = config['Video Compression']['VCodec']
    compression_log_level = config['Video Compression']['CompressionLogLevel']
    output_fps = config['Video Compression']['OutputFps']
    output_bitrate = config['Video Compression']['OutputBitrate']
    output_crf = config['Video Compression']['OutputCrf']
    #
    # Print configurations used
    sys.stdout.write('================================================================:' + '\n')
    sys.stdout.write('Tracking processing is initialized with these configurations:' + '\n')
    sys.stdout.write(' - initial conditions file:' + initial_conditions_file + '\n')
    sys.stdout.write(' - input video file:' + video_input_file + '\n')
    sys.stdout.write(' - output video file:' + video_output_file + '\n')
    sys.stdout.write('================================================================:' + '\n')
    #
    # aca pasar toda la config por argumentos y tambien imprimir que se va a procesar y como en stdout.
    tracking_calculate(initial_conditions_file, video_input_file, video_output_file)
