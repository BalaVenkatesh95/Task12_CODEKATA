A, B, C = map(int, input().split())
#triangle inequality theorem:To check sum of any 2 sides in greater than 3rd side

if A + B > C and B + C > A and C + A > B:
    print("yes")
else:
    print("no")