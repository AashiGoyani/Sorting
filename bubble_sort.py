def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(0, len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]  #swapping if the element is greater than the next element
    return list1
    
list1 = [5,12,19,8,2,20]
print(bubble_sort(list1))
