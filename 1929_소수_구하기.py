#M이상 N이하의 소수를 모두 출력하는 프로그램 작성, 에라스토테네스의 체
M, N = input().split()

M, N = int(M), int(N)


def checkPrime(n):
    if n == 1:
      return False
    else:
      for i in range(2, int(n**0.5) + 1):
        if n % i ==0:
          return False
      return True


for i in range(M, N+1):
  if checkPrime(i):
    print(i)
