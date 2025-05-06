import matplotlib.pyplot as plt

# === Simple training data ===
# Feature 1: Blood Urea Nitrogen (mg/dL)
bun = [15, 45, 30, 60, 22, 50, 18, 55, 25, 65]

# Feature 2: Serum Creatinine (mg/dL)
creatinine = [1.0, 2.5, 1.4, 3.0, 1.2, 2.8, 0.9, 3.2, 1.1, 3.5]

# (Optional) Labels: 0 = healthy, 1 = impaired
labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# Color map for labels
colors = ['blue' if lab == 0 else 'red' for lab in labels]

# === Plotting ===
plt.figure(figsize=(6, 4))
plt.scatter(bun, creatinine, c=colors, edgecolor='k', s=80)
plt.xlabel('Blood Urea Nitrogen (mg/dL)')
plt.ylabel('Serum Creatinine (mg/dL)')
plt.title('Toy Kidney Dataset')
plt.grid(True)
plt.show()
