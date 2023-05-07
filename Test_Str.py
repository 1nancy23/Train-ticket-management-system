Time1="223.12.32:12"
Time2="2:43.232:223."
if int(Time1.replace(':','').replace('.',''))<int(Time2.replace(':','').replace('.','')):
    print(1)