import matplotlib.pyplot as plt

# Sample training data
study_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # hours studied
scores     = [50, 55, 60, 68, 72, 78, 82, 85, 88, 93]  # exam score (%)

# Plotting
plt.figure(figsize=(6, 4))
plt.scatter(study_time, scores, s=50)
plt.xlabel('Study Time (hours)')
plt.ylabel('Score (%)')
plt.title('Relationship Between Study Time and Score')
plt.grid(True)
plt.show()
