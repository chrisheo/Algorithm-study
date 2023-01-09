from sys import stdin

n = int(stdin.readline())
lengths = list(map(int, stdin.readline().split()))
prices = list(map(int, stdin.readline().split()))

# 다음 주유소의 가격이 현재 주유소 가격보다 높으면 현재에 만땅 채우기
lowest_price = prices[0]
cost = prices[0] * lengths[0]
for i in range(1, n - 1):
    if prices[i] < lowest_price:
        lowest_price = prices[i]

    cost += lowest_price * lengths[i]
print(cost)


