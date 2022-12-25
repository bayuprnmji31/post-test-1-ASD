import os
os.system("cls")

def quicksort(y, kiri, kanan):
    if kiri < kanan:
        partition_tempat = partition(y, kiri, kanan)
        quicksort(y, kiri, partition_tempat - 1)
        quicksort(y, partition_tempat + 1, kanan)

def partition(y, kiri, kanan):
    a = kiri
    b = kanan - 1
    pivot = y[kanan]


    while a < b:
        while a < kanan and y[a] < pivot:
            a += 1

        while b > kiri and y[b] >= pivot:
            b -= 1

        if a < b:
            y[a], y[b] = y[b], y[a]

    if y[a] > pivot:
        y[a], y[kanan] = y[kanan], y[a]

    return a


def perubah(list1):
    result=[]
    for y in list1:
        if isinstance(y,list):
            for i in y:
                if isinstance(i,list):
                    for a in i :
                        result.append(int(a))
                elif isinstance(i, int):
                    result.append(i)
        else:
            result.append(y)
    return result



y =[12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
print("Sebelum melakukan sorting         :", y)
pr=perubah(y)
print("Proses perubahan                  :",pr)
quicksort(pr, 0, len(pr) -1 )
print("Setelah melakukan sorting (hasil) :", pr)


