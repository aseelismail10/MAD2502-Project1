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
    a = x_vals[0]
    b = x_vals[-1]
    n = len(x_vals)
    delta_x = (b-a)/(n-1)
    left_endpoints = func(x_vals[ : -1])
    left_sum = np.sum(left_endpoints * delta_x)
    return left_sum

def simpson(x_vals: np.ndarray, func: np.ufunc): 
    a = x_vals[0]
    b = x_vals[-1]
    outside = b-a/6
    part1 = func(a)
    part2 = 4*(func((a+b)/2))
    part3 = func(b)
    final_simpson = outside(part1 + part2 + part3)
    return final_simpson
