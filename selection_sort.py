def selection_sort(list1):
    for i in range(len(list1)):
        min_value = i
        for j in range (1+1,len(list1)):
            if list1[j] < list1[i]:
                min_value = j
        list1[i] , list1[min_value] = list1[min_value], list1[i]     #swapping minimum value with the first value in list

list1 = [5,12,19,8,2,20]
selection_sort(list1)
print(list1)

