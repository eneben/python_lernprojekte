import ipaddress

def berechne_subnetz(ip_praefix):
    netz = ipaddress.ip_network(
        ip_praefix, strict=False
    )
    return {
        'netz_id': str(netz.network_address),
        'broadcast': str(netz.broadcast_address),
        'erster_host': str(netz.network_address + 1),
        'letzter_host':str(netz.broadcast_address - 1),
        'anzahl_hosts':netz.num_addresses - 2
    }

print(berechne_subnetz('192.168.1.130/26'))