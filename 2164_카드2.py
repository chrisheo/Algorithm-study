from collections import deque
N = int(input())

q = deque([])
for i in range(1, N + 1):
    q.append(i)
j = 0
while len(q) > 1:

    if j % 2 == 0:
        q.popleft()
    else:
        q.append(q.popleft())
    j += 1
print(q[0])
