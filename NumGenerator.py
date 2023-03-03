import random

def numGenerator(N):
    with open("sir.txt", "w") as f:
        for i in range(N):
            f.write(str(random.randint(-1000,1000)) + "\n")
            # f.write(str(N - i) + "\n") #numere descrescatoare
            # f.write(str(i) + "\n") #numere crescatoare
