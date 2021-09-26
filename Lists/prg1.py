#Slicing Lists Function (Similar to strings)
#Functions : append, count, extend, index, 
#            insert, pop, remove, reverse, 
#            sort, extend, sum, min, max

demoList = [1, 2, 3, 4, 5, 7, 8, 9]
# print(demoList)
# print(demoList[2:5])
# print(demoList[2:5:2])
# print(demoList[::-1])

# print("Functions : ")
# demoList.insert(4, [1, 2, 3])
# print(demoList)
# demoList.pop()
# demoList.pop()
# demoList.pop()
# print(demoList)
# count = demoList.count(2)
# print(count)
# demoList.sort(reverse=True)
# print(demoList)
# employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]

# # custom functions to get employee info
# def get_name(employee):
#     return employee.get('Name')


# def get_age(employee):
#     return employee.get('age')


# def get_salary(employee):
#     return employee.get('salary')


# # sort by name (Ascending order)
# employees.sort(key=get_name)
# print(employees, end='\n\n')

# # sort by Age (Ascending order)
# employees.sort(key=get_age)
# print(employees, end='\n\n')

# # sort by salary (Descending order)
# employees.sort(key=get_salary, reverse=True)
# # print(employees, end='\n\n')
# numList = list()
# while True:
#     inp = (input('Enter a Number: '))
#     if inp == 'done': break
#     numList.append(float(inp))
# print(len(numList))
# print('Avg : ', (sum(numList)/(len(numList)+1)))
for i in range(7):
    print(i)