import os
import time
import thread
import curses

UMASK = 0
WORKDIR = "/"
MAXFD = 1024
REDIRECT_TO = os.devnull

stdscr = curses.initscr()

def getid():
   # instant_key = str(raw_input())
  # instant_key
    user_input=""
    while(True):
        #if(len(user_input) > 5):
        print user_input
         #   os._exit(os.getpid())
        user_input =  str(stdscr.getch())

def Create_deamon(func,args=""):
    try:
        pid = os.fork()
    except OSError, e:
        raise Exception, "%s [%d]" % (e.strerror, e.errno)

    if (pid == 0):
        os.setsid()
        os.chdir(WORKDIR)
        os.umask(UMASK)
    else:
        os._exit(0)

    func(*args)

Create_deamon(getid,())
"""


def child():
   print(os.getpid())

def parent():
   while(True):
       time.sleep(1)
       pid = os.fork()
       thread.start_new_thread(child,())
parent()

"""