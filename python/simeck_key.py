import simeck_round
def key_generation(t_2, t_1, t_0, k_0, T, n, z_0, z_1, c, i):
    # print (key_0_n)
    # print ("key_0_n in hex",format(key_0_n, '016b'))
    # for i in range(T):
    if (n == 16 & n == 24):
        key_r = c ^ ((z_0[i % 62]))
    elif (n == 32):
        key_r = c ^ ((z_1[i % 62]))
    t_0, k_0 = simeck_round.round(t_0, k_0, key_r, n, c, i)
    temp = t_2
    t_2 = t_0
    t_0 = t_1
    t_1 = temp
    # key_0_list.append(key_next)
    # print ("key{} = {}".format(i, key_next)
    return k_0

