biner = []
no = int(0)
result = ""
j = 0

print("============================================")
print("                 Kelompok 7                 ")
print("============================================")
print("      Program konversi desimal ke biner     ")
print("============================================")
print("1. Rizal Sofiana - 24552011183")
print("2. Rival Raditya Ramdani - 24552011143")
print("============================================")

def main():
    global j, result, no
    a = input("Masukkan angka yang ingin dikonversi: ")

    n = int(a)

    q = int(n / 2)
    c = n - (2 * q)
    biner.append(c)
    no = q
    print("============================================")
    print(f'Q({j}) = {n}/2 = {q}')
    print(f'B({j}) = {n} - ( 2 * {q}) = {c}')
    print("============================================")

    while no != 0:
        j += 1
        q = int(no / 2)
        c = no - (2 * q)
        biner.append(c)
        print(f'Q({j}) = {no}/2 = {q}')
        print(f'B({j}) = {no} - ( 2 * {q}) = {c}')
        print("============================================")
        no = q

    for biners in reversed(biner):
        result += str(biners) + ' '

    print("Hasil koversi : " + result)
    print("============================================")

    ulagiLoop = True

    while ulagiLoop:
        ulangi = input("Apakah anda ingin mengulang? (y/t) : ").lower()
        if ulangi == 'y':
            ulagiLoop = False
            biner.clear()
            j = 0
            result = ""
            print("============================================")
            main()
        elif ulangi == 't':
            ulagiLoop = False
            print("============================================")
            print("Terima kasih telah menggunakan program ini")
        else:
            ulagiLoop = True
            print("============================================")
            print("Tolong Hanya Berikan Jawaban y atau t!")
            print("============================================")   
main()