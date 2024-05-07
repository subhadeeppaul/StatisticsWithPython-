import numpy as np
import time

# Start timing
start_time = time.time()

# Generate the data and calculate means
data = [np.mean(np.random.rand(500)) for _ in range(10**6)]

# Calculate the quantiles
quantile_1 = np.quantile(data, 0.01)
quantile_99 = np.quantile(data, 0.99)

# Print the result
print("98% of the means lie in the estimated range: ",
      (quantile_1, quantile_99))

# End timing
end_time = time.time()

# Print timing information
print("{:.6f} seconds ({} M allocations: {:.3f} GiB, {:.2f}% gc time)".format(
    end_time - start_time,
    10**6,
    np.array(data).nbytes / 1024**3,
    0.0  # Assuming Python does not perform garbage collection during this small operation
))
