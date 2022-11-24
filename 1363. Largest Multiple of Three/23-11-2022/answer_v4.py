from typing import List
import collections


def largestMultipleOfThree(digits: List[int]) -> str:
    def create_result(li):
        if not li:
            return ""
        parsed_li = [str(i)*li[i] for i in sorted(li, reverse=True)]
        f_string = "".join(parsed_li)
        return f_string[:-1].lstrip('0') + f_string[-1] if f_string else ""

    if not digits:
        return ""

    # memory = [0] * 10

    # for d in digits:
    #     memory[d] += 1

    memory = collections.Counter(digits)
    print(memory)

    sum_digits = sum(digits)

    if sum_digits % 3 == 1:
        if memory[1] + memory[4] + memory[7] >= 1:
            if memory[1]:
                memory[1] -= 1
            elif memory[4]:
                memory[4] -= 1
            else:
                memory[7] -= 1
        elif memory[2] + memory[5] + memory[8] >= 2:
            for i in range(2):
                if memory[2]:
                    memory[2] -= 1
                elif memory[5]:
                    memory[5] -= 1
                else:
                    memory[8] -= 1
        else: return create_result([])

    elif sum_digits % 3 == 2:
        if memory[2] + memory[5] + memory[8] >= 1:
            if memory[2]:
                    memory[2] -= 1
            elif memory[5]:
                memory[5] -= 1
            else:
                memory[8] -= 1
        elif memory[1] + memory[4] + memory[7] >= 2:
            for i in range(2):
                if memory[1]:
                    memory[1] -= 1
                elif memory[4]:
                    memory[4] -= 1
                else:
                    memory[7] -= 1

        else: return create_result([])

    return create_result(memory)



print(largestMultipleOfThree([8,9,1]))
