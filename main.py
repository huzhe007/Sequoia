# -*- encoding: UTF-8 -*-

import logging

import settings
import work_flow

logging.basicConfig(format='%(asctime)s %(message)s', filename='sequoia.log')
logging.getLogger().setLevel(logging.INFO)

# def job():
#     if utils.is_weekday():
#         work_flow.process()
#
#
# settings.init()
# EXEC_TIME = "15:15"
# schedule.every().day.at(EXEC_TIME).do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

settings.init()
work_flow.process()
