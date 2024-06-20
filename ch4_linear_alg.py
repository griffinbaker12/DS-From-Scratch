from typing import List

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """
    Adds corresponding elements
    """
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """
    Adds corresponding elements
    """
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "No vectors provided"

    num_elements = len(vectors[0])
    assert all(
        len(v) == num_elements for v in vectors
    ), "different sized vectors won't fly chief"

    # add the i-th elements
    return [sum(v[i] for v in vectors) for i in range(num_elements)]


def vector_sum_no_comp(vectors: List[Vector]) -> Vector:
    assert vectors, "No vectors provided"

    num_elements = len(vectors[0])
    assert all(
        len(v) == num_elements for v in vectors
    ), "different sized vectors won't fly chief"

    new_vector = [0 for _ in range(num_elements)]
    for v in vectors:
        for i in range(num_elements):
            new_vector[i] += v[i]

    return new_vector


vect_sum_test_arr = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
]

assert (
    vector_sum(vect_sum_test_arr) == [16, 20] == vector_sum_no_comp(vect_sum_test_arr)
)


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(v: List[Vector]) -> Vector:
    n = len(v)
    return scalar_multiply(1 / n, vector_sum(v))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot_product(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same len"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot_product([1, 2, 3], [4, 5, 6]) == 32
