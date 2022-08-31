    #biblioteka
from puresnmp import get
import pandas as pd


    #adres ip
ip = "192.168.100.12"
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
    #nazwa urz�dzenia
oid = '1.3.6.1.2.1.1.1.0'
result_model = get(ip, community, oid)
        #szukanie pocz�tku odpowiedniej nazwy
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
    #czas dzia�ania urz�dzenia sysUpTime
oid = '1.3.6.1.2.1.1.3.0'
result_uptime = get(ip, community, oid)




#adresacja IP urz�dzenai
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

#Rola urz�dzenia w ringu
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
    #???? Maksymalny czas przelaczenia???
    oid = '1.0.62439.1.1.1.1.17.1'
    result_tripdelaymax = get(ip, community, oid)

    #???? Minimalny czas przelaczenia???
    oid = '1.0.62439.1.1.1.1.18.1'
    result_tripdelaymin = get(ip, community, oid)

#tworzenie tabeli z danymi 
    data = {'opis': ['SysName','SysContact','SysLocation','MFLB','Model','SerialNumber','Vendor','FW Version','HW Version','Czas dzialania switcha od uruchomienia',\
                'Adres IPv4','Maska','Adres gateway','Rola w ringu MRP','Nazwa domeny MRP','Port numer 1 w ringu','Status portu 2','Port numer 2 w ringu','Status portu 2',\
                'OpenCount Ring MRP','Czas otawrcia ringu','Maksymalny czas przelaczania','Minimalny czas przelaczania'],
        'informacja ze switcha': [result_sysname,result_syscontact,result_syslocation,result_mflb,result_model,result_serialnumber,result_vendor,result_fwversion,result_hwversion,\
                                result_uptime,result_ip,result_mask,result_gateway,result_mrprole,result_mrpdomain,result_mrpring1,result_mrpring1_state,result_mrpring2,result_mrpring2_state,result_opencount, result_timeopenring,result_tripdelaymax,result_tripdelaymin]}

elif result_mrprole == 0:
    result_mrprole = 'Ring disable' #rola w ringu - wy��czony ring

    data = {'opis': ['SysName','SysContact','SysLocation','MFLB','Model','SerialNumber','Vendor','FW Version','HW Version','Czas dzialania switcha od uruchomienia',\
                'Adres IPv4','Maska','Adres gateway','Rola w ringu MRP'],
        'informacja ze switcha': [result_sysname,result_syscontact,result_syslocation,result_mflb,result_model,result_serialnumber,result_vendor,result_fwversion,result_hwversion,\
                                result_uptime,result_ip,result_mask,result_gateway,result_mrprole]}
    


df = pd.DataFrame(data)

#wy�wietlanie tabeli
print(df)
print('\n')

#pitn("\n\n\n\n")
#print('SysName: ',result_sysname,'\tSysContact: ',result_syscontact,'\tSysLocation',result_syslocation,\
#        "\nMFLB: ",result_mflb,'\tModel: ',result_model,'\tSerialNumber: ',result_serialnumber,\
#        '\nVendor: ',result_vendor,\
#        '\nFW Version: ',result_fwversion,'\tHW Version: ',result_hwversion,\
#        '\nCzas dzialania: ',result_uptime)

#print("\n\nAdres IPv4: ",result_ip[0],".",result_ip[1],".",result_ip[2],".",result_ip[3],\
#        '\nMaska: ',result_mask[0],".",result_mask[1],".",result_mask[2],".",result_mask[3],\
#       '\nAdres gateway: ',result_gateway[0],".",result_gateway[1],".",result_gateway[2],".",result_gateway[3])


#print("\n\nRola w ringu MRP: ",(result_mrprole),\
#        "\nNazwa domeny MRP: ",result_mrpdomain,\
#        "\nPort numer 1 w ringu: ", result_mrpring1, "\tStatus portu: ",result_mrpring1_state,\
#        "\nPort numer 2 w ringu: ", result_mrpring2, "\tStatus portu: ",result_mrpring2_state,\
#        "\nOpenCount Ring MRP: ",result_opencount, "\tCzas otawrcia ringu: ",result_timeopenring,\
#        "\nMaksymalny czas przelaczania: ",result_tripdelaymax,"\tMinimalny czas przelaczania: ",result_tripdelaymin)

