import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print("Port {} is open on host {}".format(port, host))
        sock.close()
    except:
        pass

def scan_ports(start_ip, end_ip, ports):
    start_ip_parts = start_ip.split(".")
    end_ip_parts = end_ip.split(".")

    for i in range(int(start_ip_parts[3]), int(end_ip_parts[3]) + 1):
        host = start_ip_parts[0] + "." + start_ip_parts[1] + "." + start_ip_parts[2] + "." + str(i)
        for port in ports:
            check_port(host, port)

ports = [21, 22, 80, 443, 8080]
start_ip = "10.0.0.1"
end_ip = "11.0.0.1"
scan_ports(start_ip, end_ip, ports)
