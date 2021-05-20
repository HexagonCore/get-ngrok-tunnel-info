## -------------------------------------------------- ##
##    So you are checking my code? Have a nice day!   ##
##    Check out http://is.gd/duhovavoda               ##
## -------------------------------------------------- ##
import socket
import json
import requests
import os 
import sys
import time


#!------------------------------!
#! Start of getNGROK functions  !
#!                              !
#!------------------------------!

lvers = "1.1.15"


def checkver():
    packagenm = 'ngrok_info'
    responseinfl = requests.get(f'https://pypi.org/pypi/{packagenm}/json')
    latest_version = responseinfl.json()['info']['version']
    if latest_version != lvers:
        print("You are not using latest version, run 'python3 -m pip install --upgrade ngrok_info' three times")

checkver()
notext = 0
#last line deletion
def delete_last_line():
    pass


    
def gtngr_do_not_use_for_urself():
    url = "http://localhost:4040/api/tunnels/"
    tunnel_name = par_tnl
    

    delete_last_line()
    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == tunnel_name:
                delete_last_line()
                return i['public_url']
                break
    except:
        err = 1



def get_notext(tunnm = "command_line"):
    global notext
    notext = 1
    gtfun(tunnm)
    
def get(tunnm = "command_line"):
    global notext
    notext = 0
    gtfun(tunnm)


def gtfun(tnl_nm = "command_line"):
    global ngr
    global err
    global tnl_type
    global tnl_name
    global ip
    global port
    global adress
    global par_tnl
    global notext
    par_tnl = tnl_nm
    err = 0
    if notext == 0:
        print('Getting Ngrok stats from tunnel "{}"..'.format(par_tnl))
    ngr = gtngr_do_not_use_for_urself()
    tcp = 5
    try:
        if ngr.find("tcp://") != -1:
            tcp = 1
        else:
            tcp = 0
    except:
        err_gtngr_do_not_use_for_urself()
    
    if tcp == 1:
        try:
            ngr = ngr.replace("tcp://", "")
        except:
            err = 1
            err_gtngr_do_not_use_for_urself()
            adress = "ERR"
            ip = "ERR"
            port = "ERR"
            tnl_type = "ERR"
        if err == 0:
            ngr = ngr.split(":")
            adress = ngr[0]
            port = ngr[1]
            tnl_type = "TCP"
            try:
                ip = socket.gethostbyname(adress)
            except:
                ip = "ERR NO CONNECTION"
                tnl_type = "TCP (no connection)"
            delete_last_line()
            tnl_name = par_tnl
            if notext == 0:
                print("NAME:  ", par_tnl)
                print("TYPE:  ", tnl_type)
                print("ADRESS:", adress)
                print("IP:    ", ip)
                print("PORT:  ", port)
                print("")
                print("Variables, you can acess in your code and are for TCP are: 'ngrok_info.tnl_name', 'ngrok_info.tnl_type', 'ngrok_info.adress', 'ngrok_info.ip', 'ngrok_info.port'")
    if tcp == 0:
        try:
            ngr = ngr.replace("https://", "")
        except:
            err = 1
            err_gtngr_do_not_use_for_urself()
            adress = "ERR"
            ip = "ERR"
            port = "ERR"
            tnl_type = "ERR"
        if err == 0:
            adress = ngr
            tnl_type = "HTTPS"
            try:
                ip = socket.gethostbyname(adress)
            except:
                ip = "ERR NO CONNECTION"
                tnl_type = "HTTPS (no connection)"
            delete_last_line()
            tnl_name = par_tnl
            port = "NONE"
            if notext == 0:
                print("NAME:  ", par_tnl)
                print("TYPE:  ", tnl_type)
                print("ADRESS:", adress)
                print("IP:    ", ip, "\n")
                print("")
                print("Variables, you can acess in your code and are for HTTPS are: 'ngrok_info.tnl_name', 'ngrok_info.tnl_type', 'ngrok_info.adress', 'ngrok_info.ip'")
    
def err_gtngr_do_not_use_for_urself():
    global notext
    global tnl_name
    global par_tnl
    global tnl_type
    global port
    global ip
    global adress
    delete_last_line()
    if notext == 0:
        print("Error: wrong tunnel name specified or no tunnel is running\n")
    tnl_name = "ERR"
    par_tnl = "ERR"
    tnl_type = "ERR"
    port = "ERR"
    ip = "ERR"
    adress = "ERR"
    notext = 0

    
#!------------------------------!
#!       End of getNGROK        !
#!                              !
#!------------------------------!

