class UnionFind:
    def __init__(self, size):
        # Инициализация массива родительских узлов и рангов
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, p):
        # Поиск корня компоненты, к которой принадлежит элемент p
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # ранжирование (path compression)
        return self.parent[p]

    def union(self, p, q):
        # Объединение компонент p и q
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:  # только если корни разные
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        # Проверка, соединены ли компоненты p и q
        return self.find(p) == self.find(q)

# Пример использования
uf = UnionFind(10)

# Объединяем 1 и 2
uf.union(1, 2)
print(uf.connected(1, 2))  # True

# Объединяем 2 и 3
uf.union(2, 3)
print(uf.connected(1, 3))  # True

# Проверка несвязанных элементов
print(uf.connected(1, 4))  # False

# Объединяем 4 и 5
uf.union(4, 5)
print(uf.connected(4, 5))  # True



