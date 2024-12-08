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
        # TO IMPLEMENT
        pass
    
    def get_building(self, building_name: str) -> Building:
        return self.buildings[building_name]
    
    def get_all_building_names(self) -> List[str]:
        return list(self.buildings.keys())

def dijkstra_find_shortest_path(start:str, destination:str, school_map: School_Map) -> Dict:
    # TO IMPLEMENT
    pass
    
    
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

