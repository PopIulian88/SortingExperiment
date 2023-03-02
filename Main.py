import NumGenerator
import sorts.Insertie
import time

N = 5

#NumGenerator.numGenerator(N)

with open("sir.txt", "r") as f:
    text = f.read()
    numList = text.split("\n")

    numList.pop()
    intList = [int(i) for i in numList]

    intList.insert(0, 0) #pentru a putea face initializarea de la 1

start = time.time()
sortedList = sorts.Insertie.insertie(intList, N)
end = time.time()

sortedList.remove(0) #pentru a elimina primul 0 pus
with open("afis.txt", "w") as f:
    for i in sortedList:
        f.write(str(i) + "\n")

print("{0:.6f}".format(end - start))
