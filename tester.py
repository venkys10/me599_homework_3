#!/usr/bin/env python


from simulator import Simulator
from optimizer import optimize
from threading import Thread, Lock
from time import sleep


best_waypoints = [(-10, 10), (10, 10)]
is_done = False
waypoint_lock = Lock()


def record_waypoints(waypoints):
    global best_waypoints
    global waypoint_lock

    with waypoint_lock:
        best_waypoints = waypoints[:]


def done():
    with waypoint_lock:
        return is_done


if __name__ == '__main__':
    s = Simulator(10)

    baseline_cost = s.evaluate([(-10, -10), (10, 10)])

    t = Thread(target=optimize, args = (s, record_waypoints, done))
    t.start()

    # Give the other code some time to work.  We will almost certainly give you more than 1 second.
    sleep(1)
    with waypoint_lock:
        best_guess = best_waypoints[:]
        is_done = True

    print 'Baseline cost:', baseline_cost

    t = Simulator(10)
    print 'Lowest cost found:', t.evaluate(best_guess)

    with open('best-waypoints', 'w') as f:
        for w in best_guess:
            f.write('{0} {1}\n'.format(*w))
