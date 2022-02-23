if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    result = list(arr)
    result = [value for value in result if value != max(result)]
    print(max(result))
