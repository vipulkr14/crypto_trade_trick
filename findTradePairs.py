import datetime as dt
import requests as rs
import os
import json
import math

base_url="https://api.coindcx.com"
home_currency='INR'
intermediate_currency='USDT'
hct_list=[]
finalCur_list=[]
ict_list=[]

hct_details={}
ict_details={}

# finalCur_list=['BNB', 'USDT', 'BTC', 'ONE', 'XRP', 'MATIC', 'YFI', 'SXP', 'ENJ', 'CRO', 'ETN', 'CHZ', 'TRX', 'VET', 'DGTX', 'CKB', 'XLM', 'ETH', 'DOT', 'OXT', 'BCH', 'DOGE', 'EOS', 'LINK', 'THETA', 'LTC', 'USDC', 'UNI', 'BAT', 'STPT', 'ADA', 'CHR']
# hct_details={'BTCINR': {'market': 'BTCINR', 'change_24_hour': '-1.624', 'high': '4981820.7', 'low': '4841833.76', 'volume': '31894114.3034700149454621', 'last_price': '4872562.500000', 'bid': '4875000.01', 'ask': '4885555.55', 'timestamp': 1618685740}, 'BNBINR': {'market': 'BNBINR', 'change_24_hour': '1.208', 'high': '43374.81', 'low': '40800.0', 'volume': '5366895.36573', 'last_price': '41806.990000', 'bid': '41434.05', 'ask': '41816.11', 'timestamp': 1618685740}, 'USDTINR': {'market': 'USDTINR', 'change_24_hour': '0.91', 'high': '81.39', 'low': '78.8', 'volume': '315518232.83789983722', 'last_price': '80.930000', 'bid': '80.93', 'ask': '81', 'timestamp': 1618685740}, 'ONEINR': {'market': 'ONEINR', 'change_24_hour': '4.097', 'high': '12.3', 'low': '11.26', 'volume': '2189124.48', 'last_price': '11.940000', 'bid': '11.84', 'ask': '11.85', 'timestamp': 1618685740}, 'XRPINR': {'market': 'XRPINR', 'change_24_hour': '-2.629', 'high': '138.0', 'low': '123.22', 'volume': '8904036.0', 'last_price': '129.990000', 'bid': '129', 'ask': '129.4', 'timestamp': 1618685740}, 'MATICINR': {'market': 'MATICINR', 'change_24_hour': '-2.695', 'high': '35.0', 'low': '32.6', 'volume': '1390900.0', 'last_price': '32.739000', 'bid': '32.739', 'ask': '32.946', 'timestamp': 1618685740}, 'YFIINR': {'market': 'YFIINR', 'change_24_hour': '4.202', 'high': '4164841.0', 'low': '3996861.0', 'volume': '46479.62556', 'last_price': '4164841.000000', 'bid': '3951404', 'ask': '4010733', 'timestamp': 1618685740}, 'SXPINR': {'market': 'SXPINR', 'change_24_hour': '-3.534', 'high': '399.0', 'low': '375.0', 'volume': '81449.466', 'last_price': '375.000000', 'bid': '376.37', 'ask': '381.63', 'timestamp': 1618685740}, 'ENJINR': {'market': 'ENJINR', 'change_24_hour': '0.439', 'high': '244.52', 'low': '238.19', 'volume': '127932.864', 'last_price': '240.000000', 'bid': '240', 'ask': '242.61', 'timestamp': 1618685740}, 'CROINR': {'market': 'CROINR', 'change_24_hour': '9.768', 'high': '20.95', 'low': '18.12', 'volume': '166741.05', 'last_price': '19.890000', 'bid': '19.1', 'ask': '19.89', 'timestamp': 1618685740}, 'CHZINR': {'market': 'CHZINR', 'change_24_hour': '-13.12', 'high': '67.62', 'low': '48.09', 'volume': '12272624.28', 'last_price': '50.390000', 'bid': '50.09', 'ask': '50.54', 'timestamp': 1618685740}, 'TRXINR': {'market': 'TRXINR', 'change_24_hour': '-1.969', 'high': '14.3', 'low': '12.49', 'volume': '12478394.5', 'last_price': '12.940000', 'bid': '12.9', 'ask': '12.94', 'timestamp': 1618685740}, 'VETINR': {'market': 'VETINR', 'change_24_hour': '19.823', 'high': '22.39', 'low': '15.84', 'volume': '7137939.713355004478', 'last_price': '18.98', 'bid': '18.98', 'ask': '19', 'timestamp': 1618685740}, 'CKBINR': {'market': 'CKBINR', 'change_24_hour': '2.57', 'high': '2.65', 'low': '2.241', 'volume': '1353309.95', 'last_price': '2.434000', 'bid': '2.42', 'ask': '2.438', 'timestamp': 1618685740}, 'XLMINR': {'market': 'XLMINR', 'change_24_hour': '1.61', 'high': '51.32', 'low': '47.9', 'volume': '718223.4', 'last_price': '49.200000', 'bid': '48.26', 'ask': '48.91', 'timestamp': 1618685740}, 'ETHINR': {'market': 'ETHINR', 'change_24_hour': '-1.689', 'high': '198183.37', 'low': '188618.21', 'volume': '7579978.807401', 'last_price': '192000.000000', 'bid': '191000.03', 'ask': '192000', 'timestamp': 1618685740}, 'DOTINR': {'market': 'DOTINR', 'change_24_hour': '2.82', 'high': '3834.97', 'low': '3329.49', 'volume': '1397808.2153', 'last_price': '3450.000000', 'bid': '3506.26', 'ask': '3551.44', 'timestamp': 1618685740}, 'OXTINR': {'market': 'OXTINR', 'change_24_hour': '5.516', 'high': '67.52', 'low': '62.36', 'volume': '102090.24', 'last_price': '65.800000', 'bid': '64.56', 'ask': '65.9', 'timestamp': 1618685740}, 'BCHINR': {'market': 'BCHINR', 'change_24_hour': '-6.815', 'high': '96000.0', 'low': '81536.5', 'volume': '4267527.64799999808', 'last_price': '81536.500000', 'bid': '83276.59', 'ask': '84093.53', 'timestamp': 1618685740}, 'DOGEINR': {'market': 'DOGEINR', 'change_24_hour': '-17.996', 'high': '31.51', 'low': '18.2', 'volume': '107471283.04', 'last_price': '22.100000', 'bid': '22.0079', 'ask': '22.1', 'timestamp': 1618685740}, 'EOSINR': {'market': 'EOSINR', 'change_24_hour': '-1.342', 'high': '705.8', 'low': '620.0', 'volume': '2517298.3468079992942', 'last_price': '643.050000', 'bid': '637.58', 'ask': '642.79', 'timestamp': 1618685740}, 'LINKINR': {'market': 'LINKINR', 'change_24_hour': '-2.938', 'high': '3489.78', 'low': '3247.53', 'volume': '510014.75658588', 'last_price': '3250.000000', 'bid': '3277.96', 'ask': '3323.33', 'timestamp': 1618685740}, 'THETAINR': {'market': 'THETAINR', 'change_24_hour': '-5.029', 'high': '1188.44', 'low': '1046.31', 'volume': '1194203.934', 'last_price': '1069.040000', 'bid': '1102.05', 'ask': '1110.6', 'timestamp': 1618685740}, 'LTCINR': {'market': 'LTCINR', 'change_24_hour': '2.265', 'high': '26563.78', 'low': '24212.0', 'volume': '2640034.42184476', 'last_price': '24959.990000', 'bid': '24959.99', 'ask': '25095.17', 'timestamp': 1618685740}, 'USDCINR': {'market': 'USDCINR', 'change_24_hour': '1.229', 'high': '81.09', 'low': '78.91', 'volume': '1230889.437', 'last_price': '80.690000', 'bid': '80.99', 'ask': '81.03', 'timestamp': 1618685740}, 'UNIINR': {'market': 'UNIINR', 'change_24_hour': '-1.429', 'high': '2936.02', 'low': '2846.0', 'volume': '244364.9446', 'last_price': '2846.000000', 'bid': '2834.52', 'ask': '2872.76', 'timestamp': 1618685740}, 'BATINR': {'market': 'BATINR', 'change_24_hour': '0.468', 'high': '126.98', 'low': '119.44', 'volume': '265891.0408', 'last_price': '120.000000', 'bid': '119.21', 'ask': '121.99', 'timestamp': 1618685740}, 'STPTINR': {'market': 'STPTINR', 'change_24_hour': '5.144', 'high': '6.54', 'low': '6.15', 'volume': '404531.7', 'last_price': '6.540000', 'bid': '6.4', 'ask': '6.54', 'timestamp': 1618685740}, 'ADAINR': {'market': 'ADAINR', 'change_24_hour': '-2.287', 'high': '115.39', 'low': '109.9', 'volume': '2410035.54', 'last_price': '112.360000', 'bid': '111.28', 'ask': '112.16', 'timestamp': 1618685740}, 'CHRINR': {'market': 'CHRINR', 'change_24_hour': '-5.597', 'high': '38.23', 'low': '31.13', 'volume': '3588076.65', 'last_price': '32.550000', 'bid': '32.28', 'ask': '32.55', 'timestamp': 1618685740}}
# ict_details={'SXPUSDT': {'market': 'SXPUSDT', 'change_24_hour': '-2.738', 'high': '5.14000000', 'low': '4.57000000', 'volume': '221820167.70446400', 'last_price': '4.68800000', 'bid': '4.69', 'ask': '4.692', 'timestamp': 1618685740}, 'UNIUSDT': {'market': 'UNIUSDT', 'change_24_hour': '-2.840', 'high': '37.52670000', 'low': '34.62220000', 'volume': '104218403.32911100', 'last_price': '35.31990000', 'bid': '35.3243', 'ask': '35.3382', 'timestamp': 1618685740}, 'BATUSDT': {'market': 'BATUSDT', 'change_24_hour': '-0.140', 'high': '1.60440000', 'low': '1.46050000', 'volume': '41814948.04896300', 'last_price': '1.49510000', 'bid': '1.4966', 'ask': '1.4976', 'timestamp': 1618685740}, 'LINKUSDT': {'market': 'LINKUSDT', 'change_24_hour': '-1.861', 'high': '44.11160000', 'low': '39.92290000', 'volume': '296212707.54046100', 'last_price': '40.82560000', 'bid': '40.8603', 'ask': '40.863', 'timestamp': 1618685740}, 'ADAUSDT': {'market': 'ADAUSDT', 'change_24_hour': '-3.597', 'high': '1.45805000', 'low': '1.35501000', 'volume': '488538089.94787600', 'last_price': '1.38243000', 'bid': '1.38325', 'ask': '1.38326', 'timestamp': 1618685740}, 'BTCUSDT': {'market': 'BTCUSDT', 'change_24_hour': '-2.109', 'high': '62506.05000000', 'low': '59580.91000000', 'volume': '3795095876.88816841', 'last_price': '60327.01000000', 'bid': '60351.17', 'ask': '60353.06', 'timestamp': 1618685740}, 'VETUSDT': {'market': 'VETUSDT', 'change_24_hour': '14.467', 'high': '0.27982900', 'low': '0.19851200', 'volume': '1910219430.53671800', 'last_price': '0.23329400', 'bid': '0.233067', 'ask': '0.233177', 'timestamp': 1618685740}, 'DOTUSDT': {'market': 'DOTUSDT', 'change_24_hour': '4.477', 'high': '48.36000000', 'low': '41.11390000', 'volume': '760640263.54517800', 'last_price': '43.69270000', 'bid': '43.6773', 'ask': '43.6927', 'timestamp': 1618685740}, 'LTCUSDT': {'market': 'LTCUSDT', 'change_24_hour': '0.350', 'high': '335.69000000', 'low': '296.75000000', 'volume': '865009394.79921750', 'last_price': '309.08000000', 'bid': '309.27', 'ask': '309.38', 'timestamp': 1618685740}, 'CHZUSDT': {'market': 'CHZUSDT', 'change_24_hour': '-14.264', 'high': '0.84000000', 'low': '0.59583000', 'volume': '1775292925.23152500', 'last_price': '0.62207000', 'bid': '0.62263', 'ask': '0.623', 'timestamp': 1618685740}, 'THETAUSDT': {'market': 'THETAUSDT', 'change_24_hour': '-2.775', 'high': '14.98000000', 'low': '12.92219000', 'volume': '273802417.82158900', 'last_price': '13.67956000', 'bid': '13.65819', 'ask': '13.66294', 'timestamp': 1618685740}, 'XLMUSDT': {'market': 'XLMUSDT', 'change_24_hour': '-1.566', 'high': '0.64400000', 'low': '0.58802000', 'volume': '176833373.93900900', 'last_price': '0.60183000', 'bid': '0.60205', 'ask': '0.60225', 'timestamp': 1618685740}, 'ONEUSDT': {'market': 'ONEUSDT', 'change_24_hour': '2.190', 'high': '0.15522000', 'low': '0.13982000', 'volume': '111617972.57543800', 'last_price': '0.14779000', 'bid': '0.14778', 'ask': '0.1479', 'timestamp': 1618685740}, 'BCHUSDT': {'market': 'BCHUSDT', 'change_24_hour': '-4.648', 'high': '1219.98000000', 'low': '992.41000000', 'volume': '879961048.29136210', 'last_price': '1035.28000000', 'bid': '1036.56', 'ask': '1036.87', 'timestamp': 1618685740}, 'EOSUSDT': {'market': 'EOSUSDT', 'change_24_hour': '-4.178', 'high': '8.84650000', 'low': '7.59560000', 'volume': '546274114.27048500', 'last_price': '7.91740000', 'bid': '7.93', 'ask': '7.9316', 'timestamp': 1618685740}, 'CHRUSDT': {'market': 'CHRUSDT', 'change_24_hour': '-6.214', 'high': '0.47959000', 'low': '0.38140000', 'volume': '126911780.36141900', 'last_price': '0.40101000', 'bid': '0.401', 'ask': '0.40157', 'timestamp': 1618685740}, 'STPTUSDT': {'market': 'STPTUSDT', 'change_24_hour': '3.165', 'high': '0.08100000', 'low': '0.07627000', 'volume': '3393131.57018200', 'last_price': '0.07987000', 'bid': '0.07987', 'ask': '0.08005', 'timestamp': 1618685740}, 'ETHUSDT': {'market': 'ETHUSDT', 'change_24_hour': '-2.929', 'high': '2495.00000000', 'low': '2310.00000000', 'volume': '1578700079.20674840', 'last_price': '2361.00000000', 'bid': '2362.29', 'ask': '2362.3', 'timestamp': 1618685740}, 'XRPUSDT': {'market': 'XRPUSDT', 'change_24_hour': '-5.152', 'high': '1.74163000', 'low': '1.52991000', 'volume': '1942581446.39026400', 'last_price': '1.57813000', 'bid': '1.57962', 'ask': '1.57999', 'timestamp': 1618685740}, 'CROUSDT': {'market': 'CROUSDT', 'change_24_hour': '0.817', 'high': '0.251672', 'low': '0.231472', 'volume': '21480446.130981278', 'last_price': '0.236037', 'bid': '0.2358', 'ask': '0.2359', 'timestamp': 1618685740}, 'ENJUSDT': {'market': 'ENJUSDT', 'change_24_hour': '-1.090', 'high': '3.15418000', 'low': '2.93333000', 'volume': '95406501.18012400', 'last_price': '2.98108000', 'bid': '2.98232', 'ask': '2.98348', 'timestamp': 1618685740}, 'DOGEUSDT': {'market': 'DOGEUSDT', 'change_24_hour': '-18.465', 'high': '0.40000000', 'low': '0.23100000', 'volume': '8149954191.08800610', 'last_price': '0.27432330', 'bid': '0.274715', 'ask': '0.2747965', 'timestamp': 1618685740}, 'MATICUSDT': {'market': 'MATICUSDT', 'change_24_hour': '-3.426', 'high': '0.43906000', 'low': '0.39914000', 'volume': '69139398.95981000', 'last_price': '0.40579000', 'bid': '0.40571', 'ask': '0.40594', 'timestamp': 1618685740}, 'YFIUSDT': {'market': 'YFIUSDT', 'change_24_hour': '0.233', 'high': '54500.00000000', 'low': '48426.18000000', 'volume': '75647492.52072005', 'last_price': '49258.43000000', 'bid': '49278.18', 'ask': '49317.44', 'timestamp': 1618685740}, 'CKBUSDT': {'market': 'CKBUSDT', 'change_24_hour': '1.298', 'high': '0.03360000', 'low': '0.02789600', 'volume': '22598861.98398100', 'last_price': '0.02997600', 'bid': '0.029923', 'ask': '0.029977', 'timestamp': 1618685740}, 'TRXUSDT': {'market': 'TRXUSDT', 'change_24_hour': '-2.433', 'high': '0.18000000', 'low': '0.15278000', 'volume': '823635577.58481700', 'last_price': '0.15904000', 'bid': '0.15925', 'ask': '0.15931', 'timestamp': 1618685740}, 'OXTUSDT': {'market': 'OXTUSDT', 'change_24_hour': '3.641', 'high': '0.86390000', 'low': '0.77940000', 'volume': '14340903.79059800', 'last_price': '0.80800000', 'bid': '0.8077', 'ask': '0.8087', 'timestamp': 1618685740}, 'BNBUSDT': {'market': 'BNBUSDT', 'change_24_hour': '-0.616', 'high': '547.95000000', 'low': '506.00000000', 'volume': '1507218879.14580110', 'last_price': '515.55750000', 'bid': '515.6725', 'ask': '515.7', 'timestamp': 1618685740}, 'USDCUSDT': {'market': 'USDCUSDT', 'change_24_hour': '0.030', 'high': '1.00000000', 'low': '0.99820000', 'volume': '245769462.67875300', 'last_price': '0.99910000', 'bid': '0.999', 'ask': '0.9991', 'timestamp': 1618685740}}

