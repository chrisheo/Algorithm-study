N = int(input())
List = list(map(int,input().split()))

temp = [List[0]]
for i in range(len(List) - 1):
  temp.append(max(temp[i] + List[i + 1], List[i + 1]))
print(max(temp))