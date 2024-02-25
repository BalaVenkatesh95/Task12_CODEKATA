size = int(input())
values = list(map(int, input().split()))
min_value = min(values)
max_value = max(values)
min_value_index = values.index(min_value) + 1
max_value_index = values.index(max_value) + 1
print(min_value_index, max_value_index)
