import socket

s = socket.socket()
s.settimeout(5)

try:
    s.connect(("45.114.246.232", 3306))
    print("✅ Port open")
except Exception as e:
    print("❌ Port blocked:", e)