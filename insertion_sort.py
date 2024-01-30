def insertion_sort(list1):
    for i in range(1,len(list1)):
        value = list1[i]              #value is the value of the current element
        j = i-1                      
        while j>0 and value < list1[j]:
            list1[j+1] = list1[j]
            j = j-1
        list1[j+1] = value

list1 = [5,12,19,8,2,20]
insertion_sort(list1)
print(list1)