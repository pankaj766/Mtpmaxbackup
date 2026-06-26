import requests
from os import system

# ----------------- BANNER & MENU -----------------
def banner():
    system('clear')
    print("\033[96m")
    print("  ███████╗██╗   ██╗ ██████╗ ")
    print("  ██╔════╝██║   ██║██╔═══██╗")
    print("  ███████╗██║   ██║██║   ██║")
    print("  ╚════██║██║   ██║██║   ██║")
    print("  ███████║╚██████╔╝╚██████╔╝")
    print("  ╚══════╝ ╚═════╝  ╚═════╝ ")
    print("\033[0m")
    print("\033[95m─────────────── ON TOP ───────────────\033[0m\n")
    
    print("\033[92m[✓] DEVELOPER : @jubayer_codex\033[0m")
    print("\033[92m[✓] TOOL NAME : JUBAYER ACCOUNT RECOVERY\033[0m")
    print("\033[92m[✓] STATUS    : SAFE & SECURE\033[0m")
    
    print("\n\033[95m──────────────────────────────────────\033[0m\n")


def menu():
    banner()
    
    print("\033[96m[1]\033[0m Add Recovery Email")
    print("\033[96m[2]\033[0m Check Recovery Email")
    print("\033[96m[3]\033[0m Check Linked Accounts")
    print("\033[96m[4]\033[0m Cancel Recovery Email")
    print("\033[91m[0]\033[0m Exit")
    
    print("\n\033[95m──────────────────────────────────────\033[0m")
    
    choice = input("\nSelect Option ➤ ")
    return choice

# ----------------- FUNCTIONALITY -----------------
def CancEL(access):
    url = "https://100067.connect.garena.com/game/account_security/bind:cancel_request"
    payload = {'app_id': "100067", 'access_token': access}
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)", 
               'Connection': "Keep-Alive", 'Accept-Encoding': "gzip"}
    rsp = requests.post(url, data=payload, headers=headers)
    if rsp.status_code == 200:
        print('- Response =>', rsp.json())
    else:
        print('- No Response!')

def SEnd(email, access):
    url = "https://100067.connect.garena.com/game/account_security/bind:send_otp"    
    payload = {'app_id': "100067", 'access_token': access, 'email': email, 'locale': "en_MA"}    
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)", 
               'Connection': "Keep-Alive", 'Accept': "application/json", 
               'Accept-Encoding': "gzip", 
               'Cookie': "datadome=q2ZtAABCjPFEIWeaxYM2YvfxEUPXT_GLUp4gpUOEUPlI9jGXkQLS5uoG_HBUBnJvC0s0CBfHF6h4FUg7mBumLRO1jpLh4um4CbF4ykEKTLv5f27DgR_nkEJcZm_Sj1E~"}    
    rsp = requests.post(url, data=payload, headers=headers)    
    if rsp.status_code == 200:
        otp = input('- Enter OTP ➤ ')
        return VeriFy(otp, email, access)
    else:
        print('- Bad Response. OTP not received!')

def VeriFy(otp, email, access):
    url = "https://100067.connect.garena.com/game/account_security/bind:verify_otp"    
    payload = {'app_id': "100067", 'access_token': access, 'otp': otp, 'email': email}    
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)", 
               'Connection': "Keep-Alive", 'Accept-Encoding': "gzip"}    
    rsp = requests.post(url, data=payload, headers=headers)    
    if rsp.status_code == 200:
        auth = rsp.json().get("verifier_token")
        print('- Auth Access ➤', auth)
        return Add(auth, access, email)

def Add(auth, access, email):
    CancEL(access)
    url = "https://100067.connect.garena.com/game/account_security/bind:create_bind_request"    
    payload = {'app_id': "100067", 'access_token': access, 
               'verifier_token': auth, 
               'secondary_password': "91B4D142823F7D20C5F08DF69122DE43F35F057A988D9619F6D3138485C9A203", 
               'email': email}    
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)", 
               'Connection': "Keep-Alive", 'Accept-Encoding': "gzip"}    
    rsp = requests.post(url, data=payload, headers=headers)    
    if rsp.status_code == 200:
        print(rsp.json())
        print(f'- Successfully added {email} to account!')

def convert(s):
    d,h=divmod(s,86400);h,m=divmod(h,3600);m,s=divmod(m,60)
    return f"{d} Day {h} Hour {m} Min {s} Sec"

def ChK(access):
    url = "https://100067.connect.garena.com/game/account_security/bind:get_bind_info"
    payload = {'app_id': "100067", 'access_token': access}
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)", 
               'Connection': "Keep-Alive", 'Accept-Encoding': "gzip"}
    rsp = requests.get(url, params=payload, headers=headers)
    if rsp.status_code == 200:
        data = rsp.json()
        email = data.get("email", "")
        email_to_be = data.get("email_to_be", "")
        countdown = data.get("request_exec_countdown", 0)
        if email == "" and email_to_be != "":
            print(f"Email ➤ {email_to_be}\nConfirmed in ➤ {convert(countdown)}")
        elif email != "" and email_to_be == "":
            print(f"Email ➤ {email}\nConfirmed ➤ Yes!")
        elif email == "" and email_to_be == "":
            print("No Recovery Email Found!")       
    else:
        print("Error ➤", rsp.status_code)

def GeT_PLaFTroms(t):
    system('clear')
    r = requests.get("https://100067.connect.garena.com/bind/app/platform/info/get",
        params={'access_token': t},
        headers={'User-Agent':"GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)",
                 "Connection":"Keep-Alive",
                 "Accept-Encoding":"gzip",
                 "If-Modified-Since":"Sun, 18 May 2025 09:37:03 GMT"})
    if r.status_code not in [200,201]:
        return print("Failed to fetch.")
    j=r.json()
    m={3:"Facebook",8:"Gmail",10:"iCloud",5:"VK",11:"Twitter",7:"Huawei"}
    b,a=j.get("bounded_accounts",[]),j.get("available_platforms",[])
    print("> Secondary Links: <")
    l=False
    for x in b:
        try:
            p = x.get('platform')
            uinfo = x.get('user_info',{})
            e = uinfo.get('email','')
            n = uinfo.get('nickname','')
            if p in m:
                print(f"\n=> {m[p]} !")
                if e: print(f"- Email ➤ {e}")
                if n: print(f"- Nickname ➤ {n}")
                print(); l=True
        except: continue
    if not l: print("=> Secondary Links Not Found!")
    print("\n> Response: <\n\n", b)
    for k in m:
        if k not in a:
            print(f"\n> Main Platform ➤ {m[k]} ! <")
            break

# ----------------- MAIN MENU LOOP -----------------
while True:
    choice = menu()
    
    if choice == '1':
        system('clear')
        email = input("Enter Email ➤ ")
        access = input("Enter Access Token ➤ ")
        SEnd(email, access)

    elif choice == '2':
        system('clear')
        access = input("Enter Access Token ➤ ")
        ChK(access)

    elif choice == '3':
        system('clear')
        access = input("Enter Access Token ➤ ")
        GeT_PLaFTroms(access)

    elif choice == '4':
        system('clear')
        access = input("Enter Access Token ➤ ")
        CancEL(access)

    elif choice == '0':
        print("\nExiting...")
        break

    else:
        print("\nInvalid Option!")