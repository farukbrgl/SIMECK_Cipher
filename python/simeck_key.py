import simeck_round
def key_generation(t_2, t_1, t_0, k_0, T, n, z_0, z_1, c):
    # print (key_0_n)
    # print ("key_0_n in hex",format(key_0_n, '016b'))
    key_r_list = []
    key_list = []
    i = 0
    j = 0
    for i in range(T):
        if (n == 16 & n == 24):
            key_r = c ^ ((z_0[i % 62]))
            # print(type(key_r))
            key_r_list.append(key_r)
        elif (n == 32):
            key_r = c ^ ((z_1[i % 63])) ^ 3
            # print((key_r))
            key_r_list.append(key_r)
    print((key_r_list))
    for j in range(T):
        key_list.append(k_0)
        t_0, k_0 = simeck_round.round(t_0, k_0, key_r_list[j], n, c)
        temp = t_2
        t_2 = t_0
        t_0 = t_1
        t_1 = temp
    # key_0_list.append(key_next)
    # print ("key{} = {}".format(i, key_next)
    
    return key_list

# # z sabitleri oluşturuluyor
z_0 = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
# z_1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]
z_1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0]

# sabit değer
n = 32
c = 2**(n) - 1
T = 44
t_2 = 0x1b1a1918  # most significant
t_1 = 0x13121110
t_0 = 0x0b0a0908
k_0 = 0x03020100  # least significant

# for i in range (5):
a = key_generation(t_2, t_1, t_0, k_0, T, n, z_0, z_1, c)
print(a)