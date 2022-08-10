#hatayı anla!!!!
import socket

def ipBul():
    benimip=(socket.gethostbyname(socket.gethostname()))  
    print(benimip)
        with open("ip.txt","wb") as ipDosyam: 
            ipDosyam.write(benimip)
ipBul()

mevcutip=(socket.gethostbyname(socket.gethostname()))

def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read() 

benimip2= dosyaAc("ip.txt")
print(benimip)
print(mevcutip)

if benimip2 == mevcutip:
    print("sorun yok")
else:
    print("kontrol başlatıldı")
