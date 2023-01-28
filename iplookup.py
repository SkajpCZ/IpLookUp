import os
def IPLookUp():
    import requests, json
    def nullvalues():
        network = "?"
        city = "?"
        region = "?"
        regcode = "?"
        countryname = "?"
        countrycode = "?"
        countrycap = "?"
        tld = "?"
        contcode = "?"
        postal = "?"
        Lag = "?"
        Long = "?"
        timezone = "?"
        utc_off = "?"
        call = "?"
        cur = "?"
        lang = "?"
        org = "?"
    ip = input('\033[1;93m' + "\n Enter IP" + '\033[1;90m' + " > " + '\033[0;37m' +f"")
    ipinf = f"https://ipapi.co/{ip}/json/"
    stats = requests.get(ipinf)
    json_stats = stats.json()
    try:
        network = json_stats["network"] # 1.1.1.1/24
        city = json_stats["city"] # Sydney
        region = json_stats["region"] # New South Wales
        regcode = json_stats["region_code"] # NSW
        countryname = json_stats["country_name"] # Australia
        countrycode = json_stats["country_code"] # AU
        tld = json_stats["country_tld"] # .au
        contcode = json_stats["continent_code"] # OC
        postal = json_stats["postal"] #2000
        Lag = json_stats["latitude"] # -33.859336
        Long = json_stats["longitude"] # 151.203624
        timezone = json_stats["timezone"] # Australia/Sydney
        utc_off = json_stats["utc_offset"] # +1100
        call = json_stats["country_calling_code"] # +61
        cur = json_stats["currency"] # AUD
        lang = json_stats["languages"] # en-AU
        org = json_stats["asn"] + ", " + json_stats["org"] # AS13335, CLOUDFLARENET
    except KeyError():
        nullvalues()
    print('\033[1;93m' + "\n Network" + '\033[1;90m' + " > " + '\033[0;37m' +f"{network}")
    print('\033[1;93m' + " ORG" + '\033[1;90m' + " > " + '\033[0;37m' +f"{org}")
    print('\033[1;93m' + " TLD" + '\033[1;90m' + " > " + '\033[0;37m' +f"{tld}")
    print('\033[1;93m' + " Languages" + '\033[1;90m' + " > " + '\033[0;37m' +f"{lang}")
    print('\033[1;93m' + " City" + '\033[1;90m' + " > " + '\033[0;37m' +f"{city}")
    print('\033[1;93m' + " Region" + '\033[1;90m' + " > " + '\033[0;37m' +f"{region}")
    print('\033[1;93m' + " Region Code" + '\033[1;90m' + " > " + '\033[0;37m' +f"{regcode}")
    print('\033[1;93m' + " Country Name" + '\033[1;90m' + " > " + '\033[0;37m' +f"{countryname}")
    print('\033[1;93m' + " Country Code" + '\033[1;90m' + " > " + '\033[0;37m' +f"{countrycode}")
    print('\033[1;93m' + " Postal" + '\033[1;90m' + " > " + '\033[0;37m' +f"{postal}")
    print('\033[1;93m' + " GPS" + '\033[1;90m' + " > " + '\033[0;37m' +f"{Lag}, {Long}")
    print('\033[1;93m' + " Timezone" + '\033[1;90m' + " > " + '\033[0;37m' +f"{timezone}")
    print('\033[1;93m' + " Phone" + '\033[1;90m' + " > " + '\033[0;37m' +f"{call}")
    print('\033[1;93m' + " Currency" + '\033[1;90m' + " > " + '\033[0;37m' +f"{cur}\n")
    input('\n\033[1;37m Press \033[1;93m[ Enter ]\033[1;37m to exit')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print(f"""\033[1;36m
        ____      __                __   __  __    
       /  _/___  / /   ____  ____  / /__/ / / /___ 
       / // __ \/ /   / __ \/ __ \/ //_/ / / / __ \\
     _/ // /_/ / /___/ /_/ / /_/ / ,< / /_/ / /_/ /
    /___/ .___/_____/\____/\____/_/|_|\____/ .___/ 
       /_/                                /_/       \033[1;37mby \033[1;90mSkajp
                                                    \033[1;37mVersion: \033[1;90m1
""")

IPLookUp()