    #biblioteka wykorzystywane
from puresnmp import get
import pandas as pd


    #adres ip SCALANCE X
ip = "192.168.100.11"
    #community
community = "public_snmp"

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
#find_s1 = result_model.partition('SCALANCE')
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




#adresacja IP urządzenai
    #adresy IPv4
oid = '1.3.6.1.4.1.4329.6.3.2.1.4.1.0'
result_ip = get(ip, community, oid)
result_ip = int(result_ip[0]),int(result_ip[1]),int(result_ip[2]),int(result_ip[3])

    #maska podsieci
oid = '1.3.6.1.4.1.4329.6.3.2.1.4.2.0'
result_mask = get(ip, community, oid)
result_mask = int(result_mask[0]),int(result_mask[1]),int(result_mask[2]),int(result_mask[3])

    #adresy gateway
oid = '1.3.6.1.4.1.4329.6.3.2.1.4.3.0'
result_gateway = get(ip, community, oid)
result_gateway = int(result_gateway[0]),int(result_gateway[1]),int(result_gateway[2]),int(result_gateway[3])


#mrp

#Rola urządzenia w ringu
oid = '1.0.62439.1.1.1.1.5.1'
result_mrprole = get(ip, community, oid)
if result_mrprole == 1 or result_mrprole == 2 or result_mrprole == 3:

    if result_mrprole == 1:
        result_mrprole = 'MRP Client'
    elif result_mrprole == 2:
        result_mrprole = 'MRP Manager'
    elif result_mrprole == 3:
        result_mrprole = 'MRP Auto-Manager'

    #Domena MRP
    oid ='1.0.62439.1.1.1.1.3.1'
    result_mrpdomain = get(ip, community, oid)


    #Port Ringu 1
        #numer portu
    oid = '1.0.62439.1.1.1.1.6.1'
    result_mrpring1 = get(ip, community, oid)
        #status portu 
    oid = '1.0.62439.1.1.1.1.7.1'
    result_mrpring1_state = get(ip, community, oid)
    if result_mrpring1_state == 1:
        result_mrpring1_state = 'disabled'
    elif result_mrpring1_state == 2:
        result_mrpring1_state = 'blocked'
    elif result_mrpring1_state == 3:
        result_mrpring1_state = 'forwarding'
    elif result_mrpring1_state == 4:
        result_mrpring1_state = 'not-connection'

    #Port ringu 2
        #numer portu
    oid = '1.0.62439.1.1.1.1.8.1'
    result_mrpring2 = get(ip, community, oid)
        #status portu
    oid = '1.0.62439.1.1.1.1.9.1'
    result_mrpring2_state = get(ip, community, oid)
    if result_mrpring2_state == 1:
        result_mrpring2_state = 'disabled'
    elif result_mrpring2_state == 2:
        result_mrpring2_state = 'blocked'
    elif result_mrpring2_state == 3:
        result_mrpring2_state = 'forwarding'
    elif result_mrpring2_state == 4:
        result_mrpring2_state = 'not-connection'

    #ile razy ring zostal rozlaczony
    oid = '1.0.62439.1.1.1.1.15.1'
    result_opencount = get(ip, community, oid)
    #czas otwarcia ringu
    oid = '1.0.62439.1.1.1.1.16.1'
    result_timeopenring = get(ip, community, oid)
    #Maksymalny czas przelaczenia
    oid = '1.0.62439.1.1.1.1.17.1'
    result_tripdelaymax = get(ip, community, oid)

    #Minimalny czas przelaczenia
    oid = '1.0.62439.1.1.1.1.18.1'
    result_tripdelaymin = get(ip, community, oid)

#tworzenie tabeli z danymi 
    data = {'opis': ['SysName','SysContact','SysLocation','MFLB','Model','SerialNumber','Vendor','FW Version','HW Version','Czas dzialania switcha od uruchomienia',\
                'Adres IPv4','Maska','Adres gateway','Rola w ringu MRP','Nazwa domeny MRP','Port numer 1 w ringu','Status portu 2','Port numer 2 w ringu','Status portu 2',\
                'OpenCount Ring MRP','Czas otawrcia ringu','Maksymalny czas przelaczania','Minimalny czas przelaczania'],
        'informacja ze switcha': [result_sysname,result_syscontact,result_syslocation,result_mflb,result_model,result_serialnumber,result_vendor,result_fwversion,result_hwversion,\
                                result_uptime,result_ip,result_mask,result_gateway,result_mrprole,result_mrpdomain,result_mrpring1,result_mrpring1_state,result_mrpring2,result_mrpring2_state,result_opencount, result_timeopenring,result_tripdelaymax,result_tripdelaymin]}

elif result_mrprole == 0:
    result_mrprole = 'Ring disable' #rola w ringu - wyłączony ring

    data = {'opis': ['SysName','SysContact','SysLocation','MFLB','Model','SerialNumber','Vendor','FW Version','HW Version','Czas dzialania switcha od uruchomienia',\
                'Adres IPv4','Maska','Adres gateway','Rola w ringu MRP'],
        'informacja ze switcha': [result_sysname,result_syscontact,result_syslocation,result_mflb,result_model,result_serialnumber,result_vendor,result_fwversion,result_hwversion,\
                                result_uptime,result_ip,result_mask,result_gateway,result_mrprole]}
    


df = pd.DataFrame(data)

#wyświetlanie tabeli
print(df)
print('\n')
