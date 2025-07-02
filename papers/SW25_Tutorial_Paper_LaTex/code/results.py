def single_run(run_length, n_operators):
    """Perform a single replication of the simulation model and
    return the mean waiting time as a result"""
    env = simpy.Environment()
    operators = simpy.Resource(env, capacity=n_operators)

    env.process(arrivals_generator(env, operators))
    env.run(until=run_length)
    print(f"end of run. simulation clock time = {env.now}")

    # Calculate results on notebook level variables.
    mean_waiting_time = np.mean(results["waiting_times"])
    return mean_waiting_time


# script to run the model
results = {}
results["waiting_times"] = []

# toggle event logging to "off"
TRACE = False

# model parameters
RUN_LENGTH = 1000
N_OPERATORS = 13

mean_waiting_time = single_run(RUN_LENGTH, N_OPERATORS)
print("Simulation Complete")
print(f"Waiting time for call operators: {mean_waiting_time:.2f} minutes")
