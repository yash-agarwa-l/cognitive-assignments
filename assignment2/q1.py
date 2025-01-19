# 1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
# i. WAP to add 200 and 300 to L.
# ii. WAP to remove 10 and 30 from L.
# iii. WAP to sort L in ascending order.
# iv. WAP to sort L in descending order.

L = [10,20,30,40,50,60,70,80]

L.append(200)
L.append(300)

L.remove(10)
L.remove(30)

L.sort()
print(L)
L.sort(reverse=True)
print(L)

