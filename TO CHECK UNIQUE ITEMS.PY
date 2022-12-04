#TO COUNT ITEM IN LIST / TO PRINT UNIQ2UE ITEM USING SET

a = [1,2,3,4,4,5,76,6,6,'abc','abc']
x = set(a)
for item in x:
    b = a.count(item)
    print(b, item)
    if b > 1:
        print(item, 'occur moe than once')