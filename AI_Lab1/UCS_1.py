import heapq
'''
hepq is a module for heap queue
heap queue is a priority queue
Link: https://docs.python.org/3/library/heapq.html
'''

graph = { #Node, Cost
  'A': [('B', 1), ('C', 4)],
  'B': [('D', 3), ('E', 2)],
  'C': [('F', 5)],
  'D': [('G', 4)],
  'E': [('G', 1)],
  'F': [('G', 2)],
  'G': [] #G is goal
}

def ucs(graph, start, goal):
  heap = [(0, [start])] #heap is a priority queue
  visited = set()

  while heap:
    (cost, path) = heapq.heappop(heap)
    node = path[-1]
    
    if node not in visited: #not in is used to check if the node is in the visited set
      visited.add(node) #adds the node to the visited set
      if node == goal:
        return path, cost #returns the path and cost
      for adjacent, weight in graph.get(node, []):
        new_path = list(path)
        new_path.append(adjacent)
        heapq.heappush(heap, (cost + weight, path + [adjacent])) 
  return None

path, cost = ucs(graph, 'A', 'G')
print(f"Path: {path}, Cost: {cost}") #parking lot method