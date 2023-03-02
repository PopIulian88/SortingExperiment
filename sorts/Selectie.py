def selectie(sir, n):
    i = 1
    while(i < n): 
        mi = sir[i]
        k = i  #selectam pozitia minimului,k, dintre toate elem
        j = i + 1
        while j <= n:        #de la pozitia i pana la sf
            if sir[j] < mi: #mutam minimul,a[k], pe pozitia i
                mi = sir[j]
                k = j 
            j += 1
        aux = sir[i]
        sir[i] = sir[k]
        sir[k] = aux
        i += 1

    return sir
