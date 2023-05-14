import cv2
import face_recognition as fr
import matplotlib.pyplot as plt
import numpy as np

print(f"OpenCV version = {cv2.__version__}")
print(f"Face Recognition version = {fr.__version__}")
print(f"Numpy version = {np.__version__}")

def show(images: list[np.ndarray], labels: list[str], show: bool=False):
    """This method show a list of images with it corresponding label
    used to the matplotlib library

    Args:
        images (list[np.ndarray]): _description_
        labels (list[str]): _description_
        show (bool, optional): _description_. Defaults to False.
    """
    # Create subplots
    fig, ax = plt.subplots(1, len(images), figsize=(10, 5))

    for index, img in enumerate(images):
        # Show each image in it subplot
        ax[index].imshow(img)
        ax[index].set_title(labels[index])

        # Adjust the position of subplots
        fig.tight_layout()

    # Show
    if show:
        plt.show()
        

def show_image(image: np.ndarray):
    print("")
        

def detect_faces(image: np.ndarray, output_dir: str='', save: bool=False):
    """This function process and detect faces in a picture

    Args:
        image (np.ndarray): image to process
        output_dir (str): directory to save a file
        save (bool, optional): Flag to save image after processing. Defaults to False.

    Returns:
        _type_: _description_
    """
    response = {}
    # Locate the bbox of a face or faces in the image
    locate_faces = fr.face_locations(image)
    if len(locate_faces) != 0:
        # Draw with OpenCV the rectangle of the face
        for locate in locate_faces:
            cv2.rectangle(img=image,
                        pt1=(locate[3], locate[0]),
                        pt2=(locate[1], locate[2]),
                        color=(0, 255, 0),
                        thickness=2)
        response = {
            "detected_face": True,
            "bbox_faces": locate_faces,
            "number_of_detected_faces": len(locate_faces)
        }           
        if save:
            cv2.imwrite(output_dir, image)
        return response
    # Not detected any faces in the image
    response = {"detected_face": False}
    return response
