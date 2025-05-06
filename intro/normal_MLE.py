import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(0)

# True parameters
mu_true = 5.0
sigma_true = 2.0

# Generate synthetic data
N = 100
data = np.random.normal(loc=mu_true, scale=sigma_true, size=N)

# Maximum Likelihood Estimates for normal distribution
mu_hat = np.mean(data)
sigma_hat = np.sqrt(np.mean((data - mu_hat)**2))
# Display estimates
print(f"True μ: {mu_true:.2f}, Estimated μ̂: {mu_hat:.2f}")
print(f"True σ: {sigma_true:.2f}, Estimated σ̂: {sigma_hat:.2f}")

# Plot histogram of the data and the fitted normal PDF
x = np.linspace(data.min() - 1, data.max() + 1, 200)
pdf_est = (1 / (sigma_hat * np.sqrt(2 * np.pi))) * np.exp(-((x - mu_hat)**2) / (2 * sigma_hat**2))

plt.hist(data, bins=15, density=True, alpha=0.6)
plt.plot(x, pdf_est, linewidth=2)
plt.title("Histogram of Synthetic Data with MLE-Fitted Normal PDF")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
