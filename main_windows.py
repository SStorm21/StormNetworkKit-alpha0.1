# version 1.0
#nmap for noobies 
#=================
# scan system
# open-closed ports
# os-system  
# vulners
# etc
# #please scan this domain scanme.nmap.org if you are testing with nmap scripts


# add a verfiy function to look for files if they are here or not

#vulners protocls scans 
# nmap -p- --script smb-vuln*
#Script vulners
import os
import subprocess
import time
from pystyle import Colors, Colorate,System ,Write
class Arts:

#Script Categories
    line = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    space="        "
    
    basic_scanners = Colorate.Horizontal(Colors.red_to_purple,"\nBasic Scanners  \n━━━━━━━━━━━━━",1)
    number1=Colorate.Horizontal(Colors.red_to_purple,"[ 1 ] os-scan guess",1)
    number2=Colorate.Horizontal(Colors.red_to_purple,"[ 2 ] all ports services and versions ",1)
    number3=Colorate.Horizontal(Colors.red_to_purple,"[ 3 ] default script scan",1)
    number4=Colorate.Horizontal(Colors.red_to_purple,"[ 4 ] run smb-os-discovery.nse (use if you assume its a windows machine)",1)
    number5=Colorate.Horizontal(Colors.red_to_purple,"[ 5 ] find live hosts on network",1)

    scanning_types = Colorate.Horizontal(Colors.red_to_purple,"\nScanning Types  \n━━━━━━━━━━━━━",1)
    number6=Colorate.Horizontal(Colors.red_to_purple,"[ 6 ] tcp syn port scan (Stealth Scan -sS) : (Open Port) Responds with SYN-ACK, (Closed Port) Responds with RST. (Filtered Port) No response or ICMP unreachable message.",1)
    number7=Colorate.Horizontal(Colors.red_to_purple,"[ 7 ] tcp ack port scan (tcp ack scan) : If you receive a RST(Unfiltered) response on a port, it means the port is reachable and not blocked by a firewall.",1)
    number8=Colorate.Horizontal(Colors.red_to_purple,f"[ 8 ] tcp connect port scan : Determine the state of a target's TCP ports by establishing a full TCP connection:\n{space}- Open Port: Responds with SYN-ACK.\n{space}- Closed Port: Responds with RST.\n{space}- Filtered Port: Likely blocked by a firewall.",1)
    number9=Colorate.Horizontal(Colors.red_to_purple,f"[ 9 ] tcp fin scan (same as xmas - Null): They can sneak through certain non-stateful firewalls and packet filtering routers\n{space}No response received: open|filtered / TCP RST packet: closed / ICMP unreachable error (type 3, code 1, 2, 3, 9, 10, or 13):filtered likely blocked by a firewall." ,1)
    number10=Colorate.Horizontal(Colors.red_to_purple,"[ 10 ] list scan : performs a reverse DNS lookup to identify hostnames without sending any traffic to the hosts. determine which hosts are available on a network without actively probing them for open ports. ",1)
    number11=Colorate.Horizontal(Colors.red_to_purple,f"[ 11 ] udp port scan (udp scan) : registered ports 53, 161/162, and 67/68 Probe Response/\n{space}UDP response from target port (unusual) open / No response open|filtered / ICMP port unreachable error (type 3,code3) closed / Other ICMP unreachable errors(type3,code 1,2,9,10,or13)filtered.",1)
    number12=Colorate.Horizontal(Colors.red_to_purple,"[ 12 ] ping scan : identify live hosts on a network by sending ICMP echo request packets to a range of IP addresses.",1)
    other_scans = Colorate.Horizontal(Colors.red_to_purple,"NSE Script Categories  \n━━━━━━━━━━━━━",1)
    
    cat_1 = Colorate.Horizontal(Colors.red_to_purple,"* SSH",1)
    number13=Colorate.Horizontal(Colors.red_to_purple,"[ 13 ] check SSH authentication methods.",1)
    number14=Colorate.Horizontal(Colors.red_to_purple,"[ 14 ] Brute-Force SSH Authentication.",1)
    
    cat_2 = Colorate.Horizontal(Colors.red_to_purple,"* SMB",1)
    number15=Colorate.Horizontal(Colors.red_to_purple,"[ 15 ] Enumerate SMB shares with authentication.",1)
    number16=Colorate.Horizontal(Colors.red_to_purple,"[ 16 ] Brute-Force SMB Authentication (with Hydra).",1)
    number17=Colorate.Horizontal(Colors.red_to_purple,"[ 17 ] Check for SMB vulnerabilities.",1)

    cat_3 = Colorate.Horizontal(Colors.red_to_purple,"* HTTP",1)
    number18=Colorate.Horizontal(Colors.red_to_purple,"[ 18 ] http-auth.",1)
    number19=Colorate.Horizontal(Colors.red_to_purple,"[ 19 ] http-methods.",1)
    number20=Colorate.Horizontal(Colors.red_to_purple,"[ 20 ] http-auth-finder.",1)
    number21=Colorate.Horizontal(Colors.red_to_purple,"[ 21 ] brute-force HTTP Basic Authentication credentials.",1)
    number22=Colorate.Horizontal(Colors.red_to_purple,"[ 22 ] http-auth-digest.",1)
    number23=Colorate.Horizontal(Colors.red_to_purple,"[ 23 ] http-brute.",1)
    number24=Colorate.Horizontal(Colors.red_to_purple,"[ 24 ] http-enum.",1)
    number25=Colorate.Horizontal(Colors.red_to_purple,"[ 25 ] http-vuln-cve2014-3704: (CVE-2014-3704) in Drupal that can lead to unauthorized access.",1)
    number26=Colorate.Horizontal(Colors.red_to_purple,"[ 26 ] http-vuln-cve2017-5638: (CVE-2017-5638) in Apache Struts that can lead to remote code execution.",1)
    number27=Colorate.Horizontal(Colors.red_to_purple,"[ 27 ] http-vuln-cve2019-11043: (CVE-2019-11043) in PHP-FPM that can lead to remote code execution.",1)
    number28=Colorate.Horizontal(Colors.red_to_purple,"[ 28 ] http-slowloris: checks for the Slowloris denial of service vulnerability.",1)
    number29=Colorate.Horizontal(Colors.red_to_purple,"[ 29 ] http-sql-injection.",1)
    number30=Colorate.Horizontal(Colors.red_to_purple,"[ 30 ] http-xssed.",1)
    number31=Colorate.Horizontal(Colors.red_to_purple,"[ 31 ] http-vuln-cve2018-11776: (CVE-2018-11776) in Apache Struts that can lead to remote code execution.",1)


    girl =Colorate.Vertical(Colors.red_to_purple,"""
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
    ┃          ⠀      Welcome to NFN! - ctrl-c to exit⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀ ┃ 
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠊⢀⣰⢃⢰⡞⢰⠇⡰⢹⠀⢠⢿⢠⠃⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⠀⠀⢸⠀⠀⠀⠀⢸⡄⠀⡇⠀⢰⠀⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠦⣩⣥⣰⣶⣻⡏⡎⡞⢃⡘⣐⡕⡏⢀⠇⡇⠸⠀⠀⡰⠁⢰⡇⠀⠀⠀⠀⠀⢰⢸⠀⠈⠀⠀⠀⢸⠀⠀⠀⠀⢸⠇⠀⢹⠀⠘⡆⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠾⠕⠞⢰⠁⡇⡞⢵⠿⣑⡇⣼⠀⣇⢰⠀⣰⠁⢠⣿⠀⠀⠀⠀⢠⠀⢸⢹⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⠰⠀⠘⠀⠀⡇⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⢀⢧⢿⢠⢱⣧⠋⠀⠀⡏⣻⠀⠛⡞⣴⡏⢀⣿⢻⠀⠀⢰⠂⢸⡄⢸⣿⠀⠠⠀⠀⠀⣾⠀⢀⠀⠀⠀⡆⡄⠀⢇⠀⡇⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠸⠸⡌⢸⣿⡿⢦⣄⢀⢱⢸⠀⣦⢻⢿⡀⡞⠥⢼⣄⠀⢸⠀⢸⠃⠈⣿⠀⢰⠀⢠⢰⢻⠀⢸⢀⠀⠀⣇⢧⠀⠸⡆⡇⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡸⡇⢸⢹⣧⠸⠿⣿⣝⢮⡄⠹⡄⢸⢿⢄⠀⠈⢯⠉⣿⢄⡞⢠⡀⡇⠀⡟⠀⠸⢘⠀⢇⠘⡿⡆⠀⢸⠘⡀⠀⢡⡇⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⡇⢸⢸⠈⢻⡦⣿⡟⠈⢿⡸⣇⡟⡇⢀⡥⠤⣘⡆⡿⢀⢿⠺⢃⡇⢠⡇⠀⢠⡇⠀⠈⢦⢷⡘⢄⠀⢧⠱⡀⠀⢃⠀⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⣷⡁⣼⢸⠀⠀⠉⠙⠁⠀⠀⠑⢟⠇⠁⠞⠛⣿⣿⣿⣷⣼⣘⡄⢸⠀⣼⠀⠀⢸⢇⢠⣄⢸⠻⣏⠪⢧⡄⢣⠹⣆⠈⢧⠀⠀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡄⣿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠘⡷⣼⣯⡇⠉⣻⣗⡆⢠⡏⠀⠀⡞⠘⣜⡈⢦⡆⣬⡧⡄⡜⠧⣓⣘⣆⠀⢣⡀⠀⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⢧⢻⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠚⠓⠋⠀⢸⠃⡼⠀⠀⢠⡇⠀⢹⡇⢨⢧⢁⠀⠈⢽⡀⠉⠘⢶⠑⢄⠱⡄⠀┃
    ┃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⣿⣸⢸⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢰⡇⠀⠀⣾⠇⠀⢸⡱⡼⡌⡞⡆⠀⠀⠻⣄⠀⠈⢧⠀⠳⡌⢆┃
    ┃⠀⢀⠄⢤⣰⠛⡄⠀⠀⠀⠀⠀⠀⠀⠀⡼⣝⡏⡏⠈⡄⢸⣞⢆⠀⠘⣷⢆⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⡜⠀⠀⢠⢻⡀⠀⣿⣧⠃⠹⡜⢾⡄⠀⡀⠈⢢⡀⠈⢆⠀⠈⢢┃
    ┃⠀⣸⣠⢤⣈⡱⡜⡆⠀⠀⠀⠀⠀⠀⠠⢱⡿⢠⠃⠀⣷⢸⢻⣆⠣⡀⠈⠒⠤⠀⠯⠟⠀⠀⠀⠀⠀⠀⢀⡿⢰⠇⠀⠀⣼⠈⣿⣀⢿⣿⣀⠀⠙⢮⣻⣄⠱⡄⠀⠙⠂⠈⢦⠀⠀┃
    ┃⠈⣀⣠⡴⠳⣄⡷⠸⡄⠀⠀⠀⠀⠀⢀⢣⠇⢸⠀⠀⢸⢸⠀⠙⠣⣽⣦⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠒⠉⠃⡎⡄⠀⢀⢱⠀⢫⢹⢾⣜⢮⡑⠢⠤⠭⣟⡷⢝⣦⡀⠀⠀⠀⠣⡀┃
    ┃⢀⣀⣠⡛⢆⡘⠁⠀⢫⢷⡀⠀⠀⠀⡜⣾⠀⢸⠀⠀⠀⣾⠀⠀⡘⢸⠀⠑⠒⣶⠖⣏⢩⠙⠢⡀⠀⠀⣸⣸⢻⠁⠀⡼⡿⠀⠈⢎⢣⠻⡿⠟⠓⠋⠁⠀⣀⣀⠒⢮⣵⣄⠀⠀⠐┃
    ┃⠀⠠⠚⠱⣴⢳⠀⠀⢸⡎⣇⠀⠀⢰⣰⡟⠀⢸⠀⠀⠀⠸⡀⢠⠇⣘⠀⠀⢰⠻⠸⡘⡛⢄⠀⠈⠂⠀⡇⡏⣬⠀⢠⠃⡇⡀⠀⠈⢳⣕⣿⣦⣶⣾⠷⠛⠉⢀⡠⠤⠹⢯⢧⠀⠀┃
    ┃⣷⠩⠟⠒⠁⠙⠀⢀⠟⠀⢸⢣⣠⢯⣇⡇⠀⢸⠀⠀⠀⠀⣇⡌⢠⠘⢇⠀⢸⠀⠀⢣⠙⣗⠑⢄⠀⢸⣸⣼⡛⠀⠸⠀⡇⢧⢀⡰⢋⢃⠃⠁⠠⠊⠀⣠⠖⠁⠀⠀⠀⠀⢎⣇⠀┃
    ┃⡵⣑⣄⠀⠤⠔⠊⠁⠀⠀⡜⠀⢹⡿⢿⡇⠀⢸⠀⠀⠀⠀⣏⢇⠈⢣⡘⡀⢸⡄⠀⠀⢳⡈⠳⢄⣁⣾⢯⢧⠇⠀⡆⢀⠀⢸⣏⠔⠹⡼⠀⡷⠁⢠⠞⠁⠀⠀⠀⠀⠀⠀⠸⡇⠉┃
      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱⋆⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""",1)

