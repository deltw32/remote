from pwn import *
import time
myfile=open("out.txt",mode='w+')
def connect_to_c2_agent( cmdId, data ):
    io = remote("127.0.0.1", 7373)
    header = b'nslab_w31c0m3_U\x00'
    cmd = cmdId + b'\x00' * ( 4 - len(cmdId) )
    content = header + cmd + data
    io.send(content)
    # whatever you want
    try:
        response=io.recvline()
        myfile.write(f"cmdId:{cmdId}, response:{response}\n")
    except:
        io.close()
    io.close()
for i in range(10000):
    cmdId=str(i).zfill(4).encode()
    connect_to_c2_agent(cmdId,b'b10902035')
