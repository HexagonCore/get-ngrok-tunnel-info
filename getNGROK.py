import json
import requests
import time

#!------------------------!
#!    Start of getNGROK   !
#!------------------------!

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels/"
    tunnel_name = "command_line"
    time.sleep(0.01)
    cls()
    print("Getting Ngrok stats..")
    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == tunnel_name:
                cls()
                print("Getting Ngrok stats...")
                return i['public_url']
                break
    except:
        err = 1
        
def get_stats_n():
    global ngr
    global err
    global ip
    global port
    err = 0
    cls()
    print("Getting Ngrok stats.")
    ngr = get_ngrok_url()
    time.sleep(0.01)
    cls()
    try:
        ngr = ngr.replace("tcp://", "")
    except:
        err = 1
        cls()
        print("Error: wrong tunnel name configured or no tunnel is running")
    if err == 0:
        ngr = ngr.split(":")
        ip = ngr[0]
        port = ngr[1]
        print("IP:  ", ip)
        print("PORT:", port)
    

def cls():
    for i in range(2):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    

# ˇThis function actually gets the stats, you can use it anywhereˇ
#-----------------------------------------------------------------#
get_stats_n()
#-----------------------------------------------------------------#
# ^This function actually gets the stats, you can use it anywhere^ 



#!------------------------!
#!    End of getNGROK     !
#!------------------------!


#!------------------------!
#!   Ur code goes below   !
#!------------------------!

print(Hello world!)
