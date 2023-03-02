def numarate(sir, n):
    aux = [] #vector auxilar
    for i in range(n + 1):
       aux.append(0)

    i = 1
    while i <= n:
      k = 0
      j = 1
      while j <= n:
          if sir[j] < sir[i]:
             k += 1
          j += 1
      aux[k+1] = sir[i] #il punem  pe a[i] in b pe pozitia k+1
      i += 1
    return aux
