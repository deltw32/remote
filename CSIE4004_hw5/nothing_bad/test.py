from pwn import *
import time
def connect_to_c2_agent( cmdId, data ):
    io = remote("127.0.0.1", 7373)
    header = b'nslab_w31c0m3_U\x00'
    cmd = cmdId + b'\x00' * ( 4 - len(cmdId) )
    content = header + cmd + data
    io.send(content)
    # whatever you want.
    io.close()
for i in range(0000,9999):
    string=str(i)
    id=string.encode()
    connect_to_c2_agent(id,b'b10902035');
