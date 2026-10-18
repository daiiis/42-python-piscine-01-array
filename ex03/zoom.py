import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """Load animal.jpeg, cut a 400x400 grey square and display it."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        print(image)
        zoom = image[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)
        plt.imshow(zoom[:, :, 0], cmap="gray")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
