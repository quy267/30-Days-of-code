def is_pseudo_forest(n, wmap):
    N = 100000
    graph = [[] for i in range(N)]
    cycles = [[] for i in range(N)]
    cyclenumber = 0

    def dfs_cycle(u, p, color: list, mark: list, par: list):
        nonlocal cyclenumber
        if color[u] == 2:
            return

        if color[u] == 1:
            cyclenumber += 1
            cur = p
            mark[cur] = cyclenumber

            while cur != u:
                cur = par[cur]
                mark[cur] = cyclenumber

            return

        par[u] = p

        color[u] = 1

        for v in graph[u]:

            if v == par[u]:
                continue
            dfs_cycle(v, u, color, mark, par)

        color[u] = 2

    for element in wmap:
        graph[element[0]].append(element[1])
        graph[element[1]].append(element[0])

    color = [0] * N
    par = [0] * N
    mark = [0] * N

    dfs_cycle(1, 0, color, mark, par)

    return cyclenumber <= 1


if __name__ == '__main__':
    print(is_pseudo_forest(n=7, wmap=[[0, 1], [1, 2], [2, 3], [3, 1], [3, 4], [5, 6]]))
