from typing import List


class Solution:
    def getManhattanDistance(self, x,y,a,b):
        return abs(x - a) + abs(y - b)

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_points = []
        for i in points:
            if i[0] == x or i[1] == y:
                valid_points.append(i)
        if len(valid_points) > 0:
            min_Man_distance = 100000
            min_dist_index = 0
            for i in range(len(valid_points)):
                dist = self.getManhattanDistance(x,y,valid_points[i][0],valid_points[i][1])
                if dist < min_Man_distance:
                    min_Man_distance = dist
                    min_dist_index = i
            return points.index(valid_points[min_dist_index])
        else:
            return -1
