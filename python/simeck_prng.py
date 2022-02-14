import simeck
cipherText_1 = 0
cipherText_2 = 0
IV_1 = 0x656b696c
IV_2 = 0x20646e75
# pt_1 = IV_1 ^ 0
# pt_2 = IV_2 ^ 0
# print(pt_1)
# print(pt_2)
f = open("random_numbers.txt", "w")
a, b = simeck.SIMECK(plainText_1=IV_1, plainText_2=IV_2)
x = format(a, '032b')
y = format(b, '032b')
f.write(str(x) + str(y) + "\n")
for i in range(9999):
    a, b = simeck.SIMECK(plainText_1=a, plainText_2=b)
    z = format(a, '032b')
    t = format(b, '032b')
    f.write(str(z) + str(t) + "\n")
f.close()
# while 1 == 1:
#     a,b = SIMON(plainText_1 = a, plainText_2 = b)
