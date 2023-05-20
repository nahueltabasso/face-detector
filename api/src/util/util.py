from fastapi import UploadFile, File
from PIL import Image
from io import BytesIO
import numpy as np

def valid_img_file(file: UploadFile = File(...)):
    """Method signature to valid a file if is or not an image

    Args:
        file (UploadFile, optional): _description_. Defaults to File(...).

    Returns:
        _type_: _description_
    """
    
    try:
        img = Image.open(BytesIO(file.file.read()))
        return True
    except:
        return False
    

def conver_to_nparray(file: UploadFile = File(...)):
    """Method Signature to convert a FastApi File to a numpy array

    Args:
        file (UploadFile, optional): _description_. Defaults to File(...).

    Returns:
        _type_: _description_
    """
    
    # Reposition the file pointer to the start of the file
    file.file.seek(0)
    img = Image.open(BytesIO(file.file.read()))
    
    # Transform to an numpy array
    img_array = np.array(img)
    return img_array