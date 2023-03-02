def insertie(sir, n):
    b = []  #initializam pe b
    for i in range(0, n + 1):
        b.append(0)

    b[1] = sir[1]
    i = 2
    while i <= n:
        j = i - 1 #cautam pozitia j,dupa care se va insera sir[i]
        while(j>=1 and sir[i]<b[j]):
            j -= 1

        k = i - 1
        while k >= j + 1:  #deplasare spre dreapta
           b[k+1]=b[k]
           k -= 1

        b[j+1]=sir[i]; # sir[i] se insereaza pe pozitia j+1

        i += 1
        
    return b
    
