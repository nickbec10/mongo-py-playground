# Networking trys using socket
import socket
import dns.resolver
# from contextlib import closing


def check_dns(dns_records):
    # Finding A record
    try:
        result = dns.resolver.resolve(dns_records, 'A')
        # Printing record
        for val in result:
            print(dns_records + ' A Record : ', val.to_text())
        return True
    except dns.exception.DNSException:
        print(f'Host unknown or unavailable, are your internets up?')
        return False

def check_ntp(ntp_server):
    print('\nCheck NTP Server')
    # ntp_server = '132.163.4.103'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = sock.connect_ex((ntp_server,123))
    if result == 0:
        return 'NTP is up'
    else:
        return 'NTP is down'
    sock.close()

def check_web(web_server):
    print('\nCheck Web Server')
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((web_server,80))
        if result == 0:
            print(web_server + ' is up')
            return True
        else:
            print(web_server + ' is down')
            return False
        sock.close()
    except socket.gaierror:
        print(web_server + ': Nodename nor servname provided, or not known')
        return False

# def check_socket(host='132.163.4.103', port=123):
#     with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
#         if sock.connect_ex((host, port)) == 0:
#             print('Port is open')
#         else:
#             print('Port is closed')

# print('\nDNS Forward Lookups')
# HOSTS = [
#     'nextcloud.atomictinker.com',
#     'pymotw.com',
#     'www.python.org',
#     'apod.nasa.gov',
#     'nosuchname'
# ]

# for host in HOSTS:
#     try:
#         print('{} : {}'.format(host, socket.gethostbyname(host)))
#     except socket.error as msg:
#         print('{} : {}'.format(host, msg))

# print('\nDNS Reverse Lookups')
# try:
#     hostname, aliases, address = socket.gethostbyaddr('64.233.185.99')
# except socket.herror:
#     print(f'Host unknown or unavailable, are your internets up?')
# else:
#     print(f'Hostname: {hostname}')
#     print(f'Aliases: {aliases}')
#     print(f'IP Address: {address}')

check_dns("reddit.com")
#check_dns("dsvlknsdlve.com")

check_ntp("132.163.4.103")
#check_ntp("6.5.6.5")

check_web("stackoverflow.com")
check_web("www.npr.org")
check_web("bcnisacubkaw3u.com")