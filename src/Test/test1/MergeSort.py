from typing import List, Any


def correct_elem(array: List[Any]):
    if not all(isinstance(element, type(array[0])) for element in array):
        raise TypeError(
            "All elements in the array must be of the same type and comparable."
        )
    else:
        merge_sort(array)


def merge_sort(array: List[Any]) -> List[Any]:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)


def merge(left: List[Any], right: List[Any]) -> List[Any]:
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
