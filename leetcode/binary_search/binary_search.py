def binary_search(arr, target):
    low_index = 0
    high_index = len(arr) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        mid_element = arr[mid_index]

        if mid_element == target:
            return mid_index
        elif arr[mid_index] < target:
            low_index = mid_index + 1
        elif arr[mid_index] > target:
            high_index = mid_index - 1

    return None


# test cases
assert binary_search([1, 2, 3, 4, 5], 4) == 3
assert binary_search([1], 1) == 0
assert binary_search([], 5) is None
assert binary_search([1, 2, 3, 4], 5) is None
