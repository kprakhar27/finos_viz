import pandas as pd
import random
from datetime import date, datetime

import requests
import pandas as pd
import io
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVkZW50aWFscyI6InByaXZhdGUtZGF0YS1wbGF0Zm9ybS1rZXkgZm9yIGFscGhhIiwiY3JlYXRlZEF0IjoiMjAyMS0wNi0yOFQxODoxNjoyOC4yNThaIiwiaWF0IjoxNjI0OTA0MTg4fQ.ITcG3EO90Uzc9JZYjE6g5mbmh4kkHBDO6QEumQ8ZruQ'
api='https://endapi.truefeedback.io/dataplatform/survey/1/answers?limit=40000&offset=0'
a=requests.get(api,headers={"auth": token}).content
df=pd.read_json(a)



# def data_source():
#     rows = []
#     modifier = random.random() * random.randint(1, 50)
#     for i in range(5):
#         rows.append(
#             {
#                 "name": SECURITIES[random.randint(0, len(SECURITIES) - 1)],
#                 "client": CLIENTS[random.randint(0, len(CLIENTS) - 1)],
#                 "open": (random.random() * 75 + random.randint(0, 9)) * modifier,
#                 "high": (random.random() * 105 + random.randint(1, 3)) * modifier,
#                 "low": (random.random() * 85 + random.randint(1, 3)) * modifier,
#                 "close": (random.random() * 90 + random.randint(1, 3)) * modifier,
#                 "lastUpdate": datetime.now(),
#                 "date": date.today(),
#             }
#         )
#     return rows


# SECURITIES = [
#     "AAPL.N",
#     "AMZN.N",
#     "QQQ.N",
#     "NVDA.N",
#     "TSLA.N",
#     "FB.N",
#     "MSFT.N",
#     "TLT.N",
#     "XIV.N",
#     "YY.N",
#     "CSCO.N",
#     "GOOGL.N",
#     "PCLN.N",
# ]

# CLIENTS = ["Homer", "Marge", "Bart", "Lisa", "Maggie", "Moe", "Lenny", "Carl", "Krusty"]


def data_source():
    rows = []
    for i in range(5):
        rows.append(
            {
                "q0": df['answers'][i]['0'],
                "q1": df['answers'][i]['1'],
                "q2": df['answers'][i]['2'],
                "q3": df['answers'][i]['3'],
                "q4": df['answers'][i]['4'],
                "q5": df['answers'][i]['5'],
                "q6": df['answers'][i]['6'],
                "q7": df['answers'][i]['7'],
                "q8": df['answers'][i]['8'],
                "q9": df['answers'][i]['9'],
                "q10": df['answers'][i]['10'],
            }
        )
    return rows
print(data_source())