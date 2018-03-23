#!/usr/bin/env python


from random import uniform


def optimize(simulator, record_waypoints, done):
    baseline_cost = simulator.evaluate([(-10, -10), (10, 10)])

    waypoints = [(-10, -10), (0, 0), (10, 10)]
    record_waypoints(waypoints)

    best_cost = baseline_cost
    best_waypoints = waypoints[:]

    # Put this while statement in here to play nice with the grading software
    while not done():
        waypoints[1] = (uniform(-10, 10), uniform(-10, 10))
        cost = simulator.evaluate(waypoints)

        if cost < best_cost:
            best_cost = cost
            best_waypoints = waypoints[:]

            # If it's better, then report it to the grading system
            record_waypoints(best_waypoints)
