import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Return a 2D array with rows and columns swapped, using loops."""
    rows, cols = array.shape[0], array.shape[1]
    result = np.empty((cols, rows), dtype=array.dtype)
    for i in range(rows):
        for j in range(cols):
            result[j, i] = array[i, j]
    return result


def main():
    """Load animal.jpeg, cut a square, transpose it and display it."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        square = image[100:500, 450:850, 0:1]
        print(f"The shape of image is: {square.shape}")
        print(square)
        rotated = ft_transpose(square[:, :, 0])
        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)
        plt.imshow(rotated, cmap="gray")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
