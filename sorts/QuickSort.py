def quickSort(v, st, dr):
    if st < dr:
        m = (st + dr) // 2 #pivotul este inițial v[st]
        aux = v[st]
        v[st] = v[m]
        v[m] = aux
        i = st
        j = dr
        d = 0
        while i < j:
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                d = 1 - d
            i += d
            j -= 1 - d
        quickSort(v, st , i - 1)
        quickSort(v, i + 1 , dr)
    return v