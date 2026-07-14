import subprocess 
import ipaddress



def ping(ip):
   resultado = subprocess.run(
   ["ping", "-c", "1",str(ip)],
   stdout=subprocess.DEVNULL,
   stderr=subprocess.DEVNULL
)
   return resultado.returncode == 0

def MAC(ip):
    resultado = subprocess.run(
       ["ip", "neigh", "show", str(ip)],
       capture_output=True,
       text=True
     )
    datos = resultado.stdout.split()
    if len(datos) >= 5:
        return datos[4]
    else:
        return "Desconocida"



red_ITSP = ipaddress.ip_network("192.168.2.0/24", strict=False)

archivo = open("Resultado.txt","w")

for ip in red_ITSP.hosts():
    if ping(ip):
       mac = MAC(ip)
       print(f"{ip} - Activa - MAC:{mac} ")
       archivo.write(f"{ip} - Activa - MAC: {mac}\n")
    else:
        print(f"{ip} - Inactiva")
        archivo.write(f"{ip} - inactiva\n")  
       archivo.close()

