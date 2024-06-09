def solution(arr):
    arr1 = list(set(arr))

    arr1.sort(reversed=True)

    return arr1