#list of example.
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))  #variable for datatype
print(marks[0])  #list of index
print(marks[4])  #list of index

#new example.
#string and int both are add for list.
student=["bhaumik",66,"chirag",78]
print(student)
print(student[0])
student[0] = "krishi"
print(student)
print(student[3])


#list slicing.
marks=[66,78,54,89,91,94,54]
print(marks[0: 4]) #0 is a start index and 4 is a end index.but python are not add for last index.
print(marks[: 5]) #start index value for not define of by default to 0 start index.
print(marks[2 :]) #start index for 0 and end index is not define by this time by default count to last index.
print(marks[0: 7 :2]) #python by defualt jump for 1 index.and 2 define are to python instrction for jump is 2 index.

#list methods.
list=[2, 1, 3]
list.append(4) #adds one element at the end.
print(list)
print(list.sort()) #sort in ascending order. exmple 1,2,3,4.
print(list)
print(list.sort(reverse=True)) #sort descending order. example 4,3,2,1.
print(list)
list.reverse() #orignal list are reverse.
print(list)
list.insert(2,6) #insert element at index.
print(list)
list.remove(1) # 1 value for a remove.
print(list)
list.pop() # not enter to index for this method for by default last index to remove.
print(list) 
list.pop(1) # enter index to remove.
print(list)