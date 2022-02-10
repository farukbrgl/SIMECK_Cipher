#!/usr/bin/env python
# coding: utf-8

"""
SIMECK Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://doi.org/10.1007/978-3-662-48324-4_16 adresinden ulaşabilirsiniz.
"""

"""
plaintext, ciphertext ve key oluşturuldu
encryption ve decryption işlemlerinin ikisi de gerçekleştiriliyor
bunlar orijinal makaledeki n=16, m=4 durumunda verilen başlangıç vektörleri
sonuçların doğruluğunu makaleden inceleyebilirsiniz
farklı boyuttaki şifreleyici için farklı değerler vermelisiniz
"""
plainText_1 = 0x656b696c  # most significant
plainText_2 = 0x20646e75  # least significant
print(format(plainText_1, '016X'), format(
    plainText_2, "016X"), "plaintexts in start in hex")

cipherText_2 = 0x45ce6902
cipherText_1 = 0x5f7ab7ed
print(format(cipherText_1, '016X'), format(
    cipherText_2, "016X"), "ciphertexts in start in hex")

t_2 = 0x1b1a1918  # most significant
t_1 = 0x13121110
t_0 = 0x0b0a0908
k_0 = 0x03020100  # least significant
# print(format(key_3, '016x'), format(key_2, "016X"), format(
#     key_1, "016X"), format(key_0, "016X"), "keys in hex")

# z sabitleri oluşturuluyor
z_0 = [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1,
       0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
z_1 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1,
       0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0]


# n ve m değerleri oluşturuluyor
# bir alttaki bölümde el ile n ve m değeri girmeyi ayarlanabilir
n = 32
m = 4

"""
n ve m değerleri kullanıcıdan isteniyor
bu değerlere göre T ve j oluşturuluyor
"""
# print("n=16, 24, 32, 48, 64 olabilir\n m 2, 3, 4 olabilir")
# n = int(input("n değerini giriniz:"))
# m = int(input("m değerini giriniz:"))

# sabit değer
c = 2**(n) - 4


T = 0
if (n == 16):
    T = 32
elif (n == 24):
    T = 36
elif (n == 32):
    T = 44
else:
    print("yanlış değer girdiniz\ndevam etmeyiniz")


# round function


def round(pt_1, pt_2, key_round):
    # plaintext = t1[0:n-1]t2[0:n-1]
    t1 = plainText_1
    t2 = plainText_2
    # print ("before texts 01 in hex",format(t1, '04x'), format(t2, "04X"))
    # print(key_0_list[i])
    crol_1 = (t1 << 1) + (t1 >> (n - 1)) & c
    crol_5 = (t1 << 5) + (t1 >> (n - 5)) & c
    tmp1 = t1 & crol_5
    tmp2 = t2 ^ tmp1
    tmp3 = tmp2 ^ crol_1
    tmp4 = tmp3 ^ key_round
    t2 = t1
    t1 = tmp4
    # text1_list.append(t1)
    # text2_list.append(t2)
    plainText_1 = t1
    plainText_2 = t2
    return t1, t2
    # print(format(text1_list[-1], '016X'),
    #       format(text2_list[-1], "016X"), "ciphertext hex",)


key_0_list = []


def key_generation(t_2, t_1, t_0, k_0, T):
    # print (key_0_n)
    # print ("key_0_n in hex",format(key_0_n, '016b'))
    # for i in range(T):
    if (n == 16 & n == 24):
        key_r = c ^ ((z_0[i % 62]))
    elif (n == 32):
        key_r = c ^ ((z_1[i % 62]))
    t_0, k_0 = round(t_0, k_0, key_r)
    temp = t_2
    t_2 = t_0
    t_0 = t_1
    t_1 = temp
    # key_0_list.append(key_next)
    # print ("key{} = {}".format(i, key_next)
    return k_0


for i in range(T):
    key = key_generation(t_2, t_1, t_0, k_0, T)
    ct1, ct2 = round(plainText_1, plainText_2, key)
    print(ct1, ct2)

# key_list = key_generation(key_0, key_1, key_2, key_3, m, T)
# # text1_list = []
# # text2_list = []


# print(text1_list)


# ### decryption
# cp_text1_list= []
# cp_text2_list= []
# # def enc(plainText_1, plainText_2, key_0, T):
# for k in reversed(key_0_list):
#     #plaintext = t1[0:3]t2[0:3]
#     ct1 = cipherText_1
#     ct2 = cipherText_2
#     # print ("before texts 01 in hex",format(t1, '04x'), format(t2, "04X"))
#     # print(key_0_list[i])
#     crol_1 = (ct1 << 1) + (ct1 >> (n-1)) & c
#     crol_2 = (ct1 << 2) + (ct1 >> (n-2)) & c
#     crol_8 = (ct1 << 8) + (ct1 >> (n-8)) & c
#     tmp1 = crol_1 & crol_8
#     tmp2 = ct2 ^ tmp1
#     tmp3 = tmp2 ^ crol_2
#     tmp4 = tmp3 ^ k
#     ct2 = ct1
#     ct1 = tmp4
#
#     #print(key_0)
#     # t1 = tmp
#     cp_text1_list.append(ct1)
#     cp_text2_list.append(ct2)
#     # print(t1, t2)
#
#     # print(text1_list)
#     # print(text2_list)
#     # print("key {} = {}".format(key_0_list.index(),k))
#     cipherText_1 = ct1
#     cipherText_2 = ct2
# # print(t1,t2)
#     # return text1_list, text2_list
# print (format(cp_text2_list[-1], '016X'), format(cp_text1_list[-1], "016X"), "plaintext hex")


# key_generation(key_0, key_1, key_2, key_3, m)
# enc(plainText_1, plainText_2, key_0)
# a,b= enc(plainText_1, plainText_2, key_list, T)
