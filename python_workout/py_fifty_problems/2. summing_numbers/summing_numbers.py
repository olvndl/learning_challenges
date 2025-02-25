def mysum(*numbers):
    for number in numbers:
        if not isinstance(number, (int, float)):
            print("Not all values are of numeric type!")
            return -1
    result = 0
    for number in numbers:
        result += number
    return result


assert mysum(1, 2, 3) == 6
assert mysum(*[1, 2, 5]) == 8
assert mysum(1, 2, 3, "some value") == -1
