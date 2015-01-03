import time
import shijian

def main():

    print("create clock alpha")
    alpha = shijian.Clock(name = "alpha")
    print("clock alpha start time: {time}".format(time = alpha.startTime()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock alpha current time (s): {time}".format(time = alpha.time()))

    print

    print("create clock beta")
    beta = shijian.Clock(name = "beta")
    print("clock beta start time: {time}".format(time = beta.startTime()))
    print("clock beta stop time: {time}".format(time = beta.stopTime()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock beta current time (s): {time}".format(time = beta.time()))
    print("stop clock beta")
    beta.stop()
    print("clock beta start time: {time}".format(time = beta.startTime()))
    print("clock beta stop time: {time}".format(time = beta.stopTime()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock beta start time: {time}".format(time = beta.startTime()))
    print("clock beta stop time: {time}".format(time = beta.stopTime()))
    print("clock beta current time (s): {time}".format(time = beta.time()))

    print
    print("clock beta printout:")
    print
    beta.printout()

#    print("run function 1 (which is timed using a decorator)")
#    function1()
#
#    print

    print("create two gamma clocks")
    gamma = shijian.Clock(name = "gamma")
    gamma = shijian.Clock(name = "gamma")
    print("sleep 2 seconds")
    time.sleep(2)

    print

    print("create two unnamed clocks")
    delta = shijian.Clock()
    epsilon = shijian.Clock()
    print("sleep 2 seconds")
    time.sleep(2)

    print

    print("clocks full printout:\n")
    shijian.clocks.printout(style = "full")

    print("clocks statistics printout:\n")
    shijian.clocks.printout()

#@shijian.timer
#def function1():
#    print("function 1 initiate")
#    time.sleep(4)
#    print("function 1 terminate")

if __name__ == '__main__':
    main()
