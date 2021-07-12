import pandas as pd

## Create preprocessing pipeline for welcome survey
def mall_survey(limit, df):
    a = pd.DataFrame()
    b = pd.DataFrame()
    for i in range(limit,limit+100):
        if i >= 678:
            break
        else:
        # parse dictionaries from each row of data frame
            row=pd.DataFrame.from_dict(df['answers'][i])
            sel = pd.DataFrame.from_dict(df['answers'][i])
            # drop row with index selected
            row = row.drop(row.index[[0]])
            # drop row with index  values
            sel = sel.drop(sel.index[[1]])
            # append each row to the empty dataframes
            a = a.append(row, ignore_index=True)
            b = b.append(sel, ignore_index=True)
    # merge useful columns from b to a
    a['0'] = b['0']
    a['2'] = b['2']
    a['4'] = b['4']
    a['6'] = b['6']
    a['8'] = b['8']


    # drop unnecessary columns
    #a = a.drop(columns = ['10','11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43'])
    if i < 678:
        # clean column '0'
        for i in range(len(a)):
            if type(a['0'][i]) == list:
                if len(a['0'][i]) == 1:
                    if a['0'][i][0] == 0:
                        a['0'][i] = 'Vatan'
                    elif a['0'][i][0] == 1:
                        a['0'][i] = 'Media Markt'
                    elif a['0'][i][0] == 2:
                        a['0'][i] = 'Teknosa'
                    elif a['0'][i][0] == 3:
                        a['0'][i] = 'Diğer'
                    else:
                        a['0'][i] = 'Null'
                else:
                    a['0'][i] = 'Null'
            else:
                a['0'][i] = 'Null'
        
        # clean column '1'
        for i in range(len(a)):
            if len(a['1'][i]) == 1:
                a['1'][i] = a['1'][i][0]      
            else:
                a['1'][i] = 'No Store'
        
        # clean column '2'
        for i in range(len(a)):
            if type(a['2'][i]) == list:
                if len(a['2'][i]) == 1:
                    if a['2'][i][0] == 0:
                        a['2'][i] = 'Vatan'
                    elif a['2'][i][0] == 1:
                        a['2'][i] = 'Media Markt'
                    elif a['2'][i][0] == 2:
                        a['2'][i] = 'Teknosa'
                    elif a['2'][i][0] == 3:
                        a['2'][i] = 'İnternet Pazar Yerleri'
                    elif a['2'][i][0] == 4:
                        a['2'][i] = 'Diğer'
                    else:
                        a['2'][i] = 'Null'
                else:
                    a['2'][i] = 'Null'
            else:
                a['2'][i] = 'Null'
        
        # clean column '3'
        for i in range(len(a)):
            if len(a['3'][i]) == 1:
                a['3'][i] = a['3'][i][0]        
            else:
                a['3'][i] = 'No visits'
        
        # clean column '4'
        for i in range(len(a)):
            if type(a['4'][i]) == list:
                if len(a['4'][i]) == 1:
                    if a['4'][i][0] == 0:
                        a['4'][i] = 'Ürünü görmek'
                    elif a['4'][i][0] == 1:
                        a['4'][i] = 'Satış temsilcisinden hızlı bilgiye erişebilmek'
                    elif a['4'][i][0] == 2:
                        a['4'][i] = 'Alışkanlık'
                    elif a['4'][i][0] == 3:
                        a['4'][i] = 'Satın alma davranışı sonrasında muhatap kişiye kolay ulaşım'
                    elif a['4'][i][0] == 4:
                        a['4'][i] = 'Güvenilir olması'
                    elif a['4'][i][0] == 5:
                        a['4'][i] = 'Aktüel'
                    elif a['4'][i][0] == 6:
                        a['4'][i] = 'Diğer'
                    else:
                        a['4'][i] = 'Null'
                else:
                    a['4'][i] = 'Null'
            else:
                a['4'][i] = 'Null'
        
        # clean column '5'
        for i in range(len(a)):
            if len(a['5'][i]) == 1:
                a['5'][i] = a['5'][i][0]        
            else:
                a['5'][i] = 'Neither'
        
        # clean column '6'
        for i in range(len(a)):
            if type(a['6'][i]) == list:
                if len(a['6'][i]) == 1:
                    if a['6'][i][0] == 0:
                        a['6'][i] = 'Kentplaza AVM'
                    elif a['6'][i][0] == 1:
                        a['6'][i] = 'Kule Site'
                    elif a['6'][i][0] == 2:
                        a['6'][i] = 'M1'
                    elif a['6'][i][0] == 3:
                        a['6'][i] = 'Novaland'
                    elif a['6'][i][0] == 4:
                        a['6'][i] = 'Selçuker Center'
                    elif a['6'][i][0] == 5:
                        a['6'][i] = 'Diğer'
                    else:
                        a['6'][i] = 'Null'
                else:
                    a['6'][i] = 'Null'
            else:
                a['6'][i] = 'Null'

        # clean column '7'
        for i in range(len(a)):
            if len(a['7'][i]) == 1:
                a['7'][i] = a['7'][i][0]        
            else:
                a['7'][i] = 'No mall'

        # clean column '8'
        for i in range(len(a)):
            if type(a['8'][i]) == list:
                if len(a['8'][i]) == 1:
                    if a['8'][i][0] == 0:
                        a['8'][i] = 'Kentplaza AVM'
                    elif a['8'][i][0] == 1:
                        a['8'][i] = 'Kule Site'
                    elif a['8'][i][0] == 2:
                        a['8'][i] = 'M1'
                    elif a['8'][i][0] == 3:
                        a['8'][i] = 'Novaland'
                    elif a['8'][i][0] == 4:
                        a['8'][i] = 'Selçuker Center'
                    elif a['8'][i][0] == 5:
                        a['8'][i] = 'Diğer'
                    else:
                        a['8'][i] = 'Null'
                else:
                    a['8'][i] = 'Null'
            else:
                a['8'][i] = 'Null'

        # clean column '9'
        for i in range(len(a)):
            if type(a['9'][i]) == list:
                if len(a['9'][i]) == 1:
                    a['9'][i] = a['9'][i][0]
                else:
                    a['9'][i] = 'No expenditure'
            else:
                a['9'][i] = 'No expenditure'

        # Return the dataframe
        return a