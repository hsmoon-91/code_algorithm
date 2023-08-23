
from collections import deque

def LevelOrder(root) :
    visited = []
    if root is None :
        return 0;
    
    q = deque()
    q.append(root)
    
    while q:
        # 노드 값 추가 : visited
        cur_node = q.popleft()
        visited.append(cur_node.value)
        
        # 노드 주소값 추가 : q
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

# LevelOrder(root)