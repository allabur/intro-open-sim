import numpy as np
import simpy


def arrivals_generator(env):
    """Model caller arrival process."""
    arrival_rng = np.random.default_rng()

    while True:
        inter_arrival_time = arrival_rng.exponential(60.0 / 100.0)
        yield env.timeout(inter_arrival_time)
        print(f"Call arrives at: {env.now}")


# model parameters
RUN_LENGTH = 100

# create the simpy environment object
env = simpy.Environment()

# tell simpy that the `arrival_generator` is a process to model
env.process(arrivals_generator(env))

# run the simulation model
env.run(until=RUN_LENGTH)
print(f"end of run. simulation clock time = {env.now}")
