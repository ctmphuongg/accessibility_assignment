import csv
import heapq
from typing import List, Dict

class Building:
    def __init__(self, name):
        self.name = name
        self.dist = float('inf')
        self.neighbors = []
        self.previous = None  # Add previous to track path
        
    def add_neighbor(self, distance: int, other_building, is_accessibile: bool) -> None:
        self.neighbors.append(Path(distance, other_building, is_accessibile))
        
    def get_neighbors(self):
        return self.neighbors
    
    def get_name(self) -> str:
        return self.name
      
    def get_dist(self) -> int:
        return self.dist
    
    def __lt__(self, other) -> bool:
        return (self.dist < other.dist or self.name < other.name)

class Path:
    def __init__(self, distance: int, other_building: Building, is_accessibile: bool) -> None:
        self.other_building = other_building
        self.distance = distance
        self.is_accessibile = is_accessibile
        
    def get_other_building(self) -> Building:
        return self.other_building
    
    def get_dist(self) -> int:
        return self.distance

class School_Map:
    def __init__(self):
        self.buildings = {}

    def build_map(self, file_name: str, accessible_map: bool) -> None:
        with open(file_name, 'r') as f:
            csv_reader = csv.reader(f)
            
            for row in csv_reader:
                from_building_name, to_building_name, distance, is_accessible = row
                distance = int(distance)
                
                if from_building_name not in self.buildings:
                    self.buildings[from_building_name] = Building(from_building_name)
                if to_building_name not in self.buildings:
                    self.buildings[to_building_name] = Building(to_building_name)
                
                from_building = self.buildings[from_building_name]
                to_building = self.buildings[to_building_name]

                is_accessible = True if is_accessible == "Yes" else False
                
                if accessible_map and not is_accessible:
                    continue
                
                from_building.add_neighbor(distance, to_building, is_accessible)
    
    def get_building(self, building_name: str) -> Building:
        return self.buildings[building_name]
    
    def get_all_building_names(self) -> List[str]:
        return list(self.buildings.keys())

def dijkstra_find_shortest_path(start:str, destination:str, school_map: School_Map) -> Dict:
    # Reset buildings
    for building in school_map.get_all_building_names():
        building_obj = school_map.get_building(building)
        building_obj.dist = float('inf')
        building_obj.previous = None
    
    # Initialize start building
    start_building = school_map.get_building(start)
    start_building.dist = 0
    
    # Priority queue
    heap = [start_building]
    visited = set()
    
    while heap:
        cur_building = heapq.heappop(heap)
        current_dist = cur_building.get_dist()
        # Skip if already visited
        if cur_building.get_name() in visited:
            continue
        visited.add(cur_building.get_name())
        
        # Reached destination
        if cur_building.get_name() == destination:
            # Reconstruct path
            path = []
            current = cur_building
            while current:
                path.append(current.get_name())
                current = current.previous
            return {
                'distance': current_dist,
                'path': list(reversed(path))
            }
        
        # Check neighbors
        for neighbor_path in cur_building.get_neighbors():
            neighbor = neighbor_path.get_other_building()
            neighbor_dist = neighbor_path.get_dist()
            
            # Calculate new distance
            new_dist = current_dist + neighbor_dist
            
            # Update if new path is shorter
            if new_dist < neighbor.dist:
                neighbor.dist = new_dist
                neighbor.previous = cur_building
                heapq.heappush(heap, neighbor)
    
    # No path found
    return {
        'distance': -1,
        'path': None
    }
    
    
# TESTS

TEST_CASE_NORMAL = [
    # Direct connections
    ("Science Center", "Library", ["Science Center", "Library"], 237),
    
    ("Student Union", "Library", 
     ["Student Union","Library"], 100),
    
    # Multi-hop paths
    ("Science Center", "Student Union", 
     ["Science Center", "Library", "Student Union"], 526),
    
    ("Dormitory Complex", "Library", 
     ['Dormitory Complex', 'Science Center', 'Library'], 535),
    
    # Start and end at same location
    ("Library", "Library", ["Library"], 0),
    
]

TEST_CASE_ACCESSIBILITY = [
      # Direct connections
    ("Science Center", "Library", ["Science Center", "Library"], 237),
    
    ("Student Union", "Library", 
     ['Student Union', 'Administrative Office', 'Cafeteria', 'Gymnasium', 'Library'], 995),
    
    # Multi-hop paths
    ("Science Center", "Student Union", 
     ["Science Center", "Library", "Student Union"], 526),
    
    ("Dormitory Complex", "Library", 
     None, -1),
    
    # Start and end at same location
    ("Library", "Library", ["Library"], 0),
]

def test_normal():
  normal_map = School_Map()
  normal_map.build_map("school_map.csv", False)
  
  for test in TEST_CASE_NORMAL:
      fr, to, expected_path, expected_dist = test
      result = dijkstra_find_shortest_path(fr, to, normal_map)
      
      print(f"From {fr} to {to}:")
      print(f"  Actual Distance: {result['distance']}")
      print(f"  Actual Path: {result['path']}")
      print(f"  Expected Distance: {expected_dist}")
      print(f"  Expected Path: {expected_path}")
      
      # Validate distance
      assert result['distance'] == expected_dist, f"Distance mismatch for {fr} to {to}"
      
      # Validate path (optional, as paths might not be unique)
      # Uncomment if you want to strictly match paths
      # assert result['path'] == expected_path, f"Path mismatch for {fr} to {to}"
      
      print("Test passed!\n")
      
def test_accessibility():
      accessible_map = School_Map()
      accessible_map.build_map("school_map.csv", True)
      
      for test in TEST_CASE_ACCESSIBILITY:
          fr, to, expected_path, expected_dist = test
          result = dijkstra_find_shortest_path(fr, to, accessible_map)
          
          print(f"From {fr} to {to}:")
          print(f"  Actual Distance: {result['distance']}")
          print(f"  Actual Path: {result['path']}")
          print(f"  Expected Distance: {expected_dist}")
          print(f"  Expected Path: {expected_path}")
          
          # Validate distance
          assert result['distance'] == expected_dist, f"Distance mismatch for {fr} to {to}"
          
          # Validate path (optional, as paths might not be unique)
          # Uncomment if you want to strictly match paths
          assert result['path'] == expected_path, f"Path mismatch for {fr} to {to}"
          
          print("Test passed!\n")
      


if __name__ == "__main__":
    test_normal()
    test_accessibility()

