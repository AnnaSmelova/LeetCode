class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh_cnt = 0

        rotten = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1

        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
                    
        return minutes_passed if fresh_cnt == 0 else -1
        