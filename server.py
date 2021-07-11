
# import random
import logging
import threading
import requests

import pandas as pd

import tornado.websocket
import tornado.web
import tornado.ioloop

from perspective import Table, PerspectiveManager, PerspectiveTornadoHandler

from dataValuation import collectApiData
from dataProcessing import welcome_survey


### data token
token = ""


### session that can be reused for the answer or survey api type
## this line will need to be updated to take in surveys and answers
s = requests.Session()
#api = 'https://endapi.truefeedback.io/dataplatform/survey/1/answers?limit=40000&offset=0'

df = collectApiData(session=s, apitype="answers",token=token )
df1 = pd.DataFrame()
df2 = pd.DataFrame()
## global variable which will increase offset after every function call
offset = 10000

tracker = 1


## Multithread function to update df 
# def update_df():
#     global df
#     global offset
#     global tracker
#     global df1
#     global df2
#     if tracker%2==0:
#         df1= collectApiData(session=s, apitype="answers",token=token,offset=offset )
#         offset = offset+10000
#         tracker = tracker + 1
#     else:
#         df2= collectApiData(session=s, apitype="answers",token=token,offset=offset )
#         offset = offset+10000
#         tracker = tracker + 1
    # pass


limit = 0
### initial way of getting the api
# a=requests.get(api,headers={"auth": token}).content
# df=pd.read_json(a)

def data_source():
    global limit
    data = welcome_survey(limit=limit,df=df)
    limit = limit+100

    return data
    


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
    # data_thread = threading.Thread(target=update_df)
    # data_thread.start()

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
