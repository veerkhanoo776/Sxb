import os,json,hashlib,io,struct
os.system('clear')
#print('\n\n Checking for modules! ')
print(' ')

import os, requests, re, time, sys, random, json
from concurrent.futures import ThreadPoolExecutor as Thread
import re,uuid,sys,random,time,os,subprocess,platform
try:
    from bs4 import BeautifulSoup as sp
    from concurrent.futures import ThreadPoolExecutor as Thread
    import requests
except:
    os.system('pip install bs4 fake_email futures requests ')
    from bs4 import BeautifulSoup as sp
    from fake_email import Email
    from concurrent.futures import ThreadPoolExecutor as Thread
    import requests
import urllib.request
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor

'''-------#clour#------'''

whi = "\033[1;97m"
yal = "\033[1;93m"

ok=0

def linex():
    print(f'\033[1;97m--------------------------------------------')

tm=[]
print("""\033[1;33m[•] \033[1;32mCoded By KHALFAN AXI \033[1;37m""");linex()





def gri():
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip_address

def rnd(a,b):
    return str(random.randint(a,b))





def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx



oks=[]

def Main():
    #clr()
    print(f'{whi}[1] Add friends request\n[2] Accept friend request\n[0] Exit menu ')
    linex()
    user=input('Select Option: ')
    if user=="1":
        get_file()
    elif user=="2":
        get_filev2()
    elif user=="0":
        exit("Thanks for use ")
    else:
        Main()

def getdata(req):
    try:
        act = re.search('"actorID":"(.*?)"',str(req)).group(1)
        hst = re.search('"haste_session":"(.*?)",',str(req)).group(1)
        rev = re.search('{"rev":(.*?)}',str(req)).group(1)
        hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
        dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
        jzt = re.search('&jazoest=(.*?)",',str(req)).group(1)
        lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
        spr = re.search('"__spin_r":(.*?),',str(req)).group(1)
        spt = re.search('"__spin_t":(.*?),',str(req)).group(1)
        dta = {'av':act, '__user':act, '__a':'1', '__hs':hst, 'dpr':'1.5', '__ccg':'EXCELLENT', '__rev':rev, '__hsi':hsi, '__comet_req':'15', 'fb_dtsg': dts, 'jazoest': jzt, 'lsd': lsd, '__spin_b':'trunk', '__spin_r':spr, '__spin_t':spt}
        return(dta)
    except Exception as e: pass
    
