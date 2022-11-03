from status_user import *
import threading
from time import sleep

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


token = "your_auth_token"
unix_time = UNIX_TIME

def changeStatus2(icon, status):
    changeStatus(token, status, icon, unix_time)


def main():
    try:
        def run0():
            changeStatus2("🖥️", "Check Socials")

        def run1():
            changeStatus2("📎", "klbu.eu")

        def run2():
            changeStatus2("🏠", "klubuntu.live")

        def run3():
            changeStatus2("😺", "Git:Klubuntu")

        def run4():
            changeStatus2("📺", "YT:@Klubuntu")


        def main1():
            run0()
            sleep(5)
            run1()
            sleep(5)
            run2()
            sleep(5)
            run3()
            sleep(5)
            run4()
            sleep(5)
        main1()
        set_interval(main1, 28)
    finally:
        changeStatus2("📺", "Watching Youtube")


def __del__(self):
    changeStatus2("📺", "Watching Youtube")


if __name__=='__main__':
    main()



