import random
import logging
import threading
import tornado.websocket
import tornado.web
import tornado.ioloop
from datetime import date, datetime
from perspective import Table, PerspectiveManager, PerspectiveTornadoHandler

import requests
import pandas as pd
import io
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import sys
from catchException import exception_handler



## handle exception properly
## make it summarised info , hide traceback
sys.excepthook = exception_handler
#####

# Add token before running swerver
### we can parse this to yaml file
token = ""
api='https://endapi.truefeedback.io/dataplatform/survey/1/answers?limit=40000&offset=0'



###########################################################################
#### update in case of connection problem or 
### server is down
## create a session
try:
    s = requests.Session()
    ##

    ## configure session retry
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[ 500, 502, 503, 504 ]) ## force status retry if code returned is 500, 502, 504
    ##


    ### mount an adapter
    s.mount('http://', HTTPAdapter(max_retries=retries))
    ##

    ### establish a get on the api
    getApi = s.get(api, headers={"auth": token} )
    ##

    ## the content retry
    ##a=requests.get(api,headers={"auth": token}).content
    a = getApi.content 
    df=pd.read_json(a)
except  (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
    raise Exception('There is an http connection problem. Check the connection error', str(e))
except ValueError as e:
    raise ValueError('Data not in json format.', str(e))
except:
    raise Exception('a problem has occurred with connection/connection parameters or data format')
    #sys.exit()

##########################################################################

###################### previous connection configuration ###############33
# a=requests.get(api,headers={"auth": token}).content
# df=pd.read_json(a)
###############################################################




def data_source():
    rows = []
    for i in range(5):
        rows.append(
            {
                "q0": df['answers'][i]['0']['values'][0],
                "q1": df['answers'][i]['1']['values'][0],
                "q2": df['answers'][i]['2']['values'][0],
                "q3": df['answers'][i]['3']['values'][0],
                # "q4": df['answers'][i]['4'],
                # "q5": df['answers'][i]['5'],
                # "q6": df['answers'][i]['6'],
                # "q7": df['answers'][i]['7'],
                # "q8": df['answers'][i]['8'],
                # "q9": df['answers'][i]['9'],
                "q10": df['answers'][i]['10']['values'][0],
            }
        )
    return rows


def perspective_thread(manager):
    """Perspective application thread starts its own tornado IOLoop, and
    adds the table with the name "data_source_one", which will be used
    in the front-end."""
    psp_loop = tornado.ioloop.IOLoop()
    manager.set_loop_callback(psp_loop.add_callback)
    table = Table(
        {
            "q0": str,
            "q1": str,
            "q2": str,
            "q3": str,
            # "q4": dict,
            # "q5": dict,
            # "q6": dict,
            # "q7": dict,
            # "q8": dict,
            # "q9": dict,
            "q10": str,
        },
        limit=250,
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
