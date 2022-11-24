from typing import List


def largestMultipleOfThree(digits: List[int]) -> str:
    def create_result(li):
        if not li:
            return ""
        li.sort(reverse=True)
        f_string = "".join([str(d) for d in li])
        return f_string[:-1].lstrip('0') + f_string[-1]

    digits = sorted(digits)
    sum_digits = sum(digits)

    if sum_digits % 3 == 0:
        return create_result(digits)

    elif sum_digits % 3 == 1:
        find = iter(i for i, d in enumerate(digits) if d in [1, 4, 7])
        idx = next(find, None)
        if idx != None:
            return create_result(digits[:idx] + digits[idx+1:])
        find = iter(i for i, d in enumerate(digits) if d in [2, 5, 8])
        idx = next(find, None)
        if idx != None:
            idx_2 = next(find, None)
            if idx_2 != None:
                return create_result(digits[:idx] + digits[idx+1:idx_2] + digits[idx_2+1:])

    elif sum_digits % 3 == 2:
        find = iter(i for i, d in enumerate(digits) if d in [2, 5, 8])
        idx = next(find, None)
        if idx != None:
            return create_result(digits[:idx] + digits[idx+1:])
        find = iter(i for i, d in enumerate(digits) if d in [1, 4, 7])
        idx = next(find, None)
        if idx != None:
            idx_2 = next(find, None)
            if idx_2 != None:
                return create_result(digits[:idx] + digits[idx+1:idx_2] + digits[idx_2+1:])

    return create_result([])

print(largestMultipleOfThree([5,2,3]))
