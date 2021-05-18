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

lvers = "1.0.13"


def checkver():
    packagenm = 'ngrok_info'
    responseinfl = requests.get(f'https://pypi.org/pypi/{packagenm}/json')
    latest_version = responseinfl.json()['info']['version']
    if latest_version != lvers:
        print("You are not using latest version, run 'python3 -m pip install --upgrade ngrok_info'")

checkver()

#last line deletion
def delete_last_line():
    pass

def err_gtngr_do_not_use_for_urself():
    delete_last_line()
    print("Error: wrong tunnel name specified or no tunnel is running\n")

def gtngr_do_not_use_for_urself():
    url = "http://localhost:4040/api/tunnels/"
    tunnel_name = par_tnl
    print(tunnel_name)
    print(tunnel_name)
    print(tunnel_name)
    

    time.sleep(0.01)
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




def get(tnl_nm = "command_line"):
    global ngr
    global err
    global tnl_type
    global ip
    global port
    global adress
    global par_tnl
    par_tnl = tnl_nm
    err = 0
    print('Getting Ngrok stats from tunnel "{}"..'.format(par_tnl))
    ngr = gtngr_do_not_use_for_urself()
    time.sleep(0.01)
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
            print("NAME:  ", par_tnl)
            print("TYPE:  ", tnl_type)
            print("ADRESS:", adress)
            print("IP:    ", ip)
            print("PORT:  ", port)
            print("")
            
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
            print("NAME:  ", par_tnl)
            print("TYPE:  ", tnl_type)
            print("ADRESS:", adress)
            print("IP:    ", ip, "\n")
    

    
#!------------------------------!
#!       End of getNGROK        !
#!                              !
#!------------------------------!

