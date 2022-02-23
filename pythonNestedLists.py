if __name__ == '__main__':
    lis = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name, score])
    minValue = min(lis, key=lambda x: x[1])
    removeMin = []
    for x in lis:
        if x[1] != minValue[1]:
            removeMin.append(x)

    minValue = min(removeMin, key=lambda x: x[1])
    result = []
    for x in removeMin:
        if x[1] == minValue[1]:
            result.append(x)

    print(removeMin)
    result = sorted(result, reverse=False)
    for x in result:
        print(x[0])
