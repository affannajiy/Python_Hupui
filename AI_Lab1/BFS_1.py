from collections import deque
'''
collection is a module for containers
deque is a double ended queue
Link: https://docs.python.org/3/library/collections.html
'''

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': ['G'],
  'E': ['G'],
  'F': ['G'],
  'G': [] #G is goal
}

#Breadth First Search
def bfs(graph, start, goal):
  queue = deque([[start]])
  while queue:
    path = queue.popleft() #popleft() removes the first element
    node = path[-1]
    if node == goal:
      return path
    for adjacent in graph.get(node, []): #import graph
      new_path = list(path)
      new_path.append(adjacent)
      queue.append(new_path)
  return None

print(bfs(graph, 'A', 'G')) 
#Output: ['A', 'B', 'D', 'G']