import NumGenerator
import time
import sorts.Insertie
import sorts.Selectie
import sorts.BubbleSort
import sorts.MergeSort
import sorts.Numarare
import sorts.QuickSort

N = 10
#NumGenerator.numGenerator(N)

with open("sir.txt", "r") as f:
    text = f.read()
    numList = text.split("\n")

    numList.pop()
    intList = [int(i) for i in numList]

    intList.insert(0, 0) #pentru a putea face initializarea de la 1

print("""
        Choice 1: Insertie
        Choice 2: Selectie
        Choice 3: BubbleSort
        Choice 4: MergeSort
        Choice 5: Numarare
        Choice 6: QuickSort
        """
)

choice = int(input("Type your choice: "))

start = time.time()

match choice:
    case 1: #Insertie
        print("Insertie timp ")
        sortedList = sorts.Insertie.insertie(intList, N)
    case 2: #Selectie
        print("Selectie timp ")
        sortedList = sorts.Selectie.selectie(intList, N)
    case 3: #BubbleSort
        print("BubbleSort timp ")
        sortedList = sorts.BubbleSort.bubbleSort(intList, N)
    case 4: #MergeSort
        print("MergeSort timp ")
        sortedList = sorts.MergeSort.mergeSort(intList, 1, N)
    case 5: #Numarare
        print("Numarare timp ")
        sortedList = sorts.Numarare.numarate(intList, N)
    case 6: #QuickSort
        print("QuickSort timp ")
        sortedList = sorts.QuickSort.quickSort(intList, 1, N)

end = time.time()

sortedList.remove(0) #pentru a elimina primul 0 pus
with open("afis.txt", "w") as f: # pentru scrierea in fisierul de afisare
    for i in sortedList:
        f.write(str(i) + "\n")

print("{0:.6f}".format(end - start))
