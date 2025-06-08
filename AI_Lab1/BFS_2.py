from collections import deque
'''
collection is a module for containers
deque is a double ended queue
Link: https://docs.python.org/3/library/collections.html
'''

maze = [
    ['S', '.', '.', '#', 'G'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.']
]

#Breadth First Search
def bfs(maze):
  start, goal = None, None
  for i in range(len(maze)):
    for j in range(len(maze[0])):
      if maze[i][j] == 'S':
        start = (i, j)
      if maze[i][j] == 'G':
        goal = (i, j)
  
  queue = deque([[start]])
  visited = set()

  def valid(x, y): #for valid path
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] != '#':
        yield (nx, ny)
  
  while queue:
    path = queue.popleft()
    x, y = path[-1]
    if (x, y) == goal:
      return path
    for nx, ny in valid(x, y):
      if (nx, ny) not in visited:
        visited.add((nx, ny))
        queue.append(path + [(nx, ny)])
  return None

print(bfs(maze))