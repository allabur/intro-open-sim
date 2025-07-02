import numpy as np
import itertools
import simpy


def arrivals_generator(env, operators):

    # create the arrival process rng
    arrival_rng = np.random.default_rng()

    # create the service rng that we pass to each service process created
    service_rng = np.random.default_rng()

    # with a counter variable that we can use for unique Ids
    for caller_count in itertools.count(start=1):
        inter_arrival_time = arrival_rng.exponential(60.0 / 100.0)
        yield env.timeout(inter_arrival_time)
        print(f"call arrives at: {env.now:.3f}")

        # create a new simpy process for serving this caller.
        env.process(service(caller_count, operators, env, service_rng))


# model parameters
RUN_LENGTH = 100
N_OPERATORS = 13

# create simpy environment and operator resources
env = simpy.Environment()
operators = simpy.Resource(env, capacity=N_OPERATORS)

env.process(arrivals_generator(env, operators))
env.run(until=RUN_LENGTH)
print(f"end of run. simulation clock time = {env.now}")
