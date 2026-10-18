import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray | None:
    """Load a JPG/JPEG image, print its shape and return its RGB pixels.

    Return None and print an error message if the image cannot be loaded.
    """
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError("only JPG and JPEG files are supported")
        image = Image.open(path)
        image = image.convert("RGB")
        array = np.array(image)
        print(f"The shape of image is: {array.shape}")
        return array
    except Exception as error:
        print(f"Error: cannot load image: {error}")
        return None