class tools():

    def clear_goback():
        os.system("clear")
        main()

    def clear_return_to_main_title():
        os.system("clear")
        print("{}".format(Arts.girl))

    def save_file_or_pass(output ,ip_address):
        
        file_name=Write.Input("\n file output name >> ",Colors.red_to_purple,interval=0.0200)
        if file_name:
            usr = Write.Input(Arts.line+"\nScan results will be saved as {}\nPress any key to continue".format(file_name), Colors.red_to_purple, interval=0.0100)
            with open ("output {}.txt".format(file_name),"w")as file:
                file.write(output)

            def update():
                if usr:
                    tools.clear_goback()
            update()

        else:
            usr = Write.Input(Arts.line+"\nScan results will be saved as text file and it will replace the prev file\nPress any key to continue", Colors.red_to_purple, interval=0.0100)
            with open ("output {} os-scan-guess.txt".format(ip_address),"w")as file:
                file.write(output.stdout)

            def update():
                if usr:
                    tools.clear_goback()
            
            update()

    def Enter_info(call_Function,other_args=None,usrs_path=None,pass_path=None,usr_string=None,pass_string=None):

        ip = Write.Input("\nip address >> ", Colors.red_to_purple, interval=0.0200)
        if ip=="" or ip==" ":
            Write.Print("\n( ! ) Error!, example: 192.168.0.1\n",Colors.red_to_purple, interval=0.0100)
            time.sleep(3)
            tools.clear_goback()

        elif ip:
            tools.clear_return_to_main_title()
            if call_Function =="os_scan":
                #T3 is the default speed for nmap, tried with T2 and i took almost 4h and it was a local host.
                # yeah ik its not a real progress bar, still count tho.
                Write.Print("\n( i ) trying to get the oprating system -> "+ip+"\n",Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="OS-SCAN GUESS IS DONE FOR",arg1="-O",arg2="-p",arg3="1-65535",arg4="-sV",arg5="-sS",arg6="--osscan-guess",arg7="--max-os-tries",arg8="20")

            elif call_Function=="port_scan":
                Write.Print("\n( i ) this scan might take up to 10min please be patient\n( i ) Scanning open ports and service versions -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                #["nmap","-Pn","-p-","-sV","--allports","--version-intensity","9","--version-all","--open","-sS","{}".format(ip_address)],
                tools.sub_(tool="nmap",ip_add=ip,title="PORT SCAN IS DONE FOR",arg1="-p-",arg2="-sV",arg3="--allports",arg4="--version-intensity",arg5="9",arg6="--version-all",arg7="--open",arg8="-sS")
                
            elif call_Function=="live_host":
                Write.Print("\n( i ) scanning for live hosts -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip+"/24",title="LIVE HOSTS SCAN IS DONE FOR",arg1="-n")

            elif call_Function=="smb-os-discovery":
                Write.Print("\n( i ) running smb-os-discovery.nse script -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="smb-os-discovery SCRIPT IS DONE",arg1="-sU",arg2="-sS",arg3="--script",arg4="smb-os-discovery.nse",arg5="-p",arg6="U:137",arg7="T:139")
                #tools.sub_(ip_add=ip,title="smb-os-discovery SCRIPT IS DONE",arg1="--script",arg2="smb-os-discovery.nse")

            elif call_Function=="default_script":
                Write.Print("\n( i ) running default script scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="DEFAULT SCRIPT SCAN IS DONE FOR",arg1="-sV",arg2="-sC")

            elif call_Function=="tcp_syn_port_scan":
                Write.Print("\n( i ) running tcp syn port scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="TCP SYN PORT SCAN IS DONE",arg1="-sS",arg2="-p",arg3="1-1024")
            
            elif call_Function=="tcp_ack_scan":
                if other_args:
                    Write.Print("\n( i ) running tcp ack scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title=f"TCP ACK PORT SCAN ON {other_args} IS DONE",arg1="-sA",arg2="-p",arg3=other_args)
                elif other_args is not None:
                    Write.Print("\n( i ) running tcp ack scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title="TCP ACK PORT SCAN ON 1-1024 IS DONE",arg1="-sA",arg2="-p",arg3="1-1024")
            
            elif call_Function=="tcp_connect_port_scan":
                if other_args:
                    Write.Print("\n( i ) running tcp connect port scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title=f"TCP CONNECT PORT SCAN ON {other_args} IS DONE",arg1="-sT",arg2="-p",arg3=other_args)
                elif other_args is not None:
                    Write.Print("\n( i ) running tcp connect port scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title="TCP CONNECT PORT SCAN ON 1-1024 IS DONE",arg1="-sT",arg2="-p",arg3="1-1024")
            
            elif call_Function=="tcp_fin_scan":
                if other_args:
                    Write.Print("\n( i ) running tcp fin scan (-sF) -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title=f"TCP FIN SCAN ON {other_args} IS DONE",arg1="-sF",arg2="-p",arg3=other_args)
                elif other_args is not None:
                    Write.Print("\n( i ) running tcp fin scan (-sF) -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title="TCP FIN SCAN ON 1-1024 IS DONE",arg1="-sF",arg2="-p",arg3="1-1024")
            
            elif call_Function=="list_scan":
                Write.Print("\n( i ) running list scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="LIST SCAN IS DONE FOR ",arg1="-sL")
            
            elif call_Function=="udp_port_scan":
                if other_args:
                    Write.Print("\n( i ) running udp port scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title=f"UDP PORT SCAN ON {other_args} IS DONE",arg1="-sU",arg2="-p",arg3=other_args)
                elif other_args is not None:
                    Write.Print("\n( i ) running udp port scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                    tools.sub_(tool="nmap",ip_add=ip,title="UDP PORT SCAN ON 1-1024 IS DONE",arg1="-sU",arg2="-p",arg3="1-1024")

            elif call_Function=="ping_scan":
                Write.Print("\n( i ) running ping scan -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="PING SCAN IS DONE FOR ",arg1="-sn")
            
            elif call_Function=="SSH_auth":
                Write.Print("\n( i ) running SSH authentication methods -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="SSH authentication methods is done for ",arg1="-p",arg2="22",arg3="--script",arg4="ssh-auth-methods")
            
            elif call_Function=="Brute-Force_SSH_Authentication": #default is 7s
                if usrs_path and pass_path:
                    try:
                        Write.Print("( * )looking for:"+usrs_path +" & "+ pass_path,Colors.red_to_purple)
                        os.system(f"cat {usrs_path}")
                        os.system(f"cat {pass_path}")
                        tools.clear_return_to_main_title()

                        Write.Print("\n( * ) File Found!",Colors.green_to_blue)
                        Write.Print("\n( i )  running Brute-Force SSH Authentication -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="nmap",ip_add=ip,title="Brute-Force SSH Authentication is done for ",arg1="-p",arg2="22",arg3="--script",arg4="ssh-brute",arg5="--script-args",arg6=f"userdb={usrs_path}",arg7=f",passdb={pass_path}",arg8=",ssh-brute.timeout=4s")

                    except FileNotFoundError:
                        Write.Print("\n( ! )  File not found! running with default user/pass lists",Colors.red_to_purple,interval=0.0100)
                        Write.Print("\n( i )  running Brute-Force SSH Authentication -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="nmap",ip_add=ip,title="Brute-Force SSH Authentication is done for ",arg1="-p",arg2="22",arg3="--script",arg4="ssh-brute",arg5="--script-args",arg6="userdb=usernames.lst",arg7=",passdb=passwords.lst",arg8=",ssh-brute.timeout=7s")
                else:
                    Write.Print("\n( i )  running Brute-Force SSH Authentication -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100) 
                    tools.sub_(tool="nmap",ip_add=ip,title="Brute-Force SSH Authentication is done for ",speed="start",arg1="-p",arg2="22",arg3="--script",arg4="ssh-brute",arg5="--script-args",arg6="userdb=usernames.lst",arg7=",passdb=passwords.lst",arg8=",ssh-brute.timeout=7s")
                
            elif call_Function=="Enumerate_SMB_shares_with_authentication":
                    
                    if usr_string and pass_string is not None:
                        Write.Print(f"\n( i )  running Enumerate SMB shares with authentication {usr_string} pass is {pass_string} -> {ip}",Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="nmap",ip_add=ip,title="Enumerate SMB shares with authentication is done for ",arg1="-p",arg2="445",arg3="--script",arg4="smb-enum-shares",arg5="--script-args",arg6=f"'smbuser={usr_string}",arg7=f"smbpass={pass_string}'")
                    else:      
                        Write.Print("\n( i )  running Enumerate SMB shares with authentication -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="nmap",ip_add=ip,title="Enumerate SMB shares with authentication is done for ",arg1="-p",arg2="445",arg3="--script",arg4="smb-enum-shares")
            
            elif call_Function=="Brute-Force_smb_Authentication":
                    if usr_string and pass_string:
                        Write.Print(f"\n( i ) running BruteForce smb Authentication with login name as {usr_string} & passlist is {pass_string} -> {ip}",Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="hydra",ip_add=f"smb://{ip}",title="BruteForce smb Authentication is done for ",arg1="-l",arg2=usr_string,arg3="-P",arg4=pass_string)
                    elif usr_string:
                        Write.Print(f"\n( i ) running BruteForce smb Authentication with login name as {usr_string} & passlist is default -> {ip}",Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="hydra",ip_add=f"smb://{ip}",title="BruteForce smb Authentication is done for ",arg1="-l",arg2=usr_string,arg3="-P",arg4="passwords.lst")
                    elif pass_string:
                        Write.Print(f"\n( i ) running BruteForce smb Authentication with login name as root & passlist is {pass_string} -> {ip}",Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="hydra",ip_add=f"smb://{ip}",title="BruteForce smb Authentication is done for ",arg1="-l",arg2="root",arg3="-P",arg4=pass_string)
                    else:
                        Write.Print(f"\n( i ) running BruteForce smb Authentication using hydra -> {ip}",Colors.red_to_purple,interval=0.0100)
                        tools.sub_(tool="hydra",ip_add=f"smb://{ip}",title="BruteForce smb Authentication is done for ",arg1="-l",arg2="root",arg3="-P",arg4="passwords.lst")
            
            elif call_Function=="Check_for_SMB_vulnerabilities":
                Write.Print("\n( i )  running SMB vulnerabilities script -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="SMB vulnerabilities scan is done for ",arg1="-p",arg2="445",arg3="--script",arg4="smb-vuln*")
            
            elif call_Function=="http-auth (no args).":
                Write.Print("\n( i )  running http-auth script -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="http-auth scan is done for ",arg1="-p",arg2="80",arg3=",",arg4="443",arg5="-sV",arg6="--script",arg7="http-auth")

            elif call_Function=="HTTP_methods":
                Write.Print("\n( i )  running HTTP methods script -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="HTTP auth methods script (using .retest) is done for ",arg1="--script",arg2="http-methods",arg3="--script-args",arg4="http-methods.retest")

            elif call_Function=="http-auth-finder":
                Write.Print("\n( i )  running http-auth-finder script -> {}\n".format(ip),Colors.red_to_purple,interval=0.0100)
                tools.sub_(tool="nmap",ip_add=ip,title="http-auth-finder script is done for ",arg1="-p",arg2="80",arg4="--script",arg5="http-auth-finder")

        # nmap -p 80 --script http-brute --script-args http-brute.firstOnly=true,http-brute.mode=user,http-brute.path="/login.php" testphp.vulnweb.com


        else:                   
            tools.clear_return_to_main_title()
            print("( ! ) error!, can't use int..")
            time.sleep(2)
            tools.clear_goback()

    def sub_(tool,ip_add,title,speed=None,arg1=None,arg2=None,arg3=None,arg4=None,arg5=None,arg6=None,arg7=None,arg8=None,arg9=None,arg10=None):

        try:
            if speed is not None:
                s=0.005
            else:
                s=0.0100

            args = [arg for arg in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10] if arg is not None]
            args.append(str(ip_add))
            output = subprocess.run([tool]+args,text=True,capture_output=True)

            tools.clear_return_to_main_title()
            Write.Print(f"\n{title}{ip_add}\n{Arts.line}\n{output.stdout}",Colors.cyan_to_blue, interval=s)
            tools.save_file_or_pass(output=output.stdout, ip_address=ip_add)

        except Exception as e:
            Write.Print(f"( ! ) ERROR! {e}",Colors.red_to_purple,interval=0.0200)
            exit()

def main():
    if 1 == 10:
        print("pass")
    else:
        while 1:
            try:
                System.Clear()
                print("{}".format(Arts.girl)+"\n"+Arts.basic_scanners+"\n"+Arts.number1+"\n"+Arts.number2+"\n"+Arts.number3+"\n"+Arts.number4+"\n"+Arts.number5+"\n"+Arts.scanning_types
                      +"\n"+Arts.number6+"\n"+Arts.number7+"\n"+Arts.number8+"\n"+Arts.number9+"\n"+Arts.number10+"\n"+Arts.number11+"\n"
                      +Arts.number12+"\n"+"\n"+Arts.other_scans+"\n"+Arts.cat_1+"\n"+Arts.number13+"\n"+Arts.number14+"\n"+Arts.cat_2+"\n"+Arts.number15
                      +"\n"+Arts.number16+"\n"+Arts.number17+"\n"+Arts.cat_3+"\n"+Arts.number18+"\n"+Arts.number19+"\n"+Arts.number20+"\n"+Arts.number21
                      +"\n"+Arts.number22+"\n"+Arts.number23+"\n"+Arts.number24+"\n"+Arts.number25+"\n"+Arts.number26+"\n"+Arts.number27+"\n"+Arts.number28
                      +"\n"+Arts.number29+"\n"+Arts.number30+"\n"+Arts.number31+"\n"
                      )
                usr=Write.Input("\n>> ",Colors.red_to_purple, interval=0.0100)
                usr=int(usr)

                if usr==1:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("os_scan")

                elif usr==2:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("port_scan")

                elif usr==3:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("default_script")

                elif usr==4:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("smb-os-discovery")

                elif usr==5:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("live_host")

                elif usr==6:
                    tools.clear_return_to_main_title()
                    ports_ = Write.Input("\nset ports (default is 1-1024) example: 1-21 >> ", Colors.red_to_purple, interval=0.0200)
                    tools.Enter_info("tcp_syn_port_scan",other_args=ports_)

                elif usr==7:
                    tools.clear_return_to_main_title()
                    ports_ = Write.Input("\nset ports (default is 1-1024) example: 1-22 >> ", Colors.red_to_purple, interval=0.0200)
                    tools.Enter_info("tcp_ack_scan",other_args=ports_)

                elif usr==8:
                    tools.clear_return_to_main_title()
                    ports_ = Write.Input("\nset ports (default is 1-1024) example: 1-22 >> ", Colors.red_to_purple, interval=0.0200)
                    tools.Enter_info("tcp_connect_port_scan",other_args=ports_)

                elif usr==9: 
                    tools.clear_return_to_main_title()
                    ports_ = Write.Input("\nset ports (default is 1-1024) example: 1-22 >> ", Colors.red_to_purple, interval=0.0200)
                    tools.Enter_info("tcp_fin_scan",other_args=ports_)

                elif usr==10:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("list_scan")
                    
                elif usr==11:
                    tools.clear_return_to_main_title()
                    ports_ = Write.Input("\nset ports (default is 1-1024) example: 1-22 >> ", Colors.red_to_purple, interval=0.0200)
                    tools.Enter_info("udp_port_scan",other_args=ports_)

                elif usr==12:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("ping_scan")

                elif usr==13:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("SSH_auth")

                elif usr==14:
                    tools.clear_return_to_main_title()
                    userlist_path=Write.Input("\n( i ) don't have one? get one https://github.com/jeanphorn/wordlist/tree/master or https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials for bigger lists\n\nset usrs list path (default is usernames.lst) example: /path/to/users.lst >> ", Colors.red_to_purple, interval=0.0100)
                    passlist_path=Write.Input("set passwords list path (default is passwords.lst) example: /path/to/passwords.lst >> ", Colors.red_to_purple, interval=0.0100)
                    tools.clear_return_to_main_title()
                    tools.Enter_info("Brute-Force_SSH_Authentication",usrs_path=userlist_path,pass_path=passlist_path)

                elif usr==15:
                    tools.clear_return_to_main_title()
                    usr_st=Write.Input("\nset credentials username (optional) >> ", Colors.red_to_purple, interval=0.0100)
                    pass_st=Write.Input("set credentials password (optional) >> ", Colors.red_to_purple, interval=0.0100)
                    tools.clear_return_to_main_title()
                    tools.Enter_info("Enumerate_SMB_shares_with_authentication",usr_string=usr_st,pass_string=pass_st)

                elif usr==16:
                    tools.clear_return_to_main_title()
                    usr_st=Write.Input("\n( i ) don't have one? get one https://github.com/jeanphorn/wordlist/tree/master or https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials for bigger lists\n\nset username (default is root) >> ", Colors.red_to_purple, interval=0.0100)
                    pass_st=Write.Input("set passwords list path (default is passwords.lst) example: /path/to/passwords.lst >> ", Colors.red_to_purple, interval=0.0100)
                    tools.clear_return_to_main_title()
                    tools.Enter_info("Brute-Force_smb_Authentication",usr_string=usr_st,pass_string=pass_st)

                elif usr==17:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("Check_for_SMB_vulnerabilities")

                elif usr==18:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("http-auth")
                
                elif usr==19:
                    tools.clear_return_to_main_title()
                    tools.Enter_info("HTTP_methods")

                elif usr==20:
                    tools.clear_return_to_main_title() 
                    tools.Enter_info("http-auth-finder")

                else:
                    tools.clear_goback()

            except KeyboardInterrupt:
                try:
                    tools.clear_return_to_main_title()
                    usr=Write.Input("\nare you sure you want to exit? (y/n) >> ",Colors.red_to_purple ,interval=0.0100)
                    if usr =="yes" or usr=="y" or usr=="yep" or usr=="YES" or usr=="Y" or usr=="yea":
                        Write.Print("\nExit!\n",Colors.red_to_purple,interval=0.030)
                        quit()
                    elif usr =="no" or usr=="n" or usr=="nope" or usr=="NO" or usr=="N" or usr=="nah":
                        tools.clear_goback()
                    else:
                        tools.clear_goback()
                except KeyboardInterrupt:
                    quit()

            except ValueError as e:
                try:
                    Write.Print("\n( ! ) Error: {}".format(e),Colors.red_to_purple,interval=0.0100)
                    time.sleep(0.80)
                    tools.clear_goback()
                except KeyboardInterrupt:
                    tools.clear_goback()

if __name__=="__main__":
    main()
