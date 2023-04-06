N, M = map(int, input().split())
city = []
chicken_zip = []
for i in range(N):
    row = list(map(int, input().split(' ')))
    city.append(row)


def chicken_dist_calc(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def total_chicken_dist(city):
    for i in range(1, N+1):
        for j in range(1,N+1):
            if city[i][j] == 2:
                continue


