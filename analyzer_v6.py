class analyzer_class7:
    company_name = ""
    period_value = "5y"
    interval_value = "1d"
    code_string = ""
    i_diff = 5 #0
    match_num = 5
    data = None


    def __init__(self, _company_name):
        self.company_name = _company_name


    def interface(self):
        from yfinance import download as yf_download
        #from functions import show_additional
        from functions import country_code
        from functions import set_period
        from functions import multi

        company_name = self.company_name.upper()
        if (company_name == "S" or company_name == "SETTINGS"):
            self.company_name = input("entity name: ")
            self.code_string = country_code()
            print("1d, 5d")
            self.interval_value = str(input("interval: "))
            self.period_value = set_period(self.interval_value)
            self.i_diff = int(input("i-diff: "))
            #self.match_num = int(input("no. of matches: "))
            #show_additional(company_name)
            self.interface()
            
        elif (company_name == "M" or company_name == "MULTI"):
            company_list = {}
            company_list = multi()
            self.data = yf_download(company_list, period=self.period_value, interval=self.interval_value, threads=4, group_by="ticker")

            for company_name_n in company_list:
                self.company_name = company_name_n
                self.analyzer()
                
        elif (company_name == "T" or company_name == "TEST"):
            self.company_name = input("entity name: ")
            self.i_diff = 2
            self.interface()

        else:
            company_name = self.company_name + self.code_string
            self.data = yf_download(("MSFT",company_name,"SPY"), period=self.period_value, interval=self.interval_value, threads=4, group_by="ticker")
            self.analyzer()

    
    def analyzer(self):
        from functions import absDiffr
        from functions import absSlope
        from functions import console_chart_v2

        test_done = False
        self.i_diff = self.i_diff + 5
        self.match_num = 5
        itr_fail = 0
        company_name = self.company_name + self.code_string

        if (self.match_num < 2 or self.match_num > 5):
            self.match_num = 3
        i2 = i_match = self.match_num

        data = self.data[self.company_name]
        
        test_errors = {}
        test_errors[2] = test_errors[3] = test_errors[4] = test_errors[5] = 100

        while (True):
            data_len = len(data) - 1 - self.i_diff
            i = data_len + 1

            pre_values = {}
            accuracyR = {}
            valueR0 = {}
            valueR25 = {}
            value0_desc = {}
            minAccuracyR = {}
            avgValue0 = {}
            avgValue25 = {}

            openValue = highValue = lowValue = closeValue = 1
            openValue0 = highValue0 = lowValue0 = closeValue0 = 1
            openValue_1 = highValue_1 = lowValue_1 = closeValue_1 = 1
            match_open1 = match_high1 = match_low1 = match_close1 = 1
            minAccuracyR[0] = minAccuracyR[2] = minAccuracyR[3] = minAccuracyR[
                4] = minAccuracyR[5] = 2 * self.match_num
            accuracyR_sum = 0
            min_test_error = 100

            while (i > 0 and itr_fail < 7):
                i = i - 1

                try:
                #if (True):
                    if (isinstance((data['Open'][i].item()), float)):

                        openValue = (data['Open'][i].item())
                        highValue = (data['High'][i].item())
                        lowValue = (data['Low'][i].item())
                        closeValue = (data['Close'][i].item())

                        #0=26, 1=25, 2=24
                        for pre_num in range(0, (self.match_num)):
                            if (i == data_len):
                                pre_values[(
                                    pre_num + 1
                                )] = openValue, highValue, lowValue, closeValue
                                avgValue25[(pre_num + 1)] = (
                                    lowValue + ((highValue - lowValue) / 2))

                            pre_values[(pre_num)] = pre_values[(pre_num + 1)]
                            avgValue25[pre_num] = avgValue25[(pre_num + 1)]
                        pre_values[
                            self.
                            match_num] = openValue, highValue, lowValue, closeValue
                        avgValue25[self.match_num] = (
                            lowValue + ((highValue - lowValue) / 2))

                        if (data_len - i >= (self.match_num)):

                            #0=25, 1=24, 2=23
                            for pre_num in range(0, (self.match_num)):
                                valueR25[pre_num] = (
                                    ((pre_values[pre_num + 1][0]) -
                                     (pre_values[pre_num + 1][2])) /
                                    ((pre_values[pre_num + 1][1]) -
                                     (pre_values[pre_num + 1][2]))), (
                                         ((pre_values[pre_num + 1][3]) -
                                          (pre_values[pre_num + 1][2])) /
                                         ((pre_values[pre_num + 1][1]) -
                                          (pre_values[pre_num + 1][2])))

                            accuracyR_sum = 0
                            for pre_num in range(0, self.match_num):

                                accuracyR[pre_num] = (absDiffr(
                                    (valueR0[pre_num][0]),
                                    (valueR25[pre_num][0])) + absDiffr(
                                        (valueR0[pre_num][1]),
                                        (valueR25[pre_num][1]))) + (
                                            absSlope(
                                                ((avgValue0[pre_num]) -
                                                 (avgValue0[pre_num + 1])),
                                                ((avgValue25[pre_num]) -
                                                 (avgValue25[pre_num + 1]))) /
                                            self.match_num)

                                accuracyR_sum = accuracyR_sum + accuracyR[
                                    pre_num]
                            
                            if (test_done):

                                if (minAccuracyR[0] > accuracyR_sum):
                                    minAccuracyR[0] = accuracyR_sum
                                    i_match = len(data) - i + self.i_diff

                                    matchR = (lowValue0 +
                                              ((highValue0 - lowValue0) /
                                               2)) / (pre_values[1][2] +
                                                      ((pre_values[1][1] -
                                                        pre_values[1][2]) / 2))

                                    match_open1 = round(
                                        pre_values[0][0] * matchR, 2)
                                    match_high1 = round(
                                        pre_values[0][1] * matchR, 2)
                                    match_low1 = round(
                                        pre_values[0][2] * matchR, 2)
                                    match_close1 = round(
                                        pre_values[0][3] * matchR, 2)

                            else:

                                for pre_num in range(2, self.match_num + 1):
                                    accuracyR_sum = 0

                                    for pre_num_n in range(0, pre_num):
                                        accuracyR_sum = accuracyR_sum + accuracyR[
                                            pre_num_n]

                                    if (minAccuracyR[pre_num] > accuracyR_sum):
                                        minAccuracyR[pre_num] = accuracyR_sum

                                        matchR = (lowValue0 + (
                                            (highValue0 - lowValue0) / 2)) / (
                                                pre_values[1][2] +
                                                ((pre_values[1][1] -
                                                  pre_values[1][2]) / 2))

                                        match_open1_n = round(
                                            pre_values[0][0] * matchR, 2)
                                        match_high1_n = round(
                                            pre_values[0][1] * matchR, 2)
                                        match_low1_n = round(
                                            pre_values[0][2] * matchR, 2)
                                        match_close1_n = round(
                                            pre_values[0][3] * matchR, 2)

                                        self.test_error = ((
                                            ((absDiffr(highValue_1,
                                                       match_high1_n)) +
                                             (absDiffr(lowValue_1,
                                                       match_low1_n))) /
                                            ((highValue_1 + lowValue_1) / 2)
                                        ) * 50) * (absSlope(
                                            ((lowValue0 +
                                              ((highValue0 - lowValue0) / 2)) -
                                             (lowValue_1 +
                                              ((highValue_1 - lowValue_1) / 2))
                                             ),
                                            ((lowValue0 +
                                              ((highValue0 - lowValue0) / 2)) -
                                             (match_low1_n +
                                              ((match_high1_n - match_low1_n) /
                                               2)))) + 1)

                                        test_errors[pre_num] = self.test_error

                        else:
                            if (i == data_len):
                                openValue0 = openValue
                                highValue0 = highValue
                                lowValue0 = lowValue
                                closeValue0 = closeValue

                                if (not test_done):
                                    openValue_1 = (
                                        data['Open'][len(data) -
                                                     self.i_diff].item())
                                    highValue_1 = (
                                        data['High'][len(data) -
                                                     self.i_diff].item())
                                    lowValue_1 = (
                                        data['Low'][len(data) -
                                                    self.i_diff].item())
                                    closeValue_1 = (
                                        data['Close'][len(data) -
                                                      self.i_diff].item())

                            #0=25, 1=24, 2=23
                            valueR0[data_len - i] = (openValue - lowValue) / (
                                highValue - lowValue
                            ), (closeValue - lowValue) / (highValue - lowValue)

                            avgValue0[data_len -
                                      i] = (lowValue +
                                            ((highValue - lowValue) / 2))
                            avgValue0[(self.match_num)] = (
                                lowValue + ((highValue - lowValue) / 2))

                            value0_desc[
                                self.match_num - (data_len - i) -
                                1] = openValue, highValue, lowValue, closeValue
                            i2 = data_len - i + 1 + self.i_diff

                    else:
                        print("error for iteration: ", i, end="        \n")
                        itr_fail = itr_fail + 1

                except Exception as e:
                #else:
                    #print(company_name, i, end="   ")
                    #print(e)
                    itr_fail = itr_fail + 1

            if (test_done == False):
                test_done = True
                self.i_diff = self.i_diff - 5
            else:
                break

            min_test_error = 100
            for pre_num in range(2, self.match_num + 1):
                if (min_test_error > test_errors[pre_num]):
                    self.match_num = pre_num
                    min_test_error = test_errors[pre_num]
                    #print(pre_num, "- test_error", round(test_errors[pre_num], 2))

        if (test_done):

            perc_diff = (absDiffr(
                (lowValue0 + ((highValue0 - lowValue0) / 2)),
                (match_low1 +
                 ((match_high1 - match_low1) / 2)))) / (lowValue0 + (
                     (highValue0 - lowValue0) / 2)) * 100

            print("\n")
            print(company_name, end="   ")
            if ((100 - (minAccuracyR[0] / self.match_num / 2 * 100)) < 90
                    or perc_diff < 1 or perc_diff < self.test_error):
                print("X", end="\n")
            print(i2, "(matchTo)", i_match)
            print("upto", self.match_num, "candles", end=" ")
            print("with accuracy:",
                  int(100 - (minAccuracyR[0] / self.match_num / 2 * 100)),
                  " ",
                  "& diff:",
                  round(perc_diff, 2),
                  end="\n")

            print("period:", self.period_value, "    interval:",
                  self.interval_value)
            print("this day: ", round(openValue0, 2), " ",
                  round(highValue0, 2), " ", round(lowValue0, 2), " ",
                  round(closeValue0, 2))
            print("next day: ", match_open1, " ", match_high1, " ", match_low1,
                  " ", match_close1)
            #print("tst day: ", round(openValue_1, 2), " ", round(highValue_1, 2), " ", round(lowValue_1, 2), " ", round(closeValue_1, 2))

            if ((lowValue0 + ((highValue0 - lowValue0) / 2)) <
                (match_low1 + ((match_high1 - match_low1) / 2))):
                print("buy", end=" ")
                print("  target:", match_high1, "  stop loss:",
                      round((match_low1 - (match_high1 - match_low1)), 2))
            else:
                print("short", end=" ")
                print("  target:", match_low1, "  stop loss:",
                      round((match_high1 + (match_high1 - match_low1)), 2))

            #data = yf_download(tickers=company_name, period='5d', interval='1d')
            #print(data)

            value0_desc[
                self.
                match_num] = match_open1, match_high1, match_low1, match_close1

            console_chart_v2(value0_desc)