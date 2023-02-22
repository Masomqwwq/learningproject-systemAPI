import sys
from flask import Flask
from flask_restful import Api
import time
import traceback
import asyncio
import classHandler


def main():
    app = Flask(__name__)
    api = Api(app)
    for cl in classHandler.classes:
        api.add_resource(cl, cl.endpoint)
    app.run()


def main_handler():
    try:
        main()
    except Exception as err:
        print("failure")
        logpath = "log/crash" + time.strftime("%m.%d.%Y.%H.%M.%S", time.localtime()) + ".txt"
        with open(logpath, "w") as log:
            log.write(str(err))
            log.write(traceback.format_exc())
            log.close()
        print(f"The system has encountered an error, a report can be found at {logpath}")


if __name__ == "__main__":
    main_handler()