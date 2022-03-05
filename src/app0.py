from multitracker import InitialCondition, MultiTracker
import json

def get_initial_conditions_from_json(json_input):
    initial_conditions = []
    with open(initial_conditions_file) as json_file:
        data = json.load(json_file)
        for item in data:
            initial_condition = InitialCondition(item)
            initial_conditions.append(initial_condition)
    return initial_conditions

def tracking_calculate(_initial_conditions_file, _video_input_file, _video_output_file):
    # get initial conditions
    # Agregar verificación de archivos y formatos.
    # Agregar exceptions y log de errores.
    initial_conditions = get_initial_conditions_from_json(_initial_conditions_file)
    # Imprimir un resumen de las initial_conditions encontradas. Lo mismo con el video. 
    MultiTracker().tracking_calculate(initial_conditions, _video_input_file, _video_output_file)

if __name__ == "__main__":
    # Default configuration
    data_path = 'data-io/'
    input_path = data_path + 'input/'
    output_path = data_path + 'output/'
    initial_conditions_file = input_path + 'initial_conditions.json'
    video_input_file = input_path + 'input.mkv'
    video_output_file = output_path + 'output.mkv'
    tracking_calculate(initial_conditions_file, video_input_file, video_output_file)
