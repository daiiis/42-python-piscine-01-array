import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of family and return the rows from start to end."""
    if not isinstance(family, list) or len(family) == 0:
        raise TypeError("family must be a non-empty list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")
    first_size = len(family[0])
    for row in family:
        if len(row) != first_size:
            raise ValueError("all rows of family must have the same size")
    for index in (start, end):
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("start and end must be int")
    array = np.array(family)
    print(f"My shape is : {array.shape}")
    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
