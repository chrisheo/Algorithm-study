def solution(array, commands):
    answer = []
    print(array, commands)
    for i in range(len(commands)):
      i, j, k = commands[i]
      tempArray = array[i:j]
      tempArray.sort()
      answer.append(tempArray[k])
    return answer

if __name__=="__main__":
    array, commands = input()
    solution(array, commands)
