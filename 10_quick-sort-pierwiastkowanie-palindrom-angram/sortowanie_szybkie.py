tab = [8, 2, 1, 9, 5]

def split(tab, start, end):
    pivot = tab[end]
    low = start
    high = end - 1

    while True:
        while low <= high and tab[low] <= pivot:
            low += 1

        while low <= high and tab[high] >= pivot:
            high -= 1

        if low <= high:
            tmp = tab[low]
            tab[low] = tab[high]
            tab[high] = tmp
        else:
            break
    tmp = tab[end]
    tab[end] = tab[low]
    tab[low] = tmp

    return low

def quickSort(tab, start, end):
    if start < end:
        pivot = split(tab, start, end)
        quickSort(tab, start, pivot - 1)
        quickSort(tab, pivot + 1, end)
        print(tab)

quickSort(tab, 0, len(tab) - 1)
print(tab)