from typing import List


def solution(A: List[int], K: int) -> List[int]:
    """Return array A rotated K times to the right.

    Rotation moves every element one step to the right and the last element
    becomes the first. Doing this K times is equivalent to moving each
    element to index (i + K) % N.

    Args:
        A: list of integers
        K: non-negative integer number of rotations

    Returns:
        A new list representing A rotated K times.

    Examples:
        >>> solution([3,8,9,7,6], 1)
        [6, 3, 8, 9, 7]
        >>> solution([3,8,9,7,6], 3)
        [9, 7, 6, 3, 8]
        >>> solution([], 5)
        []
    """
    if not A:
        return []

    n = len(A)
    k = K % n  # effective rotations
    if k == 0:
        # no change
        return A.copy()

    # split and swap: last k elements come first
    return A[-k:] + A[:-k]


if __name__ == "__main__":
    # quick manual check
    print(solution([3, 8, 9, 7, 6], 1))