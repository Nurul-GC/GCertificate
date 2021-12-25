# ******************************************************************************
#  Copyright (c) 2021 Nurul-GC.                                                *
# ******************************************************************************

from os import curdir
from subprocess import getoutput
from time import sleep

if __name__ == '__main__':
    log = getoutput("heroku logs")
    sleep(0.5)
    with open("heroku_logs.txt", "+w") as log_file:
        log_file.write(log)
    print('done..')
