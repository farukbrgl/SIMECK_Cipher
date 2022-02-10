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
plainText_1 = 0x656b696c #most significant
plainText_2 = 0x20646e75 #least significant
print (format(plainText_1, '016X'), format(plainText_2, "016X"), "plaintexts in start in hex")

cipherText_2 = 0x45ce6902
cipherText_1 = 0x5f7ab7ed
print (format(cipherText_1, '016X'), format(cipherText_2, "016X"), "ciphertexts in start in hex")

key_3 = 0x1b1a1918 #most significant
key_2 = 0x13121110
key_1 = 0x0b0a0908
key_0 = 0x03020100 #least significant
print (format(key_3, '016x'), format(key_2, "016X"), format(key_1, "016X"), format(key_0, "016X"),"keys in hex")

#z sabitleri oluşturuluyor
z_0 = [1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0]
z_1 = [1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0]


#n ve m değerleri oluşturuluyor
#bir alttaki bölümde el ile n ve m değeri girmeyi ayarlanabilir
n = 32
m = 4

"""
n ve m değerleri kullanıcıdan isteniyor
bu değerlere göre T ve j oluşturuluyor
"""
# print("n=16, 24, 32, 48, 64 olabilir\n m 2, 3, 4 olabilir")
# n = int(input("n değerini giriniz:"))
# m = int(input("m değerini giriniz:"))

##sabit değer
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


key_0_list= []
def key_generation(key_0, key_1, key_2, key_3, m, T):
    key_0_n = key_0
    key_1_n = key_1
    key_2_n = key_2
    key_3_n = key_3
    # print (key_0_n)
    # print ("key_0_n in hex",format(key_0_n, '016b'))
    for i in range(T):
        # print ("key{} = {}".format(i, key_0_n))
        # print ("key_0_n in hex",format(key_0_n, '016b'))
        temp1 = (key_3 >> 3)|(key_3 << (n - 3)) & c
        temp2 = key_1 ^ temp1
        temp3 = (temp2 >> 1)|(temp2 << (n - 1)) & c
        temp4 = key_0_n ^ temp2
        temp5 = temp3 ^ temp4
        if (n == 16 & n == 24):
            temp6 = temp5 ^ c ^ ((z_0[i % 62]))
        elif (n == 32):
            temp6 = temp5 ^ c ^ ((z_1[i % 62]))
        key_next = key_0_n
        key_0_n = key_1
        key_1 = key_2
        key_2 = key_3
        key_3 = temp6
        key_0_list.append(key_next)
        # print ("key{} = {}".format(i, key_next)
    return key_0_list

key_list =key_generation(key_0, key_1, key_2, key_3, m, T)
text1_list= []
text2_list= []

### encryption
def enc(plainText_1, plainText_2):
    for k in key_0_list:
        ### plaintext = t1[0:3]t2[0:3]
        t1 = plainText_1
        t2 = plainText_2
        # print ("before texts 01 in hex",format(t1, '04x'), format(t2, "04X"))
        # print(key_0_list[i])
        crol_1 = (t1 << 1) + (t1 >> (n-1)) & c
        crol_5 = (t1 << 5) + (t1 >> (n-5)) & c
        tmp1 = t1 & crol_5
        tmp2 = t2 ^ tmp1
        tmp3 = tmp2 ^ crol_1
        tmp4 = tmp3 ^ k
        t2 = t1
        t1 = tmp4
        text1_list.append(t1)
        text2_list.append(t2)
        plainText_1 = t1
        plainText_2 = t2
        return text1_list, text2_list
    print (format(text1_list[-1], '016X'), format(text2_list[-1], "016X"), "ciphertext hex",)
print(text1_list)



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
