def round(pt_1, pt_2, key_round, n, c):
    # plaintext = t1[0:n-1]t2[0:n-1]
    # print(type(pt_1))
    t1 = pt_1    
    t2 = pt_2
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
    # plainText_1 = t1
    # plainText_2 = t2
    # print(type(t1))
    return t1, t2
    # print(format(text1_list[-1], '016X'),
    #       format(text2_list[-1], "016X"), "ciphertext hex",)

