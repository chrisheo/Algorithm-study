num = int(input("숫자를 입력해주세요 :"))
lst = []
for i in range(num):
    word = input()
    lst.append(word)

lst_set = set(lst)
lst.clear()
for i in lst_set:
    length = len(i)
    word_lst = [i, length]
    lst.append(word_lst)


for i in range(0, len(lst)-1):
    small = i
    for j in range(i+1, len(lst)):
        if lst[small][1] > lst[j][1]:
            small = j
    if i != small:
        temp = lst[small]
        lst[small] = lst[i]
        lst[i] = temp

lst.sort()
for i in range(0, len(lst)):
    print(lst[i][0])


