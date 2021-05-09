import socket
import json
import requests
import os 
import sys
import time

#!-------------------------!
#!    Start of getNGROK    !
#! Please scroll to bottom !
#!-------------------------!


#last line deletion
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')



def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels/"
    tunnel_name = "command_line"
    time.sleep(0.01)
    delete_last_line()
    print("Getting Ngrok stats..")
    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == tunnel_name:
                delete_last_line()
                print("Getting Ngrok stats...")
                return i['public_url']
                break
    except:
        err = 1




def get_stats_n():
    global ngr
    global err
    global tnl_type
    global ip
    global port
    global adress
    err = 0
    print("Getting Ngrok stats.")
    ngr = get_ngrok_url()
    time.sleep(0.01)
    tcp = 5
    try:
        if ngr.find("tcp://") != -1:
            tcp = 1
        else:
            tcp = 0
    except:
        delete_last_line()
        print("Error: wrong tunnel name configured or no tunnel is running")
    
    if tcp == 1:
        try:
            ngr = ngr.replace("tcp://", "")
        except:
            err = 1
            delete_last_line()
            print("Error: wrong tunnel name configured or no tunnel is running")
            adress = ""
            ip = ""
            port = ""
        if err == 0:
            ngr = ngr.split(":")
            adress = ngr[0]
            port = ngr[1]
            ip = socket.gethostbyname(adress)
            delete_last_line()
            tnl_type = "TCP"
            print("TYPE:  ", tnl_type)
            print("ADRESS:", adress)
            print("IP:", ip)
            print("PORT:", port)
            
    if tcp == 0:
        try:
            ngr = ngr.replace("https://", "")
        except:
            err = 1
            delete_last_line()
            print("Error: wrong tunnel name configured or no tunnel is running")
            adress = ""
            ip = ""
            port = ""
        if err == 0:
            adress = ngr
            ip = socket.gethostbyname(adress)
            delete_last_line()
            tnl_type = "HTTPS"
            print("TYPE:", tnl_type)
            print("ADRESS:", adress)
            print("IP:", ip)
    

    
#!------------------------!
#!    End of getNGROK     !
#!   Ur code goes below   !
#!------------------------!



# ˇThis function actually gets the stats, you can use it anywhereˇ
#-----------------------------------------------------------------#
get_stats_n()
#-----------------------------------------------------------------#
# ^This function actually gets the stats, you can use it anywhere^ 

print("Hello world!")