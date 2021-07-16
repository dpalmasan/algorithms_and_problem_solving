t = int(input())

for i, _ in enumerate(range(t)):
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    for j in range(2, n):
        if a[j] == a[j - 1] == a[j - 2] or found:
            continue
        if a[j] == a[j - 2]:
            print(j)
        elif a[j] == a[j - 1]:
            print(j - 1)
        else:
            print(j + 1)
        found = True
