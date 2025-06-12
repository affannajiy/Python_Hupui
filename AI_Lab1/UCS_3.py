import heapq

graph = {
  'A': [('B', 2), ('C', 5)],
  'B': [('A', 2), ('D', 1)],
  'C': [('A', 5), ('D', 2)],
  'D': [('B', 1), ('C', 2), ('G', 3)],
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
print(f"Path: {path}, Cost: {cost}")