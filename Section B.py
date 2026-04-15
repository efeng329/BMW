import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * (n + 1)
        subtree = [0] * (n + 1)

        def dfs(u, p):
            parent[u] = p
            subtree[u] = 1

            for v in graph[u]:
                if v == p:
                    continue
                dfs(v, u)
                subtree[u] += subtree[v]

        dfs(1, 0)

        limit = n - k
        total = 0

        for node in range(1, n + 1):
            bad_sum = 0

            for nxt in graph[node]:
                if nxt == parent[node]:
                    continue

                size = subtree[nxt]
                if size > limit:
                    bad_sum += size

            if parent[node] != 0:
                size = n - subtree[node]
                if size > limit:
                    bad_sum += size

            good_roots = n - bad_sum
            total += good_roots

        print(total)


if __name__ == "__main__":
    solve()
