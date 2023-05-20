from fastapi import FastAPI, File, UploadFile, Header
from typing import Annotated
from config.logger_config import logger
from util.util import valid_img_file
from service import detected_faces_from_image, validated_api_key

app = FastAPI()

@app.post("/faceDetectAPI/detect_face", status_code=200)
def detect_face_in_image(api_key: Annotated[str, Header()] = None,
                         image: UploadFile = File(...)):
    """_summary_

    Args:
        api_key (Annotated[str, Header, optional): _description_. Defaults to None.
        image (UploadFile, optional): _description_. Defaults to File(...).

    Returns:
        _type_: _description_
    """
    
    logger.info("Enter to detect_face_in_image()")
    logger.info(f"Request Header api_key ----- {api_key}")
    logger.info(f"Request Image ----- {image.filename}")
    if not validated_api_key(api_key=api_key):
        logger.error("api_key Header can not be None")
        return {"status": 200, "error_code": "HEADER_NOT_VALID"}
    
    if not valid_img_file(image):
        logger.error("Received file is not an image")
        return {"status": 200, "error_code": "FILE_NOT_IMAGE"}
    
    response = detected_faces_from_image(file = image)
    
    return response        
