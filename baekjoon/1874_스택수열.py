n = int(input())

st = list()
answer = list()
cursor = 1
isTrue = True
for i in range(n):
    # 입력값 확인
    val = int(input())
    # n까지 순서대로 입력
    while cursor <= val:
        answer.append("+")
        st.append(cursor)
        cursor += 1
    # pop되는 값과 입력값이 일치하면 pop 실행
    if st[-1] == val:
        st.pop()
        answer.append("-")
    # else case -> 수행 불가
    else:
        print("NO")
        isTrue = False
        break
if isTrue:
    for i in range(len(answer)):
        print(answer[i])
