import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    prev = 0
    curr_label = 1
    a = []
    for i in range(n):
        diff = b[i] - prev
        if diff > len(a):
            # Need to introduce new distinct numbers
            a.append(curr_label)
            curr_label += 1
        else:
            # Can reuse an earlier number
            a.append(a[-diff])
        prev = b[i]
    print(*a)
