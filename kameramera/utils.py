import yaml

def load_conf(filepath) -> dict:
    """Load a YAML configuration file

    Args:
        filepath (str): The filepath of the conf YAML file. 
    """
    with open(filepath, 'r') as infile:
        return yaml.load(infile, Loader=yaml.FullLoader)