from collections import deque

def bfs(root):
  visited = []
  if root is None:
    return 0

  q = deque()
  # q에는 노드의 주소값을 저장
  q.append(root)

  while q:
    cur_node = q.popleft()
    # visited 에는 노드의 값을 저장, 방문완료
    visited.append(cur_node.value)

    if cur_node.left:
      # q에 노드의 주소값을 저장하여 방문예약
      q.append(cur_node.left)
    if cur_node.right:
      q.append(cur_node.right)

  return visited
###