from collections import deque

# canVisitAllRooms
def keysandRooms(rooms=[]):
    
    # 리스트를 쓸지, 해쉬테이블을 쓸지, 딕셔너리를 쓸지
    visited = []


    def dfs(cur_v = 0):
        
        visited.append(cur_v)
        
        for next_v in rooms[cur_v]:
            if next_v not in visited:
                dfs(next_v)            
    
    dfs(0)
    
    
    
   
rooms = [[1,3],[2,4],[0],[4],[],[3,4]],
answer = keysandRooms(rooms) 
print(answer)
    