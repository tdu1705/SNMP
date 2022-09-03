   #wykorzystane biblioteki
from puresnmp import get
import pandas as pd


    #adres ip
ip = "192.168.100.2"
    #community
community = "public"

#oid informacje systemowe
    #nazwa systemowa
oid = '1.3.6.1.2.1.1.5.0'
result_sysname = get(ip, community, oid)
    #osoba kontaktowa
oid = '1.3.6.1.2.1.1.4.0'
result_syscontact = get(ip, community, oid)
    #systemowa lokalizacja
oid = '1.3.6.1.2.1.1.6.0'
result_syslocation = get(ip, community, oid)
    #MFLB
oid = '1.3.6.1.4.1.4329.6.3.2.1.1.2.0'
result_mflb = get(ip, community, oid)
    #SerialNumber
oid = '1.3.6.1.4.1.4329.6.3.2.1.1.3.0'
result_serialnumber = get(ip, community, oid)
    #nazwa urządzenia
oid = '1.3.6.1.2.1.1.1.0'
result_model = get(ip, community, oid)
        #szukanie początku odpowiedniej nazwy
find_s1 = result_model.find(b'SCALANCE')
result_model = result_model[find_s1:37]
    #Vendor
oid = '1.3.6.1.2.1.1.2.0'
result_vendor = get(ip, community, oid)
if result_vendor == '1.3.6.1.4.1.4329.6.1.2.1.2':
    result_vendor = 'Siemens AG'
    #FW Version
oid = '1.3.6.1.4.1.4329.6.3.2.1.1.5.0'
result_fwversion = get(ip, community, oid)
    #HW Version
oid = '1.3.6.1.4.1.4329.6.3.2.1.1.4.0'
result_hwversion = get(ip, community, oid)
    #czas działania urządzenia sysUpTime
oid = '1.3.6.1.2.1.1.3.0'
result_uptime = get(ip, community, oid)

#infomacje o podłączonych klientach

    
data = {'opis': ['SysName','SysContact','SysLocation','MFLB','Model','SerialNumber','Vendor','FW Version','HW Version','Czas dzialania switcha od uruchomienia'],
        'informacja ze switcha': [result_sysname,result_syscontact,result_syslocation,result_mflb,result_model,result_serialnumber,result_vendor,result_fwversion,result_hwversion,\
                                result_uptime]}

df = pd.DataFrame(data)
print(df)