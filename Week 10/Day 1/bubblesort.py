def bubblesort(array): # n*n
    swapped = True
    length_to_loop = len(array)
    while swapped:
        swapped=False
        length_to_loop -= 1
        for i in range(length_to_loop):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                swapped=True


array = [6, 5, 12, 10, 9, 1]
bubblesort(array)
print(array)