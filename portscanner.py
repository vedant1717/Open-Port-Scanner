import socket
import termcolor

def scan(target, ports):
    print(termcolor.colored(('\n' + 'Starting scan for '+ str(target)), 'cyan'))
    for port in range(1, ports):
        scan_port(target, port)
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored(("[+] Port Opened " + str(port)),'red'))
    except:
       pass

print(termcolor.colored(('''⠀⠀⠀⢀⣴⣾⣿⣿⣿⡶⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⢾⣿⣿⣿⣷⣦⡀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠉⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠈⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣯⠁⠀⠀⠀⠀⠀⢈⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⢖⣛⣧⣴⣶⣤⣄⠹⡆⡀⠀⠀⠀⠀⡼⢃⣤⣴⣶⣧⣽⣛⡲⣤⠀⠀⠀⠀⠀
⠀⢱⣄⣴⣟⠾⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣞⣷⣄⣴⠃⠀
⢠⠟⠉⠉⠉⠛⠓⠿⠏⠸⠟⠛⠉⠀⢠⡇⠀⠀⠀⣿⠀⠀⠉⠛⠻⠇⠿⠟⠛⠋⠉⠉⠙⠻⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⢿⡇⠀⠀⠀⢿⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡄⠀⠀⠀⠀⠀⠀⠀⣀⣤⢴⠏⠀⣸⠁⠀⠀⠀⢸⡆⠈⢳⡀⣤⡀⠀⠀⠀⠀⠀⠀⠀⡄⠀
⠀⢹⣶⢤⣤⡤⠴⠶⠛⠉⠀⠸⠀⣄⢻⣄⠀⠀⢀⣸⢃⣀⠰⠃⠈⠙⠓⠶⠤⣤⣤⢤⣾⠃⠀
⠀⠈⢿⣆⠻⣿⣄⠀⠀⠀⠀⠀⠀⠉⣱⣬⣍⣉⣯⣥⡉⠁⠀⠀⠀⠀⠀⠀⣴⣿⢃⣾⡏⠀⠀
⠀⠀⠈⢿⣆⠹⣿⣧⣀⣀⣀⣀⣤⣴⣿⣿⠟⠙⢿⣿⣿⣦⣄⣀⣀⣀⣠⣾⡿⠁⣼⠟⠀⠀⠀
⠀⠀⠀⠈⢿⣦⡈⠻⠿⠿⠿⠿⢿⣿⣿⣋⣀⣀⣀⣻⣿⣿⠿⠿⠿⠿⠿⠛⣠⣾⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣎⠓⢤⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⣀⠴⢊⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⢤⣄⣀⣠⡄⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣿⣿⣷⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''),'green'))

targets = input("[*] Enter targets to scan(split them by ,): ")
ports = int(input("[*] Enter how many ports to scan: "))
if ',' in targets:
    print(termcolor.colored(("[*] Scanning multiple targets..."), 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(','), ports)
else:
    scan(targets, ports)