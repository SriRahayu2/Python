def faktorial(n):
    if n==1: 
        return 1
    else:
        return n*faktorial(n-1)

x=int(input("Masukkan nilai = "))
print(faktorial(x))   