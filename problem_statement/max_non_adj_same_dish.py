def count_pick(pos):
    ans = 0
    run = 1

    for i in range(1, len(pos)):
        if pos[i] == pos[i - 1] + 1:
            run += 1
        else:
            ans += (run + 1) // 2
            run = 1

    ans += (run + 1) // 2
    return ans


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    mp = {}

    for i in range(N):
        if A[i] not in mp:
            mp[A[i]] = []
        mp[A[i]].append(i)

    best_type = -1
    best_count = -1

    for x in mp:
        cnt = count_pick(mp[x])

        if cnt > best_count:
            best_count = cnt
            best_type = x
        elif cnt == best_count and x < best_type:
            best_type = x

    print(best_type)
