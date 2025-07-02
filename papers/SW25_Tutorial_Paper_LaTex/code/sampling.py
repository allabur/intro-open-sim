import numpy as np

rng = np.random.default_rng(42) # define arrivals PRNG
samples = rng.uniform(low=10, high=40, size=1_000_000)
