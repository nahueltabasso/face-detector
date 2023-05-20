import sys
import os
import uuid
sys.path.append('../../')
from fastapi import File, UploadFile
from dotenv import load_dotenv
from scripts.face_detector_fr import detect_faces
from config.logger_config import logger
from util.util import conver_to_nparray


STR_TO_BOOL = {"True": True, "False": False}
load_dotenv()


def detected_faces_from_image(file: UploadFile = File(...)) -> dict:
    """Method Signature to detected faces from an image

    Args:
        file (UploadFile, optional): _description_. Defaults to File(...).
    """
    
    logger.info("Enter to detected_faces_from_image()")
    
    # Convert to numpy array
    file_array = conver_to_nparray(file= file)

    # output = '../../data/image.jpg'
    output = os.getenv('OUTPUT_DIRECTORY') + "/" + str(uuid.uuid4()) + ".jpg"
    save_flag = os.getenv('SAVE_FILE')
    save_flag = STR_TO_BOOL.get(save_flag)
    # Detected faces in image
    response = detect_faces(image=file_array, output_dir=output, save=save_flag)
    return response


def validated_api_key(api_key: str) -> bool:
    """Method Signature to valid the api_key

    Args:
        api_key (str): _description_

    Returns:
        bool: _description_
    """
    
    logger.info("Enter to validated_api_key()")
    if api_key is None or api_key == '':
        return False
    
    apis_key_valids = os.getenv('APIs_KEY_VALIDS')
    apis_key_valids = apis_key_valids.split(",")
    
    if api_key in apis_key_valids:
        return True
    
    return False
        
    