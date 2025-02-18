import ipaddress
import csv
import matplotlib.pyplot as plt


def validar_rango_ip(ip):
    """Verifica si la IP es privada o pública."""
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        if ip_obj.is_private:
            print(f"La IP {ip} es PRIVADA (uso interno en redes LAN, VPN, etc.).")
        else:
            print(f"La IP {ip} es PÚBLICA (enrutada a través de Internet).")
    except ValueError:
        print("Error: La dirección IP ingresada no es válida.")

def clasificar_ip(ip):
    """Determina la clase de la dirección IP y su uso típico."""
    primer_octeto = int(ip.split(".")[0])
    
    if 1 <= primer_octeto <= 126:
        clase = "A"
        uso = "Grandes redes empresariales y gubernamentales."
    elif 128 <= primer_octeto <= 191:
        clase = "B"
        uso = "Medianas empresas y organizaciones."
    elif 192 <= primer_octeto <= 223:
        clase = "C"
        uso = "Pequeñas empresas y redes domésticas."
    elif 224 <= primer_octeto <= 239:
        clase = "D"
        uso = "Direcciones multicast (no asignadas a dispositivos específicos)."
    elif 240 <= primer_octeto <= 255:
        clase = "E"
        uso = "Reservado para investigación y usos futuros."
    else:
        clase = "Desconocida"
        uso = "No corresponde a una clase estándar."

    print(f"La IP {ip} pertenece a la clase {clase}. Uso típico: {uso}")

def guardar_en_csv(ip, prefijo, direccion_red, mascara, broadcast, primera_ip, ultima_ip, num_hosts):
    nombre_archivo = "subnetting_resultados.csv"
    try:
        with open(nombre_archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["IP", "Prefijo", "Dirección de Red", "Máscara", "Broadcast", "Primera IP", "Última IP", "Hosts Disponibles"])
            writer.writerow([ip, prefijo, direccion_red, mascara, broadcast, primera_ip, ultima_ip, num_hosts])
        
        print(f"✅ Resultados exportados correctamente a '{nombre_archivo}'.")

    except Exception as e:
        print(f"❌ Error al exportar a CSV: {e}")

def calcular_subnetting(ip, prefijo):
    try:
        # Crear un objeto IPv4Network
        red = ipaddress.IPv4Network(f"{ip}/{prefijo}", strict=False)
        
        # Obtener la máscara de subred
        mascara = red.netmask
        
        # Obtener la dirección de red
        direccion_red = red.network_address
        
        # Obtener la dirección de broadcast
        broadcast = red.broadcast_address
        
        # Obtener el rango de direcciones IP disponibles
        primera_ip = list(red.hosts())[0]
        ultima_ip = list(red.hosts())[-1]
        
        # Obtener el número de hosts disponibles
        num_hosts = red.num_addresses - 2  # Restamos 2 para excluir la dirección de red y broadcast
        
        # Imprimir los resultados
        print(f"Dirección de red: {direccion_red}")
        print(f"Máscara de subred: {mascara}")
        print(f"Dirección de broadcast: {broadcast}")
        print(f"Rango de direcciones IP disponibles: {primera_ip} - {ultima_ip}")
        print(f"Número de hosts disponibles: {num_hosts}")

         # Validar si la IP es privada o pública
        print("\n--- Validación de Rango de IP ---")
        validar_rango_ip(ip)

        # Clasificar la IP
        print("\n--- Clasificación de la IP ---")
        clasificar_ip(ip)
        
        # Guardar resultados en CSV
        guardar_en_csv(ip, prefijo, direccion_red, mascara, broadcast, primera_ip, ultima_ip, num_hosts)

    except ValueError as e:
        print(f"Error: {e}")


# Ejemplo de uso
ip = input("Introduce la dirección IP (ej. 192.168.1.0): ")
prefijo = int(input("Introduce el prefijo de la máscara de subred (ej. 24): "))

calcular_subnetting(ip, prefijo)