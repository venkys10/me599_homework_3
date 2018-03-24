#!/usr/bin/env python

# Bill Smart
# Homework 2 example solution


from subprocess import check_output
from uuid import uuid4
from os import remove
from random import uniform
import sys


class Simulator:
    def __init__(self, instance, executable='./simulator-mac'):
        # Get a unique name for the waypoints file, so that we can run multiple instances of the simulator, if we want to.
        self.waypoints_file = './waypoints-' + str(uuid4())
        self.command = '{0} {1} {2}'.format(executable, self.waypoints_file, instance).split()

    def write_waypoints(self, waypoints):
        with open(self.waypoints_file, 'w') as f:
            for w in waypoints:
                f.write('{0} {1}\n'.format(*w))

    def evaluate(self, waypoints):
        # Write out the waypoints file
        self.write_waypoints(waypoints)

        # Execute the simulator and grab the output
        output = check_output(self.command).split()

        # Get rid of the waypoints file
        remove(self.waypoints_file)

        # Harvest the output.  Make sure we processed the correct number of waypoints, and deal
        # with the . at the end of the cost.
        number = int(output[1])
        cost = float(output[-1][:-1])

        if number != len(waypoints):
            raise ValueError

        return cost


if __name__ == '__main__':
    try:
        instance = int(sys.argv[1])
    except:
        print 'Need an instance number.\nUsage:', sys.argv[0], '<instance>'
        exit(1)

    s = Simulator(instance)
    baseline_cost = s.evaluate([(-10, -10), (10, 10)])

    waypoints = [(-10, -10), (0, 0), (10, 10)]

    best_cost = baseline_cost
    best_waypoints = waypoints[:]

    # Loop for a while, to see if we can come up with a lower cost path
    TRIES = 1000
    for i in xrange(TRIES):
        waypoints[1] = (uniform(-10, 10), uniform(-10, 10))
        cost = s.evaluate(waypoints)

        if cost < best_cost:
            best_cost = cost
            best_waypoints = waypoints[:]

            # For this homework, we just need to find a single lower cost path.
            break

    print 'Baseline cost:', baseline_cost
    if best_cost < baseline_cost:
        print 'Lower cost: {0}\n  {1}'.format(best_cost, best_waypoints)
    else:
        print 'Could not find lower cost path after', TRIES, 'attempts.'
