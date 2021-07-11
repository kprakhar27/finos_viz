import pandas as pd

## Create preprocessing pipeline for welcome survey
def welcome_survey(limit, df):
    a = pd.DataFrame()
    b = pd.DataFrame()
    for i in range(limit,limit+100):
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
    a['4'] = b['4']
    a['5'] = b['5']
    a['6'] = b['6']
    # a['7'] = b['7']
    # a['8'] = b['8']
    # a['9'] = b['9']

    # drop unnecessary columns
    a = a.drop(columns = ['7', '8', '9','10'])

    # clean column '0'
    for i in range(len(a)):
        if len(a['0'][i]) == 1:
            a['0'][i] = a['0'][i][0]
        else:
            a['0'][i] = 'No Country'
    
    # clean column '1'
    for i in range(len(a)):
        if len(a['1'][i]) == 1:
            a['1'][i] = a['1'][i][0]
        else:
            a['1'][i] = 'No City'
    
    # clean column '2'
    for i in range(len(a)):
        if len(a['2'][i]) == 1:
            a['2'][i] = a['2'][i][0]
        else:
            a['2'][i] = 'Null'
    
    # clean column '3'
    for i in range(len(a)):
        if len(a['3'][i]) == 1:
            a['3'][i] = a['3'][i][0]
        else:
            a['3'][i] = 'Null'
    
    # clean column '4'
    for i in range(len(a)):
        if type(a['4'][i]) == list:
            if len(a['4'][i]) == 1:
                if a['4'][i][0] == 0:
                    a['4'][i] = 'Primary school'
                elif a['4'][i][0] == 1:
                    a['4'][i] = 'Elementary school'
                elif a['4'][i][0] == 2:
                    a['4'][i] = 'High school'
                elif a['4'][i][0] == 3:
                    a['4'][i] = '2 year college degree'
                elif a['4'][i][0] == 4:
                    a['4'][i] = 'Bachelor'
                elif a['4'][i][0] == 5:
                    a['4'][i] = 'Master'
                elif a['4'][i][0] == 6:
                    a['4'][i] = 'Doctoral degree'
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
                    a['5'][i] = 'Single'
                elif a['5'][i][0] == 1:
                    a['5'][i] = 'Married'
                elif a['5'][i][0] == 2:
                    a['5'][i] = 'Divorced'
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
                    a['6'][i] = 'Yes'
                elif a['6'][i][0] == 1:
                    a['6'][i] = 'No'
                else:
                    a['6'][i] = 'Null'
            else:
                a['6'][i] = 'Null'
        else:
            a['6'][i] = 'Null'

    # Return the dataframe
    return a