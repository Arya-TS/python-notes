if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = arr[0]
    second_largest = float('-inf')

    for mark1 in arr:
        if mark1 > largest:
            largest = mark1
    for mark1 in arr:
        if mark1 != largest:
            if mark1 > second_largest:
                second_largest = mark1
    print(second_largest)
