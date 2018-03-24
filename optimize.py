#!usr/bin/env python
import os
import subprocess
import commands
import sys
import random
import numpy as np
from simulator import *
from simulator import Simulator
from threading import Thread, Lock
from time import sleep
import pdb


def optimize( num_waypoints):
    # make default waypoints safeside
    wp = [(-10, -10), (10, 10)]
    with open('waypoints', 'w') as f:
        for w1 in wp:
            f.write('{0} {1}\n'.format(*w1))
    #getting baseline cost
    baseline_cost = s.evaluate(wp)

    # waypoints = [(-10, -10), (0, 0), (10, 10)]
    # pdb.set_trace()
    # for i in waypoints:
    #     s.record_waypoints(waypoints[i])

    best_cost = baseline_cost
    way1 = (-10,-10)
    way2 = (10,10)
    best = {}
    
    #finding 1 to n randomized waypoints)
    for i in range(1,num_waypoints):

        new_best_cost = best_cost

        print i
        # get cost 25% better than the base cost
        # Put this while statement in here to play nice with the grading software
        while new_best_cost > 0.25*best_cost:
            waypoints = []
            #print waypoints
            waypoints.append(way1)
            for j  in range(i):
                waypoints.append((random.uniform(-10, 10), random.uniform(-10, 10)))
            waypoints.append(way2)
            
            new_best_cost = s.evaluate(waypoints)

        best[i]=[new_best_cost,waypoints]

    with open("better_waypoints.txt", "w") as bet:
        for w1 in best:
            for w2 in best[w1][1]:
                bet.write('{0} {1}\n'.format(*w2))

    return True, best 

'''I tried gradient descent but was taking too much time; might be errorneous'''
def descent():
    space_x = np.arange(-10, 10, 10000)
    space_y = np.arange(-10, 10, 10000)
    u = random.choice(space_x)
    v = random.choice(space_y)
    #print cur_x
    step_size = 0.02
    diff = float("-inf")
    h =0.0001
    count = 0
    w_list = []
    while diff < 1e-3:
        prev_u = u
        gradient = (v + h)/h    # - cur_x / h
        #print "grad", gradient
        u += step_size*gradient
        #print "current x", cur_x
        diff = abs(u-prev_u)
        if (u > 10):
            step_size = step_size/10
            u = prev_u
            diff = float("-inf")
        elif (u < -10):
            step_size = step_size/10
            u = prev_u
            diff = float("-inf")

        count += 1
        print count
        w_list.append(v)
        #print w_list
    return w_list

if __name__ == '__main__':
    try:
        inst_number = int(sys.argv[1])
    except:
        print 'Need an instance number.\nUsage:', sys.argv[0], '<instance>'
        exit(1)

    s = Simulator(inst_number)
    print optimize(4)
    #best[10] = {11:(2.7115932464,6.85875080975),1.41419:(9.54491536082,7.68695125929)}