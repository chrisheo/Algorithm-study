N = input()
lenN = len(N)
box = ''
for i in range(1, int(N)+1):
    box = box + str(i)
cnt = 0
while cnt < len(box) - lenN+1:
    buf = box[cnt:cnt + lenN]
    
    if buf == N:
        print(cnt + 1)
        break
    else:
        cnt +=1