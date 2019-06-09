import math
import sys
from functools import reduce


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_1 + w_1 for v_1, w_1 in zip(v, w)]


def vector_subtract(v, w):
    """subtract corresponding elements"""
    return [v_1 - w_1 for v_1, w_1 in zip(v, w)]


def vector_sum(vectors):
    """sums all corresponding elements"""
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """
    compute the vector whose ith element is the mean of the ith elements
    of the input vectors
    """
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_1 * w_1 for v_1, w_1 in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    """
    euclidean algorithm
    see phormula at: https://en.wikipedia.org/wiki/Euclidean_distance
    """
    return math.sqrt(squared_distance(v, w))


def distance_with_magnitude(v, w):
    """same as distance (defined prior)"""
    return magnitude(vector_subtract(v, w))


if "vector" in sys.argv:
    print("### vector.py ###")
    a = [1, 2, 3, 4]
    b = [7, 6, 5, 4]
    c = [0, 0, 3, 8]

    print(vector_add(a, b))
    print(vector_subtract(a, b))
    print(vector_sum([a, b, c]))
    print(scalar_multiply(5, a))
    print(vector_mean([a, b, c]))
    print(dot(a, b))
    print(sum_of_squares(a))
    print(magnitude(a))
    print(squared_distance(a, b))
    print(distance(a, b))
    print(distance_with_magnitude(a, b))
