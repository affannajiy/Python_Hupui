import heapq

grid = [
  [1, 1, 1, 99, 1],
  [99, 99, 1, 99, 1],
  [1, 1, 1, 1, 1],
  [1, 99, 99, 99, 1],
  [1, 1, 1, 1, 1]
]  # 1 = safe, 99 = trap

def ucs(grid, start, goal):
  rows = len(grid)
  cols = len(grid[0]) if rows > 0 else 0
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    
  #Priority queue: (total_cost, path)
  #Path is list of coordinates [(x1,y1), (x2,y2), ...]
  heap = [(0, [start])]
  visited = set()
    
  while heap:
    total_cost, path = heapq.heappop(heap)
    current = path[-1]  #Get last position in path
        
    if current == goal:
      return path, total_cost
        
    if current in visited:
      continue
            
    visited.add(current)
        
    for dx, dy in directions:
      x, y = current
      new_x, new_y = x + dx, y + dy 
            
       #Check boundaries and avoid traps
      if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != 99:
        new_pos = (new_x, new_y)
        if new_pos not in path:  #Prevent cycles
          new_path = path + [new_pos]
          new_cost = total_cost + grid[new_x][new_y]
          heapq.heappush(heap, (new_cost, new_path))
  return None

start = (0, 0)
goal = (4, 4)

path, cost = ucs(grid, start, goal)
print(f"Path: {path}")
print(f"Cost: {cost}")