#!/usr/bin/env python

import inspect
import time

import shijian

def main():

    print("create clock alpha")
    alpha = shijian.Clock(name = "alpha")
    print("clock alpha start time: {time}".format(time = alpha.start_time()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock alpha current time (s): {time}".format(time = alpha.time()))

    print("\ncreate clock beta")
    beta = shijian.Clock(name = "beta")
    print("clock beta start time: {time}".format(time = beta.start_time()))
    print("clock beta stop time: {time}".format(time = beta.stop_time()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock beta current time (s): {time}".format(time = beta.time()))
    print("stop clock beta")
    beta.stop()
    print("clock beta start time: {time}".format(time = beta.start_time()))
    print("clock beta stop time: {time}".format(time = beta.stop_time()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock beta start time: {time}".format(time = beta.start_time()))
    print("clock beta stop time: {time}".format(time = beta.stop_time()))
    print("clock beta current time (s): {time}".format(time = beta.time()))

    print("\nclock beta printout:\n")
    beta.printout()

    print("create two gamma clocks")
    gamma = shijian.Clock(name = "gamma")
    gamma = shijian.Clock(name = "gamma")
    print("sleep 2 seconds")
    time.sleep(2)

    print("\ncreate two unnamed clocks")
    delta = shijian.Clock()
    epsilon = shijian.Clock()
    print("sleep 2 seconds")
    time.sleep(2)

    print("\nrun function 1 (which is timed using internal clocks)")
    print("result of function 1: {result}".format(result = function_1()))

    print("\nrun function 2 (which is timed using a decorator)")
    print("result of function 2: {result}".format(result = function_2()))

    print("\ncreate clock zeta, to illustrate clock resets")
    zeta = shijian.Clock(name = "zeta")
    print("clock zeta start time: {time}".format(time = zeta.start_time()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock zeta current time (s): {time}".format(time = zeta.time()))
    print("reset clock zeta and start it again")
    zeta.reset()
    zeta.start()
    print("clock zeta start time: {time}".format(time = zeta.start_time()))
    print("sleep 2 seconds")
    time.sleep(2)
    print("clock zeta current time (s): {time}".format(time = zeta.time()))

    print("\nclocks full printout:\n")
    shijian.clocks.printout(style = "full")

    print("clocks statistics printout:\n")
    shijian.clocks.printout()

def function_1():
    function_name = inspect.stack()[0][3]
    clock = shijian.Clock(name = function_name)
    print("initiate {function_name}".format(function_name = function_name))
    time.sleep(3)
    print("terminate {function_name}".format(function_name = function_name))
    clock.stop()
    return(3)

@shijian.timer
def function_2():
    function_name = inspect.stack()[0][3]
    print("initiate {function_name}".format(function_name = function_name))
    time.sleep(4)
    print("terminate {function_name}".format(function_name = function_name))
    return(4)

if __name__ == '__main__':
    main()
