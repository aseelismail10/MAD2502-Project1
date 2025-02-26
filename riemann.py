import numpy as np

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float :
    """ approximates the area between a curve and the x-axis over a given interval
    using trapezoids according to the riemann sum trapezoidal rule

    takes a numpy array of x values and a corresponding function, returns a float"""
    a, b = x_vals[0], x_vals[-1]
    n = len(x_vals)
    delta_x = (b - a)/(n-1)
    middle = func(x_vals[1:-1]) * 2
    area = (0.5 * delta_x) * ((func(x_vals[0])) + np.sum(middle) + func(x_vals[-1]))
    return area

def left_endpoint (x_vals: np.ndarray, func: np.ufunc): 
    """ approximates the area between a curve and the x-axis over a given interval by dividing the
    interval into smaller subintervals and using the left endpoint value of each subinterval for
    the height"""
    a = x_vals[0]
    b = x_vals[-1]
    n = len(x_vals)
    delta_x = (b-a)/(n-1)
    left_endpoints = func(x_vals[ : -1])
    left_sum = np.sum(left_endpoints * delta_x)
    return left_sum

def simpson(x_vals: np.ndarray, func: np.ufunc): 
    """takes the x values and y values over a given interval and slices them to get the correct values 
    to return the reimann simpson function"""
    n = len(x_vals)
    a = x_vals[0]
    b = x_vals[-1]
    h = (b-a)/(n - 1)
    y_vals = func(x_vals)
    weights = np.arange(n)
    weights[1:-1:3] = 3
    weights[2:-1:3] = 3
    weights[3:-1:3] = 2
    weights[0], weights[-1] = 1, 1
    final_simpson = (3/8*h) * (np.sum(weights * y_vals))
    return final_simpson
