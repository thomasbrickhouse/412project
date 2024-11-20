# run minimum spanning tree on same inputs and compare for analysis
# MST = Lower bound helps to estimate final answer between approximate

# Heres what I need to present:
    # why MST is a good lower bound for TSP
    # convince Malloy that MST is polynomial time computable
    # showcase the lower bound, optimal, approximate exist --> test cases
    # run all of these on something the optimal cannot complete --> plot on graph

# Lab 10 MST code: # https://canvas.jmu.edu/courses/2035607/assignments/18443313

# TSP MST Implementation: 
    # add lightest edge thats not in the minimum spanning tree to the graph after 
        # you run the code to complete the tour
    # May need to change code to make it so that it doesnt backtrack
def main():
    # your code here
    n = int(input())
    stops = {}
    for _ in range(n):
        k,v = input().split()
        if k not in stops:
            stops[k] = set()
        stops[k].add(v)

        if v not in stops:
            stops[v] = set()
        stops[v].add(k)
        
    query = input().split()
    # print(n)
    # print(stops)
    # print(query)
    visited = set()
    current_path = []
    DFS = search(query[0], query[1], stops, visited, current_path)
    if not DFS:
        print("no route possible")
    pass

def search(location, destination, routes, visited, path):
    # Keep track of path and visited locations
    visited.add(location)
    path.append(location)

    # Base Cases:
    # If the current location is the same as the destination, path found
    if location == destination:
        print(' '.join(path))
        return True 

    # Explore neighboring routes
    for route in routes[location]:
        if route not in visited: # Keep going
            if search(route, destination, routes, visited, path): # Check path
                return True # Path found
            
    path.pop() # Backtrack

    if location not in path: # Unconnected graph so no path possible
        return False
    pass

if __name__ == "__main__":
    main()
