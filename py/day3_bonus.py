# Run with `cat day3.in.txt | py day3.py`
import sys

def find_shortest_combined_intersections(intersections, paths):
    shortest = sys.maxsize
    for intersection in intersections:
        distance = 0
        for path in paths:
            for coord in path:
                distance += 1
                if coord == intersection:
                    break

        if distance < shortest:
            shortest = distance

    return shortest

def find_shortest_intersection(intersections):
    magnitudes = [abs(c[0]) + abs(c[1]) for c in intersections]
    magnitudes.sort()
    return magnitudes[0]

def find_intersections(paths):
    return set(paths[0]).intersection(*paths)

def trace_wire(input):
    coordinates = [(0,0)]

    for direction in input.split(','):
        magnitude = int(direction[1:])
        current = (coordinates[-1])
        if direction[0] in ['R', 'L', 'U', 'D']:
            if direction[0] in ['R', 'L']:
                mod = 1 if direction[0] == 'R' else -1
                for num in range(1, magnitude + 1):
                    coordinates.append((current[0] + mod * num, current[1]))
            else:
                mod = 1 if direction[0] == 'U' else -1
                for num in range(1, magnitude + 1):
                    coordinates.append((current[0], current[1] + mod * num))        
        else:
            raise Exception("Unrecognised direction {}".format(direction[0]))    

    return coordinates[1:]

def parse_input():
    #with open('D:\\source\\personal\\AdventOfCode\\2019\\day3.in.txt') as fd:
     #   return [line for line in fd]
    return [line for line in sys.stdin]

if __name__ == "__main__":
    paths = parse_input()
    wire_paths = []

    for path in paths:
        wire_paths.append(trace_wire(path))

    intersections = list(find_intersections(wire_paths))
    print("Find {} intersections".format(len(intersections)))
    print("Intersections: \n{}".format('\n'.join([str(i) for i in intersections])))
    shortest = find_shortest_intersection(intersections)
    print("Shortest distance to intersection = {}".format(shortest))

    shorted_combined = find_shortest_combined_intersections(intersections, wire_paths)
    print("Shortest combined distance = {}".format(shorted_combined))