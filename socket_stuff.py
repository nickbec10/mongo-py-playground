# Networking trys using socket
import socket
# from contextlib import closing

print('Check DNS Server')
dns_server = '8.8.8.8'
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_result = udp_sock.connect_ex((dns_server,53))
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_result = udp_sock.connect_ex((dns_server,53))
if udp_result or tcp_result == 0:
    print('DNS is up')
else:
    print('DNS is down')
udp_sock.close()
tcp_sock.close()

print('\nCheck NTP Server')
ntp_server = '132.163.4.103'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result = sock.connect_ex((ntp_server,123))
if result == 0:
    print('NTP is up')
else:
    print('NTP is down')
sock.close()

# def check_socket(host='132.163.4.103', port=123):
#     with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
#         if sock.connect_ex((host, port)) == 0:
#             print('Port is open')
#         else:
#             print('Port is closed')

print('\nDNS Forward Lookups')
HOSTS = [
    'nextcloud.atomictinker.com',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host, msg))

print('\nDNS Reverse Lookups')
try:
    hostname, aliases, address = socket.gethostbyaddr('64.233.185.99')
except socket.herror:
    print(f'Host unknown or unavailable, are your internets up?')
else:
    print(f'Hostname: {hostname}')
    print(f'Aliases: {aliases}')
    print(f'IP Address: {address}')