def process_details(f):
    i_h=hct_details.get(intermediate_currency+home_currency)
    i_h_bid=float(i_h['bid'])
    insert_new_line(f," ")
    insert_new_line(f,"------------Processing starts-----------------")
    insert_new_line(f,"rate to buy "+intermediate_currency+" = "+str(i_h_bid))
    insert_new_line(f," ")
    number_of_i=10
    price_to_buy_i=1.001*number_of_i*i_h_bid
    # print("price to buy "+intermediate_currency+": "+str(price_to_buy_i))

    for i in ict_details:
        insert_new_line(f," ")
        c_i=ict_details.get(i)
        curr=i.split(intermediate_currency)[0]
        insert_new_line(f,curr)
        c_i_bid=float(c_i['bid'])
        insert_new_line(f,"rate to buy: "+str(c_i_bid))
        number_of_c=number_of_i/c_i_bid
        insert_new_line(f,"number: "+str(number_of_c))
        # print("currency: "+curr+" number: "+str(number_of_c))
        number_of_c=math.ceil(number_of_c)
        insert_new_line(f,"rounded off number: "+str(number_of_c))
        # print("final number of c: "+str(number_of_c))
        new_number_of_i=number_of_c*c_i_bid*1.001
        insert_new_line(f,"number of "+intermediate_currency+": "+str(new_number_of_i))
        new_price_to_buy_i=1.001*new_number_of_i*i_h_bid
        # print("price to buy i: "+str(new_price_to_buy_i))
        insert_new_line(f,"price to buy "+intermediate_currency+": "+str(new_price_to_buy_i))
        c_h=hct_details.get(curr+home_currency)
        c_h_ask=float(c_h['last_price'])
        insert_new_line(f,"rate to sell "+curr+": "+str(c_h_ask))
        price_to_sell_c=0.999*number_of_c*c_h_ask
        # print("price to sell c: "+str(price_to_sell_c))
        insert_new_line(f,"price to sell "+curr+": "+str(price_to_sell_c))
        profit=price_to_sell_c-new_price_to_buy_i
        insert_new_line(f,"profit: "+str(profit))

