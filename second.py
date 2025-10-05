#question 1: write the program to input student name and marks of three subject 
# print name and percentage in out put
student = input("enter the name: ")
math = input("enter the math marks: ")
hindi = input("enter the hindi marks: ")
english = input("enter the english marks: ")
percentage=((int(math)+int(hindi)+int(english)/300))*100
print(f"my {student} total {percentage} in this subject")

# question 2:write a program that collects multiple type of data to store in a
        #    dictionary and print out put
user_data = {}
user_data['name']=input("enter the name: ")
user_data['math']=input("enter the math: ")
user_data['hindi']=input("enter the hindi: ")
user_data['english']=input("enter the english: ")

print(user_data)