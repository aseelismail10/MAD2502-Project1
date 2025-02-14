import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    """ Takes an input of 2x3 array called triangle_coordinates that has corresponding x and y
    values for three points and a 1d array called point_coordinates that is in the
    form (xy) of a point.
    Returns a 1d array with the corresponding barycentric coordinates """
    coef = np.transpose(triangle_coordinates)
    coef = np.append(coef, [[1,1,1]], axis=0)
    answer = np.insert(point_coordinates, 2,[1])
    answer = np.transpose(answer)
    barycentric_coordinates = np.linalg.solve(coef, answer)
    return barycentric_coordinates