from collections import defaultdict, deque

# We will be using deque for efficient bfs
def find_paths(cave_map, can_visit_twice=False):
    # Create a dictionary to represent the graph
    graph = defaultdict(list)
    for connection in cave_map:
        cave1, cave2 = connection.split("-") 
        graph[cave1].append(cave2)
        graph[cave2].append(cave1)
    # Initialize a deque for BFS
    q = deque([("start", set(["start"]), False)])
    counter = 0

    while q:
        current_cave, seen, visited = q.popleft()
        # If we reach the end cave, increment the path counter
        if current_cave == "end":
            counter += 1
            continue
        # Iterate over neighboring caves connected to the current cave    
        for next_cave in graph[current_cave]:
            seen_cp = set(seen)
            # If the neighboring cave is a small cave (lowercase), add it to the 'seen' set
            if next_cave.islower():
                # Add the neighboring cave to the deque for further exploration
                seen_cp.add(next_cave)
            # Check if we haven't seen the next cave before
            if next_cave not in seen:
                q.append((next_cave, seen_cp, visited))
            # If we've seen the next cave, and it's not visited, and we can visit it twice, add it to the deque
            elif next_cave in seen and not visited and next_cave not in ["start", "end"] and can_visit_twice:
                q.append((next_cave, seen, next_cave))
    return counter


def convert_text_to_cave_map(text):
    lines = text.strip().split("\n")
    cave_map = []

    for line in lines:
        cave1, cave2 = line.split("-")
        cave_map.append(f"{cave1}-{cave2}")
    return cave_map


if __name__ == "__main__":
    cave_map = convert_text_to_cave_map(open("day12_input.txt",'r').read())

    all_paths_count = find_paths(cave_map, True)

    print("Total paths:", all_paths_count)
