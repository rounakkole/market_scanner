def absDiffr(a, b):
    if (a >= 0 and b >= 0 and a >= b):
        diff = (a - b)
    elif (a >= 0 and b >= 0 and b >= a):
        diff = (b - a)
    elif (a < 0 and b < 0 and a >= b):
        diff = ((-b) - (-a))
    elif (a < 0 and b < 0 and b >= a):
        diff = ((-a) - (-b))
    elif (a <= 0 and b >= 0):
        diff = ((-a) + b)
    elif (a >= 0 and b <= 0):
        diff = (a + (-b))
    else:
        diff = (a + b)
    return diff


def absSlope(a, b):
    if (a > 0 and b > 0):
        diff = 0
    elif (a < 0 and b < 0):
        diff = 0
    elif (a < 0 and b > 0):
        diff = 1
    elif (a > 0 and b < 0):
        diff = 1
    else:
        diff = 0
    return diff


def show_additional(company_name):
    import yfinance as yf

    print("y/n")
    show_additional = str(input("show_additional: "))
    show_additional = show_additional.upper()

    if (show_additional == "Y"):

        display = yf.Ticker(company_name)

        print("historical market data:")
        hist = display.history(period="max")
        print(hist)

        print("next event")
        display.calendar

        data = yf.download(tickers=company_name, period='5d', interval='1d')
        print(data)

        # show analysts recommendations
        #msft.recommendations


def country_code():

    country_name = str(input("country: "))
    country_name = country_name.upper()
    if (country_name == "CURRENCY"):
        code_string = "=X"
    elif (country_name == "INDIA"):
        code_string = ".BO"
    elif (country_name == "IN"):
        code_string = ".NS"
    elif (country_name == "BRAZIL"):
        code_string = ".SA"
    elif (country_name == "CANADA"):
        code_string = ".CN"
    elif (country_name == "CHINA"):
        code_string = ".SS"
    elif (country_name == "EUROPE"):
        code_string = ".NX"
    elif (country_name == "JAPAN"):
        code_string = ".T"
    elif (country_name == "RUSSIA"):
        code_string = ".ME"
    elif (country_name == "SINGAPORE"):
        code_string = ".SI"
    elif (country_name == "S.AFRICA"):
        code_string = ".JO"
    elif (country_name == "S.KOREA"):
        code_string = ".KS"
    elif (country_name == "SWITZERLAND"):
        code_string = ".SW"
    elif (country_name == "UK"):
        code_string = ".L"
    elif (country_name == "US"):
        code_string = ""
    else:
        print("https://in.help.yahoo.com/kb/SLN2310.html")
        code_string = str(input("suffix: "))

    return code_string


def set_period(interval_value):
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    if (interval_value == "1m" or interval_value == "2m"):
        period = "1d"
    elif (interval_value == "5m"):
        period = "5d"
    elif (interval_value == "15m" or interval_value == "30m"):
        period = "1mo"
    elif (interval_value == "60m" or interval_value == "90m"
          or interval_value == "1h"):
        period = "3mo"
    elif (interval_value == "1d"):
        period = "5y"
    elif (interval_value == "5d"):
        period = "5y"
    elif (interval_value == "1wk"):
        period = "5y"
    elif (interval_value == "1mo" or interval_value == "3mo"):
        period = "max"
    else:
        period = "1y"

    return period


