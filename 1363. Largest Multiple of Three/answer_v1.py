from typing import List


def largestMultipleOfThree(digits: List[int]) -> str:
    def create_result(li):
        if not li:
            return ""
        li.sort(reverse=True)
        f_string = "".join([str(d) for d in li])
        return f_string[:-1].lstrip('0') + f_string[-1]

    if sum(digits) % 3 == 0:
        return create_result(digits)
    
    digits.sort(reverse=True)
    rest = [(d, d % 3) for d in digits if d % 3 != 0]
    divisible = [d for d in digits if d % 3 == 0]
    
    exclude = []
    add_digits = []
    
    sorted_ds = sorted(rest, key=lambda x: x[0])
    sorted_divs = sorted(sorted_ds, key=lambda x: x[1], reverse=True)
    
    sum_divs = sum([d[1] for d in rest])

    i = 0

    while sum_divs % 3 != 0 and i < len(sorted_divs):
        if (sum_divs % 3) - sorted_divs[i][-1] >= 0:
            sum_divs = sum_divs - sorted_divs[i][-1]
            exclude.append(i)
        i += 1

    if sum_divs % 3 == 0:
        add_digits = [d[0] for i, d in enumerate(sorted_divs) if i not in exclude]
    return create_result(divisible + add_digits)


print(largestMultipleOfThree([8,6,7,1,0]))
