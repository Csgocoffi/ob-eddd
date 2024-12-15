class UnionFind:
    def __init__(self, size):
        # ������������� ������� ������������ ����� � ������
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, p):
        # ����� ����� ����������, � ������� ����������� ������� p
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # ������������ (path compression)
        return self.parent[p]

    def union(self, p, q):
        # ����������� ��������� p � q
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:  # ������ ���� ����� ������
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        # ��������, ��������� �� ���������� p � q
        return self.find(p) == self.find(q)

# ������ �������������
uf = UnionFind(10)

# ���������� 1 � 2
uf.union(1, 2)
print(uf.connected(1, 2))  # True

# ���������� 2 � 3
uf.union(2, 3)
print(uf.connected(1, 3))  # True

# �������� ����������� ���������
print(uf.connected(1, 4))  # False

# ���������� 4 � 5
uf.union(4, 5)
print(uf.connected(4, 5))  # True



