A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]


def shape(m):
    num_rows = len(m)
    num_cols = len(m[0]) if m else 0
    return num_rows, num_cols


def get_row(m, i):
    return m[i]


def get_column(m, j):
    return [m_i[j] for m_i in m]


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


print(shape(A))
print(shape(B))
print(get_row(A, 1))
print(get_column(B, 0))
print(make_matrix(5, 5, is_diagonal))
