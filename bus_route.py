# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
import collections
class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        stop_to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        visited = set()
        queue = collections.deque([(source, 0)])
        while queue:
            stop, buses = queue.popleft()
            if stop == target:
                return buses
            for route in stop_to_routes[stop]:
                if route in visited:
                    continue
                visited.add(route)
                for next_stop in routes[route]:
                    if next_stop != stop:
                        queue.append((next_stop, buses + 1))
        return -1

inputs = [[1,2,7],[3,6,7]]
source = 1
target = 6
s = Solution()
print(s.numBusesToDestination(inputs, source, target)) # 2