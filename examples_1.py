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
    print("clock start time: {time}".format(time = beta.startTime()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock beta current time (s): {time}".format(time = beta.time()))
    print("stop clock beta")
    beta.stop()
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock beta current time (s): {time}".format(time = beta.time()))

    print

    print("create two gamma clocks")
    gamma1 = shijian.Clock(name = "gamma")
    gamma1 = shijian.Clock(name = "gamma")
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

if __name__ == '__main__':
    main()
