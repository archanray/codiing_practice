def find_max(list1, list2) -> int:
	if len(list1) == 1:
		return list1[0]
	cost = 0
	n = len(list1)
	l1 = list1[0] + find_max(list1[1:], list2[1:])
	l2 = find_max(list2[1:], list1[1:])
	if l1 > l2:
		cost += l1
	else:
		cost += l2
	return cost

def TSP(list1, list2) -> int:
	return max(find_max(list1, list2), find_max(list2, list1))

print(TSP([12, 14, 15], [15, 1, 3]))
print(TSP([25, 1, 30, 12, 10], [10, 12, 3, 1, 200]))