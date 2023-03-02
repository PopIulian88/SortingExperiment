def bubbleSort(sir, n):
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if sir[i] > sir[i + 1]:
                sir[i], sir[i + 1] = sir[i + 1], sir[i]
                flag = True
    return sir
    