def acpt(cookies):
    cookies = {'cookie':cookies}
    try:
        headers = {'authority': 'web.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','referer': 'https://web.facebook.com/','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Linux"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','viewport-width': '980','x-asbd-id': '129477','x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation','x-fb-lsd': '_HXdQr8kHu0XQKU7XKSGvZ',}
        req = requests.get('https://web.facebook.com/',cookies=cookies).text
        data = getdata(req)
        data.update({'server_timestamps':'true','variables':'{"scale":2}','doc_id':'4851458921570237','fb_api_req_friendly_name':'CommerceManagerCreatePageMutation'})
        postv = requests.post('https://web.facebook.com/api/graphql/', cookies=cookies,data=data)
        x = json.loads(postv.text)
        try:
            tot = x['data']['viewer']['friend_requests']['count']
            print("[÷] Total Requests: "+str(tot))
            for iid in re.findall('"id":"(.*?)"',postv.text):
                data = getdata(req)
                data.update({'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation','variables': '{"input":{"attribution_id_v2":"FriendingCometFriendRequestsRoot.react,comet.friending.friendrequests,via_cold_start,1706085835850,561322,2356318349,,","friend_requester_id":"'+iid+'","source":"friends_tab","actor_id":"'+data['__user']+'","client_mutation_id":"2"},"scale":2,"refresh_num":0}','server_timestamps': 'true','doc_id': '7495020253863724'})
                post = requests.post('https://web.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
                if "ARE_FRIENDS" in str(post.text):
                    print("\033[1;92m[√] Successfully Accepted: "+iid)
                    oks.append(iid)
                else:
                    pass
            if '"has_next_page":true' in str(postv.text):
                acpt(cookies,uid)
        except Exception as e:print("[×] Not found requests:", data['__user'])
    except Exception as e:pass
def rq(idx,cookie):
    uid = cookie.split('c_user=')[1].split(';')[0]
    cookies = {'cookie':cookie}
    profile = requests.get('https://web.facebook.com/', cookies=cookies).text
    try:
        headers = {'authority': 'web.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','referer': 'https://web.facebook.com/','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Linux"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','viewport-width': '980','x-asbd-id': '129477','x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation','x-fb-lsd': '_HXdQr8kHu0XQKU7XKSGvZ',}
        data = getdata(profile)
        data.update({'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation','variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1706094125196,451302,190055527696468,,","friend_requestee_ids":["'+idx+'"],"refs":[null],"source":"profile_button","warn_ack_for_ids":[],"actor_id":"'+data['__user']+'","client_mutation_id":"3"},"scale":2}','server_timestamps': 'true','doc_id': '7033797416660129'})
        pos = requests.post('https://web.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
        if "checkpoint" in str(pos.text):
            print("[×] Account got checkpoint wait ")
        elif "people you know" in str(pos.text):
            data = getdata(profile)
            data.update({'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation','variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1706094449393,338154,190055527696468,,","friend_requestee_ids":["'+idx+'"],"refs":[null],"source":"profile_button","warn_ack_for_ids":["'+idx+'"],"actor_id":"'+data['__user']+'","client_mutation_id":"2"},"scale":2}','server_timestamps': 'true','doc_id': '7033797416660129'})
            pos = requests.post('https://web.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
            if "Cancel Request" in str(pos.text):
                print("\033[1;32m[√] Request Send Successfully:",idx)
                oks.append(idx)
        elif "Cancel Request" in str(pos.text):
            print("\033[1;32m[√] Request Send Successfully:",idx)
            ok.append(idx)
        else:
            pass
    except Exception as e:
        pass


def get_file():
    #clr()
    try:
        ids = open(input(f'{yal}[+] {whi}Put ids file with cookies: '),'r',encoding='utf-8').read().splitlines()
    except FileNotFoundError:
        print('\n No file found, try again ')
        time.sleep(2)
        get_file()
    linex()
    try:
        print(f'{yal}[~]{whi} Make sure put new ids and simple file ')
        linex()
        idx = open(input(f'{yal}[+] {whi}Put simple ids file: '),'r',encoding='utf-8').read().splitlines()
    except FileNotFoundError:
        print('\n No file found, try again ')
        time.sleep(2)
        get_file()
    #clr()
    print(f'{yal}[+] {whi}Total ids: {len(ids)}')
    print(f'{yal}[+]{whi} Friend Request process has been started')
    linex()
    with Thread(max_workers=15) as executor:
        for cok in ids:
            data = cok.replace('oo=v|3','oo=v3')
            cookie = data.split('|')[2]
            for iid in idx:
                op = iid.split('|')[0]
                executor.submit(rq,op,cookie)
    linex()
    print('[+] The process has been completed')
    print(f'[+] Total request accept: {len(oks)}')
    linex()
    input('[+] Press enter for back')
    oks.clear()
    Main()

def get_filev2():
    #clr()
    try:
        ids = open(input(f'{yal}[+] {whi}Put ids file with cookies: '),'r',encoding='utf-8').read().splitlines()
    except FileNotFoundError:
        print('\n No file found, try again ')
        time.sleep(2)
        get_filev2()
    #clr()
    print(f'{yal}[+] {whi}Total ids: {len(ids)}')
    print(f'{yal}[+] {whi}Request accept process has been started')
    linex()
    with Thread(max_workers=15) as executor:
        for cok in ids:
            data = cok.replace('oo=v|3','oo=v3')
            cookie = data.split('|')[2]
            executor.submit(acpt,cookie)
    linex()
    print('[+] The process has been completed')
    print(f'[+] Total request accept: {len(oks)}')
    linex()
    input('[+] Press enter for back')
    oks.clear()
    
      
Main()

