import yaml
import os
import glob
from pathlib import Path
from datetime import datetime

def load_conf(filepath) -> dict:
    """Load a YAML configuration file

    Args:
        filepath (str): The filepath of the conf YAML file. 
    """
    with open(filepath, 'r') as infile:
        return yaml.load(infile, Loader=yaml.FullLoader)

def get_closest_value(values, value) -> int:
    """Get the closest value

    In a list of values get the closest one

    Args:
        values (list): The list to get the closest. 
        value (int): The value we would like to come close to>

    Return:
        (int): The closest value
    """
    return min(values, key=lambda x:abs(x-value))

def build_index(filepath=os.path.join('kameramera', 'data', 'index.yml')):
    """Build the index file

    List all YAML files in data directory and create an index file

    Args:
        filepath (str): Filepath of the index output file. 
            Default: "kameramera\data\index.yml"
    """
    print('Building INDEX')
    camera_filepath = os.path.join('kameramera', 'data', 'camera', '*.yml')
    cameras = []
    nb_cameras = len(glob.glob(camera_filepath))

    print('    - Building camera index | nb of cameras {}'.format(nb_cameras))

    for camera in glob.glob(camera_filepath):
        cameras.append(
            {
                'manufacturer': load_conf(camera)['general']['manufacturer'],
                'name': load_conf(camera)['general']['name'],
                'id': Path(camera).stem,
                'path': camera
            }
        )

    data = {
        'last_update': datetime.now(),
        'cameras': cameras
    }

    print('Writing into file : {}'.format(filepath))
    with open(filepath, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)