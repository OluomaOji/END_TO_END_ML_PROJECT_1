import os
import yaml
from src.end_to_end_ML_project_1 import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    read yaml file and returns

    Args:
        path_to_yaml (str) : path like input

    Raises:
        ValueError : if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise  ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data

    Args:
        path (Path): path to json file
        data (dict); data to be saved in json file
    """
    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f'json file save at: {path}')

@ensure_annotations
def create_directories(path_to_directories):
    """
    Create list of directoreis

    Args:
        path_to_directores (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created.
    """
    if isinstance(path_to_directories, str):
        path_to_directories = [path_to_directories]
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f'created directory at: {path}')