def multi():
    #symbols = ['^NSEI', '^BSESN', '^GSPC', 'MSFT', 'IWO', 'VFINX', 'BTC-USD']
    fortune_100 = [
        'ACC', 'ADANIENT', 'ADANIPORTS', 'AMBUJACEM', 'APOLLOHOSP',
        'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV',
        'BAJAJHLDNG', 'BANDHANBNK', 'BANKBARODA', 'BERGEPAINT', 'BPCL',
        'BHARTIARTL', 'BIOCON', 'BOSCHLTD', 'BRITANNIA', 'CHOLAFIN', 'CIPLA',
        'COALINDIA', 'COLPAL', 'DABUR', 'DIVISLAB', 'DRREDDY', 'EICHERMOT',
        'NYKAA', 'GAIL', 'GLAND', 'GODREJCP', 'GRASIM', 'HCLTECH', 'HDFCAMC',
        'HDFCBANK', 'HDFCLIFE', 'HAVELLS', 'HEROMOTOCO', 'HINDALCO',
        'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ITC',
        'IOC', 'INDUSTOWER', 'INDUSINDBK', 'NAUKRI', 'INFY', 'INDIGO',
        'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'LTI', 'LT', 'LUPIN', 'M&M',
        'MARICO', 'MARUTI', 'MINDTREE', 'MUTHOOTFIN', 'NMDC', 'NTPC',
        'NESTLEIND', 'ONGC', 'PAYTM', 'PIIND', 'PIDILITIND', 'PEL',
        'POWERGRID', 'PGHH', 'PNB', 'RELIANCE', 'SBICARD', 'SBILIFE', 'SRF',
        'SHREECEM', 'SIEMENS', 'SBIN', 'SAIL', 'SUNPHARMA', 'TCS',
        'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN',
        'TORNTPHARM', 'UPL', 'MCDOWELL-N', 'VEDL', 'WIPRO', 'ZOMATO',
        'ZYDUSLIFE'
    ]

    return fortune_100


def console_chart(data_list):

    #data_list = [open, high, low, close]
    #Not to scale
    print("\n")
    j = 1
    list_len = len(data_list)
    
    while (j <= 10 and list_len > 1):

        for pre_num in range(0, list_len):
            tenR = (data_list[pre_num][1] - data_list[pre_num][2]) / 10

            if (data_list[pre_num][0] > data_list[pre_num][3]):
                if (j > (data_list[pre_num][1] - data_list[pre_num][0]) / tenR
                        and j <
                    (data_list[pre_num][1] - data_list[pre_num][3]) / tenR):
                    print("██dn", end="   ")
                else:
                    print(" |  ", end="   ")
            else:
                if (j < (data_list[pre_num][1] - data_list[pre_num][0]) / tenR
                        and j >
                    (data_list[pre_num][1] - data_list[pre_num][3]) / tenR):
                    print("██up", end="   ")
                else:
                    print(" |  ", end="   ")
        j = j + 1
        print(end="\n")
    print("\n")



def console_chart_v2(data_list):
    try:
        print("\n")
        j = 1
        list_len = len(data_list)
        lowest = data_list[1][1]
        highest = 0
    
        for pre_num in range(0, list_len):
            if (data_list[pre_num][2] < lowest):
                lowest = data_list[pre_num][2]
            if (data_list[pre_num][1] > highest):
                highest = data_list[pre_num][1]
        tenR = (highest - lowest) / 20
    
        while (j <= 20 and list_len > 1):
    
            for pre_num in range(0, list_len):
    
                if (data_list[pre_num][0] > data_list[pre_num][3]):
    
                    if ((((data_list[pre_num][2]) - lowest) / tenR) + j > 20
                            or ((highest) - data_list[pre_num][1]) / tenR >= j):
                        print(end="       ")
    
                    elif (j > (highest - data_list[pre_num][0]) / tenR and j <=
                          (highest - data_list[pre_num][3]) / tenR):
                        print("██dn", end="   ")
    
                    else:
                        print(" |  ", end="   ")
                else:
    
                    if ((((data_list[pre_num][2]) - lowest) / tenR) + j > 20
                            or ((highest) - data_list[pre_num][1]) / tenR >= j):
                        print(end="       ")
    
                    elif (j <= (highest - data_list[pre_num][0]) / tenR and j >
                          (highest - data_list[pre_num][3]) / tenR):
                        print("██up", end="   ")
                    else:
                        print(" |  ", end="   ")
            j = j + 1
            print(end="\n")
    except Exception as e:
        print("key error:",e)
        
    print("\n")
