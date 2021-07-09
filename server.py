import random
import logging
import threading
import tornado.websocket
import tornado.web
import tornado.ioloop
from datetime import date, datetime
from perspective import Table, PerspectiveManager, PerspectiveTornadoHandler

import pandas as pd
import io
from dataValuation import collectApiData
import requests




### data token
token = ""
### session that can be reused for the answer or survey api type
## this line will need to be updated to take in surveys and answers
s = requests.Session()
#api = 'https://endapi.truefeedback.io/dataplatform/survey/1/answers?limit=40000&offset=0'

df = collectApiData(session=s, apitype="answers",token=token )
limit = 0
### initial way of getting the api
# a=requests.get(api,headers={"auth": token}).content
# df=pd.read_json(a)

def data_source():
    global limit
    a = pd.DataFrame()
    b = pd.DataFrame()
    # k = pd.DataFrame()
    # token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVkZW50aWFscyI6InByaXZhdGUtZGF0YS1wbGF0Zm9ybS1rZXkgZm9yIGFscGhhIiwiY3JlYXRlZEF0IjoiMjAyMS0wNi0yOFQxODoxNjoyOC4yNThaIiwiaWF0IjoxNjI0OTA0MTg4fQ.ITcG3EO90Uzc9JZYjE6g5mbmh4kkHBDO6QEumQ8ZruQ'
    # url="https://endapi.truefeedback.io/dataplatform/survey/1/answers?limit=400&offset=%d&sort=desc"%offset
    # s=requests.get(url,headers={"auth": token}).content
    # k=pd.read_json(s)
    for i in range(limit,limit+100):
        row=pd.DataFrame.from_dict(df['answers'][i])
        sel = pd.DataFrame.from_dict(df['answers'][i])
        row = row.drop(row.index[[0]])
        sel = sel.drop(sel.index[[1]])
        a = a.append(row, ignore_index=True)
        b = b.append(sel, ignore_index=True)
    limit = limit+100
    a['4'] = b['4']
    a['5'] = b['5']
    a['6'] = b['6']
    a['7'] = b['7']
    a['8'] = b['8']
    a['9'] = b['9']
    a = a.drop(columns = ['7', '8', '9','10'])
    for i in range(len(a)):
        if len(a['0'][i]) == 1:
            a['0'][i] = a['0'][i][0]
        else:
            a['0'][i] = 'No Country'
    for i in range(len(a)):
        if len(a['1'][i]) == 1:
            a['1'][i] = a['1'][i][0]
        else:
            a['1'][i] = 'No City'
    for i in range(len(a)):
        if len(a['2'][i]) == 1:
            a['2'][i] = a['2'][i][0]
        else:
            a['2'][i] = 'Null'
    for i in range(len(a)):
        if len(a['3'][i]) == 1:
            a['3'][i] = a['3'][i][0]
        else:
            a['3'][i] = 'Null'
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
    return a


def perspective_thread(manager):
    """Perspective application thread starts its own tornado IOLoop, and
    adds the table with the name "data_source_one", which will be used
    in the front-end."""
    psp_loop = tornado.ioloop.IOLoop()
    manager.set_loop_callback(psp_loop.add_callback)
    table = Table(
        {
            "0": str,
            "1": str,
            "2": str,
            "3": str,
            "4": str,
            "5": str,
            "6": str,
            # "uid": int,
            # "q7": dict,
            # "q8": dict,
            # "q9": dict,
            # "q10": str,
        },
    )

    # Track the table with the name "data_source_one", which will be used in
    # the front-end to access the Table.
    manager.host_table("data_source_one", table)

    # update with new data every 50ms
    def updater():
        table.update(data_source())

    callback = tornado.ioloop.PeriodicCallback(callback=updater, callback_time=50)
    callback.start()
    psp_loop.start()


def make_app():
    manager = PerspectiveManager()

    thread = threading.Thread(target=perspective_thread, args=(manager,))
    thread.daemon = True
    thread.start()

    return tornado.web.Application(
        [
            # create a websocket endpoint that the client Javascript can access
            (
                r"/websocket",
                PerspectiveTornadoHandler,
                {"manager": manager, "check_origin": True},
            ),
            (
                r"/node_modules/(.*)",
                tornado.web.StaticFileHandler,
                {"path": "./node_modules/@finos/"},
            ),
            (
                r"/(.*)",
                tornado.web.StaticFileHandler,
                {"path": "./", "default_filename": "index.html"},
            ),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    logging.critical("Listening on http://localhost:8080")
    loop = tornado.ioloop.IOLoop.current()
    loop.start()
