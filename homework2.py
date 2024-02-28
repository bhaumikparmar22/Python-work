movies=[]
movie1=input("Enter a first movie: ")
movie2=input("Enter a second movie: ")
movie3=input("Enter a third movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies) 


#list contains a palindrome of elements.(hint: use copy()method)
list1=["m", "a", "a", "m"]


copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")    


#write a program to count the number of students with the "A" grade in the following tuple.
grade = ("A", "C", "C", "B", "A", "A", "B")
print(grade.count("A"))        


#store the above values in a list & sort them from "A" to "D".
grade = ["A", "C", "C", "B", "A", "A", "B"]
grade.sort()
print(grade)