import configparser

# Read config file settings
def read_config():
    config = configparser.ConfigParser()
    config.read('./configurations.ini')
    return config
