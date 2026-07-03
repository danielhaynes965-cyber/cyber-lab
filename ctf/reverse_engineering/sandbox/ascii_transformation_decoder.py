enc = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽'

# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

flag = ''

for i in range(0, len(enc)):
    char1 = chr(ord(enc[i]) >> 8)
    char2 = chr(ord(enc[i]) & 0xFF)
    
    flag += char1+char2

print(flag)
