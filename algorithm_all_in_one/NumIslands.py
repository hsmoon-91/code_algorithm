from collections import deque

def numIslands(grid):
    
    number_of_islands = 0
    
    row = len(grid)
    col = len(grid[0])
    visited = [[False]*col for _ in range(row)]
    
    def bfs(x,y):
        
        # 상하좌우 
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        visited[x][y] = True
        queue = deque()
        while queue:
            cur_x, cur_y = queue.pop()
            # 상하좌우 모두 방문
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if next_x >= 0 and next_x < col and next_y >= 0 and next_y < row:
                    if grid[next_x,next_y] == '1' and not visited[next_x,next_y]:
                         
                        visited[next_x][next_y] = True
                        queue.append((next_x,next_y))
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i,j)
                number_of_islands += 1
                   
    
    return number_of_islands




val = numIslands(grid=[
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
])
print(val)