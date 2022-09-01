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

print(result_sysname,'\n',result_syscontact,'\n',result_syslocation)