def get_ticker(f):
    url=base_url+"/exchange/ticker"
    response=rs.get(url)
    data=response.json()
    print(type(data))
    for i in data:
        if i['market'] in hct_list:
            hct_details[i['market']]=i
        if i['market'] in ict_list:
            ict_details[i['market']]=i
    insert_new_line(f,"hct details: "+str(len(hct_details)))
    insert_new_line(f,hct_details)
    insert_new_line(f,"ict details: "+str(len(ict_details)))
    insert_new_line(f,ict_details)

def get_markets(f):
    url=base_url+"/exchange/v1/markets"
    response=rs.get(url)
    data=response.json()
    temp_hct_list=[]
    temp_ict_list=[]
    print(type(data))
    for i in data:
        if home_currency in i:
            temp_hct_list.append(i)
            finalCur_list.append(i.split(home_currency)[0])
        if intermediate_currency in i:
            temp_ict_list.append(i)

    insert_new_line(f,"currencies with matching pair:")
    for i in temp_ict_list:
        fcurr=i.split(intermediate_currency)[0]
        if fcurr in finalCur_list:
            insert_new_line(f,fcurr)
            ict_list.append(i)
        if i in intermediate_currency+home_currency:
            hct_list.append(i)
    
    for i in finalCur_list:
        if i+intermediate_currency in temp_ict_list:
            hct_list.append(i+home_currency)

    insert_new_line(f,"final currencies to check: "+str(len(finalCur_list)))
    insert_new_line(f,finalCur_list)
    insert_new_line(f,"total currencies to check: "+str(len(ict_list)))
    insert_new_line(f,"total with home currency: "+str(len(hct_list)))
    insert_new_line(f,"total in intermediate currency: "+str(len(temp_ict_list)))
    #insert_new_line(f,data)



def insert_new_line(f,content):
    if " "==content:
        f.write('\n')
    else:
        f.write('\n'+str(content))

def start():
    ct = dt.datetime.now()
    print("current time:-", ct)
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    filename="outputs/output_"+str(ct.year)+"_"+str(ct.month)+"_"+str(ct.day)+"_"+str(ct.hour)+"_"+str(ct.minute)+"_"+str(ct.second)+".txt"
    print(filename)
    f = open(filename, "x")
    print(type(f))
    f.write("Current time: "+str(ct))
    #get the market details
    get_markets(f)
    #get ticker details
    get_ticker(f)
    process_details(f)
    f.close()
start()