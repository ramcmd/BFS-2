# TC: O(m*n)
# SC: O(m*n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_count = 0
        
        m = len(grid)
        n = len(grid[0])
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        
        q = deque()
        time = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        while q:
            size = len(q)
            
            for _ in range(size):
                x,y = q.popleft()
                
                for dx,dy in dirs:
                    nr = dx + x
                    nc = dy + y
                    
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                        q.append([nr, nc])
                        fresh_count -= 1
                        grid[nr][nc] = 2
            
            if len(q) != 0:
                time += 1
        
        print(fresh_count)
        if fresh_count > 0:
            return -1
        else:
            return time 
                    
            
            
        