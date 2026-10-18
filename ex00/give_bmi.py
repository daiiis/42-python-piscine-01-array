import numpy as np


def check_numbers(values: list, name: str) -> None:
    """Raise an error if values is not a list of int or float."""
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must contain only int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Return the BMI (weight / height ** 2) for each person."""
    check_numbers(height, "height")
    check_numbers(weight, "weight")
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same size")
    if any(h <= 0 for h in height):
        raise ValueError("height must be greater than 0")
    h = np.array(height)
    w = np.array(weight)
    return (w / h ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI above the limit, else False."""
    check_numbers(bmi, "bmi")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an int")
    return (np.array(bmi) > limit).tolist()
