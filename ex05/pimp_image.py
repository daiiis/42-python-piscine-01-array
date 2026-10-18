import numpy as np
import matplotlib.pyplot as plt


def show(array: np.ndarray, title: str) -> None:
    """Display an image in a window with a title."""
    plt.imshow(array)
    plt.title(title)
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array
    show(inverted, "Invert")
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image received."""
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    show(red, "Red")
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel of the image received."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    show(green, "Green")
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of the image received."""
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    show(blue, "Blue")
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Turn the image received into shades of grey."""
    grey = array.copy()
    value = array.sum(axis=2) / 3
    for channel in range(3):
        grey[:, :, channel] = value
    show(grey, "Grey")
    return grey
