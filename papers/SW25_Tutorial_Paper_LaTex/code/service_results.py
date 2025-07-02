def trace(msg):
    """Wrap print function to toggle simulation printed output on/off"""
    if TRACE:
        print(msg)


def service(identifier, operators, env, service_rng):
    """Simulates the service process for a call operator"""
    # record the time that call entered the queue
    start_wait = env.now

    # request an operator
    with operators.request() as req:
        yield req

        # record the waiting time for call to be answered
        waiting_time = env.now - start_wait
        results["waiting_times"].append(waiting_time)

        trace(f"operator answered call {identifier} at " + f"{env.now:.3f}")

        call_duration = service_rng.triangular(left=5.0, mode=7.0, right=10.0)
        yield env.timeout(call_duration)

        trace(
            f"call {identifier} ended {env.now:.3f}; "
            + f"waiting time was {waiting_time:.3f}"
        )
