#!/usr/bin/env python
# coding: utf-8
 
"""
SIMECK Hafif Blok Şifreleyicisinin Python ile Gerçeklenmesi
Orijinal makaleye https://doi.org/10.1007/978-3-662-48324-4_16 adresinden ulaşabilirsiniz.
"""

"""
plaintext, ciphertext ve key oluşturuldu
encryption ve decryption işlemlerinin ikisi de gerçekleştiriliyor
bunlar orijinal makaledeki n=32 durumunda verilen başlangıç vektörleri
sonuçların doğruluğunu makaleden inceleyebilirsiniz
farklı boyuttaki şifreleyici için farklı değerler vermelisiniz
"""
plainText_1 = 0x656b696c  # most significant
plainText_2 = 0x20646e75  # least significant
# print(format(plainText_1, '016X'), format(
#     plainText_2, "016X"), "plaintexts in start in hex")

cipherText_2 = 0x45ce6902
cipherText_1 = 0x5f7ab7ed
# print(format(cipherText_1, '016X'), format(
#     cipherText_2, "016X"), "ciphertexts in start in hex")

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

# sabit değer
n = 32
c = 2**(n) - 4
T = 44


key_0_list = []
import simeck_round

import simeck_key

for i in range(T):
    key = simeck_key.key_generation(t_2, t_1, t_0, k_0, T, n, z_0, z_1, c, i)
    pt1, pt2 = simeck_round.round(plainText_1, plainText_2, key, n, c, i)
    plainText_1 = pt1
    plainText_2 = pt2
    print(plainText_1, plainText_2, i)