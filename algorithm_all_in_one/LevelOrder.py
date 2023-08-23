
from collections import deque

def LevelOrder(root) :
    visited = []
    if root is None :
        return 0;
    
    q = deque()
    q.append(root)
    
    while q:
        # 노드 값 추가 : visited
        cur_node = q.popleft() # 방문했다고 판단함.
        visited.append(cur_node.value) # 노드 값에 값을 추가
        
        # 노드 주소값 추가 : q
        if cur_node.left: # cur_node에 left 주소값이 있다면,
            q.append(cur_node.left)
        if cur_node.right: # cur_node에 right 주소값이 있다면,
            q.append(cur_node.right)
    return visited

# LevelOrder(root)