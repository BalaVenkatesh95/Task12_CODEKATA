N, K = map(int, input().split())
values = list(map(int, input().split()))
repeat_value = -1
for value in values:
    if value == K:
        repeat_value = repeat_value + 1
print(repeat_value)
