from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/whoareyou')
def whoareyou():
    name = '홍길동'
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    
    return name + " : " + host_name + " : " + host_ip

app.run(host="0.0.0.0",port=5000)