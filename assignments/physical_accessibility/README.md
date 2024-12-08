# Accessibility Assessment of School Map

## Overview

This project involves analyzing the accessibility of a school map by implementing a series of computational tasks. The main objectives are to construct a graph representation of the school map, calculate the shortest paths between buildings, and evaluate whether the school meets accessibility standards. The analysis focuses on comparing accessible and normal routes, identifying potential violations of accessibility standards.

## Project Objectives

1. **Build the School Map**:

   - Parse data from a CSV file to construct a graph where nodes represent buildings and edges represent paths between them.
   - Include an accessible-only mode to filter and analyze wheelchair-friendly paths.

2. **Implement Shortest Path Algorithm**:

   - Write Dijkstra’s algorithm to calculate the shortest path between two buildings.
   - Ensure the implementation works for both normal and accessible maps.

3. **Accessibility Evaluation**:
   - Compare the shortest paths between two buildings using normal and accessible paths.
   - If the difference in path lengths exceeds 200 units, report that the school violates accessibility standards.

## Introduction

Accessibility is a critical factor in designing inclusive spaces, ensuring that all individuals, regardless of physical ability, can navigate and utilize facilities with ease. This assignment is designed to provide hands-on experience in assessing the accessibility of a school map. By leveraging computational techniques, you will analyze the school’s infrastructure to determine whether it adheres to accessibility standards.

The task involves building a graph representation of the school map, where nodes correspond to buildings, and edges represent paths between them. Each path will have associated attributes, such as distance and accessibility status. Using this graph, you will implement Dijkstra's shortest-path algorithm to calculate the shortest routes between buildings. The paths will then be analyzed to compare the normal (standard) routes with those specifically designated as accessible.

Finally, you will evaluate the school’s compliance with accessibility standards. Specifically, you will compare the path lengths for accessible and normal routes. If the difference between the two exceeds a threshold (200 units in this case), it may indicate a potential violation of accessibility standards, highlighting areas that require improvement.

This assignment will deepen your understanding of graph algorithms, accessibility considerations, and the importance of data-driven approaches in assessing real-world infrastructure. You will also develop skills in programming, problem-solving, and report generation, culminating in a comprehensive evaluation of the school map’s accessibility.

## Instructions

### Part 1: Build the School Map

1. **Function to Implement**: `build_map`
   - Read data from a provided CSV file containing information about buildings and paths.
   - Use the data to construct a graph representation of the school map.
   - Each node represents a building, and each edge represents a path between buildings with associated weights (e.g., distance).
2. **Accessible Map Attribute**: Add functionality to create an accessible-only version of the map.
   - Include paths that are wheelchair-friendly, avoiding stairs or inaccessible areas.
   - This version should be a filtered subset of the main map.

**Guide**:

- Study how CSV files are parsed in Python using `csv.reader` or pandas.
- Research graph representation techniques (e.g., adjacency list or matrix).
- Create a clear distinction between normal paths and accessible paths.

### Part 2: Dijkstra’s Shortest Path Algorithm

1. **Function to Implement**: `shortest_path`
   - Write a function to compute the shortest path between two buildings using Dijkstra’s algorithm.
   - Return the path length and the sequence of nodes for the route.

**Guide**:

- Revise Dijkstra’s algorithm, focusing on priority queues (e.g., using `heapq` in Python).
- Test with sample graphs to ensure accuracy.
- Make your function modular so it can work for both normal and accessible maps.

### Part 3: Accessibility Analysis

1. Compare the shortest paths between two buildings:
   - Compute paths using the normal map and the accessible map.
2. For each test case:

   - Calculate the difference in path length.
   - Determine if the difference exceeds 200 units (a violation of accessibility standards).

3. **Output**:
   - A report summarizing the differences for all test cases.
   - Highlight buildings or pairs of buildings that violate accessibility standards.

**Guide**:

- Prepare a list of test cases (pairs of buildings to test).
- Automate the comparison process with a function.
- Structure the report for clarity:
  - Include the building pairs, path lengths, differences, and compliance status.

## Deliverables

1. Python script with the following implemented:
   - `build_map` function (Part 1)
   - `shortest_path` function (Part 2)
   - Accessibility comparison logic (Part 3)
2. A report file (e.g., Markdown or plain text) containing:
   - Description of your approach for each part.
   - The comparison table for test cases and conclusions on accessibility compliance.

## Resources

- Python libraries: `csv`, `heapq`, `pandas` (optional).
- Concepts: Graph representations, shortest-path algorithms, file parsing.
- Refer to the sample CSV format provided in the assignment.

## Evaluation Criteria

1. **Correctness**: Does your code produce the expected results for all test cases?
2. **Code Quality**: Is your code well-organized, commented, and modular?
3. **Report**: Does your report clearly communicate the results and insights from the analysis?

## Sample CSV Format

```csv
source,destination,weight,accessible
A,B,150,True
B,C,100,False
A,C,300,True
```
