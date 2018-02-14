#by:
#!/usr/bin/python2.7

import sys
import socket
import threading
import json
from collections import OrderedDict
import binascii
import datetime
import time


def server_loop(local_host, local_port, remote_host, remote_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print "--Jaring sudah dipasang, jangan di close.!!--"
        print "Tong cena kabur eta preman.!!"
        server.bind((local_host, local_port))
    except:
        print "[!!] Gagal menerima IP %s:%d" % (local_host, local_port)
        print "[!!] Pastikan IP sudah benar!"
        sys.exit(0)

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        print"[+] Koneksi masuk dari  %s:%d" % (addr[0], addr[1])

        proxy_thread = threading.Thread(target=proxy_handler,
                                        args=(client_socket, remote_host, remote_port))
        proxy_thread.daemon = False

        proxy_thread.start()


def receive_from(connection):

    buffer = ""

    connection.settimeout(0)

    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass

    return buffer


def request_handler(socket_buffer):
    if ('submitLogin' in socket_buffer) or ('eth_login' in socket_buffer):
        json_data = json.loads(socket_buffer, object_pairs_hook=OrderedDict)
        print('[+] Proses autentikasi dari alamat : ' + json_data['params'][0])
        if wallet not in json_data['params'][0]:
             print('[*] Ada Preman - Merubah alamat - ' + str(datetime.datetime.now()))
             print('[*] PREMAN: ' + json_data['params'][0])
             json_data['params'][0] = wallet + worker_name
             print('[*] SULTAN: ' + json_data['params'][0])

        socket_buffer = json.dumps(json_data) + '\n'
        
    return socket_buffer



def response_handler(buffer):
    return buffer


def proxy_handler(client_socket, remote_host, remote_port):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    for attempt_pool in range(3):
        try:
            remote_socket.connect((remote_host, remote_port))
        except:
            print "[!] Tidak mungkin masuk ke pool ini "
            time.sleep(2)
        else:
            # Connection OK
            break
    else:
        print "[!] Tidak mungkin masuk ke pool ini. Restart claymore atau periksa koneksi internet "+ str(datetime.datetime.now())
        
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
        
        sys.exit()
        

    while True:

        local_buffer = receive_from(client_socket)
        
        if len(local_buffer):

            local_buffer = request_handler(local_buffer)
            
            
            try:
                remote_socket.send(local_buffer)
            except:
                print "[!] Kiriman share gagal."
                time.sleep(0.02)
                print "[!] Koneksi dengan pool gagal. Restart claymore atau periksa koneksi internet "+ str(datetime.datetime.now())
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
                break
                
            time.sleep(0.001)

        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            
            remote_buffer = response_handler(remote_buffer)
            
            
            try:
                 client_socket.send(remote_buffer)
            except:
                 print('[-] Autentikasi Terputus - Preman berhenti mining - ' + str(datetime.datetime.now()))
                 client_socket.close()
                 break

            time.sleep(0.001)
        time.sleep(0.001)
        
    sys.exit()


def main():
    if len(sys.argv[1:]) != 5:
        print "Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [ETH Wallet]"
        print "Example: ./proxy.py 127.0.0.1 9000 eth.realpool.org 9000 0x..."
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    global wallet 
    wallet = sys.argv[5]
    
    global worker_name
    worker_name = 'rba'
    
    #worker_name = ''
    
    pool_slash = ['nanopool.org','dwarfpool.com']
    pool_dot = ['ethpool.org','ethermine.org','alpereum.ch']
    if worker_name:
        if any(s in remote_host for s in pool_slash):
            worker_name = '/' + worker_name
        elif any(d in remote_host for d in pool_dot):
            worker_name = '.' + worker_name
        else:
            print "Pool mana ini ? - Worker kosong"
            worker_name = ''

    print "Wallet set: " + wallet + worker_name

    server_loop(local_host, local_port, remote_host, remote_port)


if __name__ == "__main__":
    main()

