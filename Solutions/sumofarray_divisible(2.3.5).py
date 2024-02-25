size = int(input())
values = list(map(int, input().split()))
sum = sum(values)

if sum % 2 == 0 and sum % 3 == 0 and sum % 5 == 0:
    print(1)
else:
    print(0)