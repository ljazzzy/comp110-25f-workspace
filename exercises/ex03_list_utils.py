"""
ex03_list_utils.py

Implements simple list utilities (all, max, is_equal) as an exercise
in manual algorithm implementation.
"""

author = "730760217"  # 9-digit student PID

def all(lst: list[int], num: int) -> bool:
    if len(lst) == 0:
        return False
    i = 0
    while i < len(lst):
        if lst[i] != num:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i = 1
    max_val = input[0]
    while i < len(input):
        if input[i] > max_val:
            max_val = input[i]
        i += 1
    return max_val


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) != len(lst2):
        return False
    i = 0
    while i < len(lst1):
        if lst1[i] != lst2[i]:
            return False
        i += 1
    return True


# Quick local tests (will only run when this file is executed directly)
if __name__ == "__main__":
    print("all([1,1,1], 1) ->", all([1,1,1], 1))     # True
    print("all([], 1) ->", all([], 1))               # False
    print("max([1,3,2]) ->", max([1,3,2]))           # 3
    print("is_equal([1,2],[1,2]) ->", is_equal([1,2],[1,2]))  # True
    print("is_equal([],[]) ->", is_equal([],[]))     # True

