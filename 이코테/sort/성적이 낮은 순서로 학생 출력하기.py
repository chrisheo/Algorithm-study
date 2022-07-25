N = int(input())

students = []
for i in range(N):
  input_data = input().split()
  students.append((input_data[0], input_data[1]))
students.sort(key= lambda x: x[1])
print(students)