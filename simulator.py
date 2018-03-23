#!usr/bin/env python
import os
import subprocess
import commands
import sys
import random
import numpy as np


class Simulator:
    def __init__(self, inst_number):
        self.num = inst_number
    

    def evaluate(self, w):
        fileToRun = "./simulator-linux waypoints "+ str(self.num)
        # getting path cost to orginal set of way points
        (stat, output ) = commands.getstatusoutput( fileToRun )
        path_cost =  output.split(' ')
        path_cost = float(path_cost[-1][:-2])

        prev_ans = 0
        #self.descent()
        for u,v in w_list:
        #     for i in range(-10,10):
        #         u = u+1
        #         for j in range(-10,10):
        #             v = v+1
        #             if v > 10:
        #                 v = -10
            new_way_point = str('\n') + str(u) + " " + str(v) + str('\n') + str(10) + " "+ str(10)

            with file('waypoints', 'r') as original: data = original.read()
            
            write_to_file = open('waypoints', 'w')
            write_to_file.write(data[:-6])

            write_to_file = open('waypoints', 'a')
            write_to_file.write(new_way_point)
            write_to_file.close()

            # getting path cost after addding new way point
            (stat, output ) = commands.getstatusoutput( fileToRun )

            # if( stat == 0 ):
            #     print "Command succeeded, here is the output: %s" % output
            # else:
            #     print "Command failed, here is the output: %s" % output

            ans  = output.split(' ')
            ans = float(ans[-1][:-2])
            new_ans = ans + prev_ans
            prev_ans = new_ans
            # check new path cost is less than the orginal
            if new_ans < path_cost:
                path_cost = new_ans
                with open("better_waypoints.txt", "w") as bet:
                    with file('waypoints', 'r') as original: better_way_point = original.read()
                    bet.write(better_way_point) 
        return path_cost

    def descent(self):
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

    random1 = random.uniform(-10, 10)
    random2 = random.uniform(-10,10) 
    w = [(random1, random2)]

    s = Simulator(inst_number)
    s.descent()
    print s.evaluate(w_list)
