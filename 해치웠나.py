def main():
    x = input()
    stack = []
    #only pop or push
    stack.append(x[0])
    for i in range(1,len(x)):
      if stack:
        if stack[-1] != x[i]:
          stack.pop()
        else:
          stack.append(x[i])
      else:
        stack.append(x[i])
    if stack:
        print("NO")
    else:
        print("YES")


if __name__=="__main__":
    main()