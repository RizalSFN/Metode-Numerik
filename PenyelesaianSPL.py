def eliminasi_gauss_jordan(A, b):
    n = len(A)
    
    # Gabungkan A dan b menjadi matriks augmented
    for i in range(n):
        A[i].append(b[i])

    # Proses Gauss-Jordan
    for i in range(n):
        # Pastikan diagonal utama tidak nol (pivoting)
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    break

        # Bagi seluruh baris agar elemen diagonal = 1
        factor = A[i][i]
        for j in range(n+1):
            A[i][j] /= factor

        # Eliminasi kolom di atas dan bawah pivot
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n+1):
                    A[k][j] -= factor * A[i][j]

    # Ambil solusi
    x = [A[i][-1] for i in range(n)]
    return x

def iterasi_jacobi(A, b, tol=1e-6, max_iter=100):
    n = len(A)
    x = [0 for _ in range(n)]

    for iteration in range(max_iter):
        x_new = [0 for _ in range(n)]
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / A[i][i]

        # Cek konvergensi
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new

    print("Tidak konvergen dalam iterasi maksimum.")
    return x

# Contoh sistem persamaan:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

A = [
    [3, -1, 1],
    [3, 6, 2],
    [3, 3, 7],
]
b = [1, 0, 4]

# Solusi dengan Eliminasi Gauss-Jordan
# sol_gauss = eliminasi_gauss_jordan([row[:] for row in A], b[:])
# print("Solusi (Eliminasi Gauss-Jordan):", sol_gauss)

# Solusi dengan Iterasi Jacobi
sol_jacobi = iterasi_jacobi([row[:] for row in A], b[:])
print("Solusi (Jacobi):", sol_jacobi)