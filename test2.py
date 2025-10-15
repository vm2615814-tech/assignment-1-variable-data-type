#  question 1: create dictionary using curly braces
# vivek= {'course':'b tech','age':37,'name':'vivek'}
# print(vivek)
# print(type(vivek))

# question 2: using list of tuples

# man=dict([('name','vivek'),('age',20),('city','agra')])
# print(man)
# print(type(man))

# question 3: add value in dict 
# student={
#         1:'class 2',
#         'name':'vivek',
#         'grade':'a',
#         'city':'agra'
#          }
# student['om']='namah shivaya'
# print(student)

# nested dictionary
# dict can contain other dict which is useful for storing more complex data 
student={
    "student1":{
        1:'class 2',
        'name':'vivek',
        'grade':'a',
        'city':'agra'
         },

    "student2":{
        1:'class 2',
        'name':'om',
        'grade':'b',
        'city':'omn'
         }
}
print(student["student1"]["name"])