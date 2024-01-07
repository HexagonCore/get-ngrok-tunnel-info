## -------------------------------------------------- ##
##    So you are checking my code? Have a nice day!   ##
##    Check out http://is.gd/duhovavoda               ##
## -------------------------------------------------- ##
import socket
import json
import requests

# JAN/7/2024
# Ok so this code is absolutely terrible and relies on the global keyword but it works so let's not change it

silent = True
updated = False

#!------------------------------!
#! Start of getNGROK functions  !
#!------------------------------!

__version__ = "develop"


def allow_update():
    global silent
    global updated
    silent = False
    if updated == False:
        updated = True
        checkver()


def not_silent():
    allow_update()


def is_online():
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close()
        return True
    except OSError:
        pass
    return False


def checkver():
    if is_online() == True:
        packagenm = 'input_num'
        latest_version = "ERR"
        responseinfl = requests.get(f'https://pypi.org/pypi/{packagenm}/json')
        latest_version = responseinfl.json()['info']['version']
        if latest_version != __version__:
            if silent == False:
                print(
                    f"[{packagenm}] New update is here, run 'python3 -m pip install --upgrade input_num' TWO TIMES in normal terminal")


notext = False


def gtngr_do_not_use_for_urself():
    global err
    url = "http://localhost:4040/api/tunnels/"
    tunnel_name = par_tnl

    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == tunnel_name:
                return i['public_url']
    except:
        err = True
        return None


def get_notext(tunnm="command_line"):
    global notext
    notext = True
    gtfun(tunnm)


def get(tunnm="command_line"):
    global notext
    notext = False
    gtfun(tunnm)


def gtfun(tnl_nm="command_line"):
    global ngr
    global err
    global tnl_type
    global tnl_name
    global ip
    global port
    global adress
    global address
    global par_tnl
    global notext
    par_tnl = tnl_nm
    err = False
    if notext == False:
        print('Getting Ngrok stats from tunnel "{}"..'.format(par_tnl))

    ngr = gtngr_do_not_use_for_urself()

    tcp = -1
    try:
        if "tcp://" in ngr:
            tcp = 1
        else:
            tcp = 0
    except:
        err_gtngr_do_not_use_for_urself()

    if tcp == 1:
        try:
            ngr = ngr.replace("tcp://", "")
        except:
            err = True
            err_gtngr_do_not_use_for_urself()
        if not err:
            ngr = ngr.split(":")
            adress = address = ngr[0]
            port = ngr[1]
            tnl_type = "TCP"
            try:
                ip = socket.gethostbyname(address)
            except:
                ip = "ERR NO CONNECTION"
                tnl_type = "TCP (no connection)"
            tnl_name = par_tnl
            if notext == False:
                print("NAME:   ", par_tnl)
                print("TYPE:   ", tnl_type)
                print("ADDRESS:", address)
                print("IP:     ", ip)
                print("PORT:   ", port)
                print("")
                print("Variables, you can acess in your code and are for TCP are: 'ngrok_info.tnl_name', 'ngrok_info.tnl_type', 'ngrok_info.address', 'ngrok_info.ip', 'ngrok_info.port'")
    if tcp == 0:
        try:
            ngr = ngr.replace("https://", "")
        except:
            err = True
            err_gtngr_do_not_use_for_urself()
        if not err:
            adress = address = ngr
            tnl_type = "HTTPS"
            try:
                ip = socket.gethostbyname(address)
            except:
                ip = "ERR NO CONNECTION"
                tnl_type = "HTTPS (no connection)"
            tnl_name = par_tnl
            port = None
            if notext == False:
                print("NAME:   ", par_tnl)
                print("TYPE:   ", tnl_type)
                print("ADDRESS:", address)
                print("IP:     ", ip)
                print("")
                print("Variables, you can acess in your code and are for HTTPS are: 'ngrok_info.tnl_name', 'ngrok_info.tnl_type', 'ngrok_info.address', 'ngrok_info.ip'")


def err_gtngr_do_not_use_for_urself():
    global notext
    global tnl_name
    global par_tnl
    global tnl_type
    global port
    global ip
    global adress
    global address
    if notext == False:
        print("Error: wrong tunnel name specified or no tunnel is running\n")
    tnl_name = par_tnl = tnl_type = port = ip = adress = address = "ERR"
    notext = False


#!------------------------------!
#!       End of getNGROK        !
#!------------------------------!
