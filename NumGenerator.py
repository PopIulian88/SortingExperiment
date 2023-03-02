import random

def numGenerator(N):
    with open("sir.txt", "w") as f:
        for i in range(N):
            f.write(str(random.randint(-9,9)) + "\n")
