import math

def vector_add(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i,w_i in zip(v, w)]

def vector_subtract(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors)
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

def vector_scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

assert vector_scalar_multiply(1 / n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
assert dot([1,2,3], [4,5,6]) == 32

def sum_of_squares(v:Vector) -> float:
    return dot(v, v)
assert sum_of_squares([1,2,3]) == 14

def magnitude(v:Vector) -> float:
    return math.sqrt(sum_of_squares)

def vector_distance(v:Vector,w:Vector) -> float:
    return magnitude(vector_subtract(v, w))