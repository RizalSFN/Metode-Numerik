def menu():
    print("===========================================================")
    print("                          Kelompok 7                       ")
    print("===========================================================")
    print("                   Program Penyelesaian SPL                ")
    print("===========================================================")
    print("1. Rizal Sofiana - 24552011183")
    print("2. Rival Raditya Ramdani - 24552011143")
    print("===========================================================\n")

    print("===========================================================")
    print("                        Pilihan Metode                     ")
    print("===========================================================")
    print("1. Metode Eliminasi (Gaussian)")
    print("2. Metode Iterasi (Jacobi)")

    loop = True

    while (loop):
        print("===========================================================")

        pilihan = int(input("Masukkan pilihan metode : "))

        if (pilihan == int(1)):
            a = [
                [1, 1, -1, 1, -1],
                [2, 2, 1, -1, 1],
                [3, 1,-3, -2, 3],
                [4, 1, -1, 4, -5],
                [16, -1, 1, -1, -1]
            ]
            b = [2, 4, 8, 16, 32]

            print("===========================================================\n")
            print("===========================================================")
            print("                             SOAL                          ")
            print("===========================================================")
            print("x1   + x2  - x3  + x4  - x5  = 2")
            print("2x1  + 2x2 + x3  - x4  + x5  = 4")
            print("3x1  + x2  - 3x3 - 2x4 + 3x5 = 8")
            print("4x1  + x2  - x3  + 4x4 - 5x5 = 16")
            print("16x1 - x2  + x3  - x4  - x5  = 32 \n")

            print("===========================================================")
            print("                LANGKAH - LANGKAH PENYELESAIAN             ")
            print("===========================================================")
            gauss_elimination([row[:] for row in a], b[:])
            loop = False
        elif (pilihan == int(2)):
            A = [
                [10, 5, 0, 0],
                [5, 10, -4, 0],
                [0, -4, 8, -1],
                [0, 0, -1, 5],
            ]
            B = [6, 25, -11, -11]

            print("===========================================================\n")
            print("===========================================================")
            print("                             SOAL                          ")
            print("===========================================================")
            print("10x1 + 5x2              = 6")
            print("5x1  + 10x2 - 4x3       = 25")
            print("     - 4x2  + 8x3 - x4  = -11")
            print("            - x3  + 5x4 = -11\n")

            print("===========================================================")
            max_itr = int(input("Masukkan maksimal iterasi : "))
            print("===========================================================\n")
            print("===========================================================")
            print("                LANGKAH - LANGKAH PENYELESAIAN             ")
            print("===========================================================")
            jacobi_iteration(A, B, max_iter=max_itr)
            loop = False
        else:
            print("Masukkan angka yang valid (1 atau 2)")
            loop = True

def print_matrix(a, b):
    """Mencetak matriks dan vektor hasil secara rapih"""
    for i in range(len(a)):
        row = "  ".join(f"{val:8.4f}" for val in a[i])
        print(f"{row} | {b[i]:8.4f}")
    print()

def gauss_elimination(a, b):
    n = len(b)

    print("Matriks Awal:")
    print_matrix(a, b)

    for i in range(n):
        # Pivoting
        max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
        if i != max_row:
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]
            print(f"Menukar baris {i+1} dengan baris {max_row+1}")
            print_matrix(a, b)

        # Eliminasi
        for j in range(i+1, n):
            if a[i][i] == 0:
                continue  # hindari pembagian dengan nol
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            b[j] -= factor * b[i]
            print(f"Eliminasi baris {j+1} dengan faktor {factor:.4f}")
            print_matrix(a, b)

    # Substitusi mundur
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(a[i][j]*x[j] for j in range(i+1, n))) / a[i][i]

    print("===========================================================")
    print("                   Hasil Substitusi Mundur                 ")
    print("===========================================================")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.4f}")
    return x

def jacobi_iteration(A, b, tol=1e-6, max_iter=0):
    n = len(b)
    x = [0.0 for _ in range(n)]
    print("Tebakan awal:", x)

    for iterasi in range(max_iter):
        x_new = [0.0 for _ in range(n)]
        print(f"\nIterasi ke-{iterasi+1}:")
        for i in range(n):
            sigma = sum(A[i][j]*x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]
            print(f"x{i+1} = ({b[i]} - {sigma:.6f}) / {A[i][i]} = {x_new[i]:.6f}")

        # Cek konvergensi
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            print("\nKonvergen!")
            break

        x = x_new[:]

    print("\n===========================================================")
    print("                         Hasil Akhir                       ")
    print("===========================================================")
    for i, val in enumerate(x):
        print(f"x{i+1} = {val:.6f}")
    return x

menu()