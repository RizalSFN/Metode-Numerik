def main():
    print("===========================================================")
    print("                          Kelompok 7                       ")
    print("===========================================================")
    print("      Program Penyelesaian SPL - Metode Iterasi Jacobi     ")
    print("===========================================================")
    print("1. Rizal Sofiana - 24552011183")
    print("2. Rival Raditya Ramdani - 24552011143")
    print("===========================================================\n")
    
    A = [
            [10, 5, 0, 0],
            [5, 10, -4, 0],
            [0, -4, 8, -1],
            [0, 0, -1, 5],
        ]
    B = [6, 25, -11, -11]
    
    print("===========================================================")
    print("                     SOAL Hal. 459 No. 1c                  ")
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

main()