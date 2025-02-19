import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    """ Takes an input of 2x3 array called triangle_coordinates that has corresponding x and y
    values for three points and a 1d array called point_coordinates that is in the
    form (x,y) of a point.
    Returns a 1d array with the corresponding barycentric coordinates """
    coef = np.transpose(triangle_coordinates)
    coef = np.append(coef, [[1,1,1]], axis=0)
    answer = np.insert(point_coordinates, 2,[1])
    answer = np.transpose(answer)
    barycentric_coordinates = np.linalg.solve(coef, answer)
    return barycentric_coordinates

def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    """ Takes an input of 2x3 array called triangle_coordinates that has corresponding x and y
    values for three points and a 1d array called barycentric_coordinates that is in the
    form (λ1,λ2,λ3).
    Returns a 1d array which has the form (x, y) """
    T1, T2, T3 = np.transpose(triangle_coordinates)
    x = barycentric_coordinates[0] * T1[0] + barycentric_coordinates[1] * T2[0] + barycentric_coordinates[2] * T3[0]
    y = barycentric_coordinates[0] * T1[1] + barycentric_coordinates[1] * T2[1] + barycentric_coordinates[2] * T3[1]
    return np.array([x,y])

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> bool:
    """ Takes an input of 2x3 array called triangle_coordinates that has corresponding x and y
    values for three points and a 1d array called point_coordinates that is in the
    form (x,y) of a point.
    Returns a bool as to whether the point lies inside of the triangle or not. """
    coord = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    result = all(coord >= 0) and np.isclose(np.sum(coord), 1)
    return result
    
