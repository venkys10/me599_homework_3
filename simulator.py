#!usr/bin/env python
import os
import subprocess
import commands

class Simulator:
    def __init__(self, inst_number):
        self.num = inst_number

    def evaluate(self,w):

        fileToRun = "./simulator-linux waypoints "+ str(self.num)
        # getting path cost to orginal set of way points
        if len(w) ==2:
            (stat, output ) = commands.getstatusoutput( fileToRun )
            path_cost =  output.split(' ')
            path_cost = float(path_cost[-1][:-2])

        else:

            with open('waypoints', 'w') as f:
                for w1 in w:
                    f.write('{0} {1}\n'.format(*w1))

            
            (stat, output ) = commands.getstatusoutput( fileToRun )

            ans  = output.split(' ')
            ans = float(ans[-1][:-2])

            path_cost = ans

        return path_cost
    
    def evaluatePre(self, w):
        fileToRun = "./simulator-linux waypoints "+ str(self.num)
        # getting path cost to orginal set of way points
        (stat, output ) = commands.getstatusoutput( fileToRun )
        path_cost =  output.split(' ')
        path_cost = float(path_cost[-1][:-2])

        if len(w) !=0 :
            for u,v in w:
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

                # check new path cost is less than the orginal
                if ans < path_cost:
                    path_cost = ans
                    with open("better_waypoints.txt", "w") as bet:
                        with file('waypoints', 'r') as original: better_way_point = original.read()
                        bet.write(better_way_point) 
        return path_cost


    def record_waypoints(waypoints):
        global best_waypoints
        global waypoint_lock

        with waypoint_lock:
            best_waypoints = waypoints[:]

    def done():
        with waypoint_lock:
            return is_done


if __name__ == '__main__':
    try:
        inst_number = int(sys.argv[1])
    except:
        print 'Need an instance number.\nUsage:', sys.argv[0], '<instance>'
        exit(1)

	w = [(-10, 10), (0, 2), (5,6), (10, 10)]
	s = Simulator(inst_number)
	print s.evaluate(w)
