def check_password(password):
    buffer = [""]*32
    p = list(password)
    
    for i in range(8):
        buffer[i] = p[i]
    for i in range(8, 16):
        buffer[i] = p[23- i]
    for i in range(16, 32, 2):
        buffer[i] = p[46 - i]
    for i in range(31, 16, -2):
        buffer[i] = p[i]

    print(''.join(buffer))

check_password("jU5t_a_sna_3lpm11g54e_u_4_m4r042")
