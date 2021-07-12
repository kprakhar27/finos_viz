import pandas as pd

## Create preprocessing pipeline for welcome survey
def e_survey(limit, df):
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
    a['1'] = b['1']
    a['2'] = b['2']
    a['3'] = b['3']
    a['4'] = b['4']
    a['5'] = b['5']
    a['6'] = b['6']


    # drop unnecessary columns
    #a = a.drop(columns = ['8','9','10','11', '12', '13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43'])
    if i < 678:
        # clean column '0'
        for i in range(len(a)):
            if type(a['0'][i]) == list:
                if len(a['0'][i]) == 1:
                    if a['0'][i][0] == 0:
                        a['0'][i] = 'Çok iyi'
                    elif a['0'][i][0] == 1:
                        a['0'][i] = 'İyi'
                    elif a['0'][i][0] == 2:
                        a['0'][i] = 'Normal'
                    elif a['0'][i][0] == 3:
                        a['0'][i] = 'Kötü'
                    elif a['0'][i][0] == 4:
                        a['0'][i] = 'Çok kötü'
                    else:
                        a['0'][i] = 'Null'
                else:
                    a['0'][i] = 'Null'
            else:
                a['0'][i] = 'Null'
        
        # clean column '1'
        for i in range(len(a)):
            if type(a['1'][i]) == list:
                if len(a['1'][i]) == 1:
                    if a['1'][i][0] == 0:
                        a['1'][i] = 'Her gün'
                    elif a['1'][i][0] == 1:
                        a['1'][i] = 'Haftada bir'
                    elif a['1'][i][0] == 2:
                        a['1'][i] = 'Ayda bir'
                    elif a['1'][i][0] == 3:
                        a['1'][i] = 'Üç ayda bir'
                    elif a['1'][i][0] == 4:
                        a['1'][i] = 'Yılda bir kez'
                    elif a['1'][i][0] == 5:
                        a['1'][i] = 'Hiç gitmiyorum'
                    else:
                        a['1'][i] = 'Null'
                else:
                    a['1'][i] = 'Null'
            else:
                a['1'][i] = 'Null'
        
        # clean column '2'
        for i in range(len(a)):
            if type(a['2'][i]) == list:
                if len(a['2'][i]) == 1:
                    if a['2'][i][0] == 0:
                        a['2'][i] = 'Meyve-Sebze'
                    elif a['2'][i][0] == 1:
                        a['2'][i] = 'Şarküteri'
                    elif a['2'][i][0] == 2:
                        a['2'][i] = 'Balık'
                    elif a['2'][i][0] == 3:
                        a['2'][i] = 'Temizlik'
                    elif a['2'][i][0] == 4:
                        a['2'][i] = 'Bebek - Kişisel Bakım'
                    elif a['2'][i][0] == 5:
                        a['2'][i] = 'Aktüel'
                    else:
                        a['2'][i] = 'Null'
                else:
                    a['2'][i] = 'Null'
            else:
                a['2'][i] = 'Null'
        
        # clean column '3'
        for i in range(len(a)):
            if type(a['3'][i]) == list:
                if len(a['3'][i]) == 1:
                    if a['3'][i][0] == 0:
                        a['3'][i] = 'Meyve-Sebze'
                    elif a['3'][i][0] == 1:
                        a['3'][i] = 'Şarküteri'
                    elif a['3'][i][0] == 2:
                        a['3'][i] = 'Balık'
                    elif a['3'][i][0] == 3:
                        a['3'][i] = 'Temizlik'
                    elif a['3'][i][0] == 4:
                        a['3'][i] = 'Bebek - Kişisel Bakım'
                    elif a['3'][i][0] == 5:
                        a['3'][i] = 'Aktüel'
                    else:
                        a['3'][i] = 'Null'
                else:
                    a['3'][i] = 'Null'
            else:
                a['3'][i] = 'Null'
        
        # clean column '4'
        for i in range(len(a)):
            if type(a['4'][i]) == list:
                if len(a['4'][i]) == 1:
                    if a['4'][i][0] == 0:
                        a['4'][i] = 'Fiyat'
                    elif a['4'][i][0] == 1:
                        a['4'][i] = 'Yakınlık'
                    elif a['4'][i][0] == 2:
                        a['4'][i] = 'Bol çeşit'
                    elif a['4'][i][0] == 3:
                        a['4'][i] = 'Hizmet Kalitesi'
                    elif a['4'][i][0] == 4:
                        a['4'][i] = 'Temizlik'
                    else:
                        a['4'][i] = 'Null'
                else:
                    a['4'][i] = 'Null'
            else:
                a['4'][i] = 'Null'
        
        # clean column '5'
        for i in range(len(a)):
            if type(a['5'][i]) == list:
                if len(a['5'][i]) == 1:
                    if a['5'][i][0] == 0:
                        a['5'][i] = 'Yüksek fiyat'
                    elif a['5'][i][0] == 1:
                        a['5'][i] = 'Ürün çeşidi yetersiz'
                    elif a['5'][i][0] == 2:
                        a['5'][i] = 'Temiz – hijyenik değil'
                    elif a['5'][i][0] == 3:
                        a['5'][i] = 'Hizmet kalites'
                    elif a['5'][i][0] == 4:
                        a['5'][i] = 'Muhatap bulamıyorum'
                    elif a['5'][i][0] == 5:
                        a['5'][i] = 'Personel sorunu var'
                    elif a['5'][i][0] == 6:
                        a['5'][i] = 'İade sorunu'
                    elif a['5'][i][0] == 7:
                        a['5'][i] = 'Erişim zorluğu'
                    else:
                        a['5'][i] = 'Null'
                else:
                    a['5'][i] = 'Null'
            else:
                a['5'][i] = 'Null'
        
        # clean column '6'
        for i in range(len(a)):
            if type(a['6'][i]) == list:
                if len(a['6'][i]) == 1:
                    if a['6'][i][0] == 0:
                        a['6'][i] = 'Carrefoursa'
                    elif a['6'][i][0] == 1:
                        a['6'][i] = 'Metro'
                    elif a['6'][i][0] == 2:
                        a['6'][i] = 'Migros'
                    elif a['6'][i][0] == 3:
                        a['6'][i] = 'BİM'
                    elif a['6'][i][0] == 4:
                        a['6'][i] = 'Hiçbiri'
                    else:
                        a['6'][i] = 'Null'
                else:
                    a['6'][i] = 'Null'
            else:
                a['6'][i] = 'Null'

        # clean column '7'
        for i in range(len(a)):
            if type(a['7'][i]) == list:
                if len(a['7'][i]) == 1:
                    a['7'][i] = a['7'][i][0]
                else:
                    a['7'][i] = 'No products'
            else:
                a['7'][i] = 'No products'

        # Return the dataframe
        return a