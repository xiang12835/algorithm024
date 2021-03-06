class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di, x, y = 0, 0, 0
        distance = 0
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2: # 向左转 90 度
                di = (di + 3)%4
            elif com == -1: # 向右转 90 度
                di = (di + 1)%4
            else:
                for j in range(com):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    if (next_x, next_y) in obs_dict: # 遇到障碍物
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance