def genap(item):
    list_genap=[]
    for i in item:
        if i%2==0:
            list_genap.append(i)
    return list_genap
list=[1,2,3,4,5,6,7,8,9]

print(genap(list))


