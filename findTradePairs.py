import datetime as dt
import requests as rs

base_url="https://api.coindcx.com"
home_currency='INR'
intermediate_currency='USDT'
hct_list=[]
finalCur_list=[]
ict_list=[]

def get_markets(f):
    url=base_url+"/exchange/v1/markets"
    response=rs.get(url)
    data=response.json()
    temp_ict_list=[]
    print(type(data))
    for i in data:
        if home_currency in i:
            hct_list.append(i)
            finalCur_list.append(i.split(home_currency)[0])
        if intermediate_currency in i:
            temp_ict_list.append(i)
    insert_new_line(f,"currencies with matching pair:")
    for i in temp_ict_list:
        fcurr=i.split(intermediate_currency)[0]
        if fcurr in finalCur_list:
            insert_new_line(f,fcurr)
            ict_list.append(i)
            
    insert_new_line(f,"total currencies to check: "+str(len(ict_list)))
    insert_new_line(f,"total with home currency: "+str(len(hct_list)))
    insert_new_line(f,"total in intermediate currency: "+str(len(temp_ict_list)))
    #insert_new_line(f,data)


def insert_new_line(f,content):
    f.write('\n'+str(content))

def start():
    ct = dt.datetime.now()
    print("current time:-", ct)
    filename="output_"+str(ct.year)+"_"+str(ct.month)+"_"+str(ct.day)+"_"+str(ct.hour)+"_"+str(ct.minute)+"_"+str(ct.second)+".txt"
    print(filename)
    f = open(filename, "x")
    print(type(f))
    f.write("Current time: "+str(ct))
    #get the market details
    get_markets(f)
    f.close()
start()