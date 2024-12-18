%pip install seaborn
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('heart.csv')

# Step 1: Select relevant features for analysis
selected_features = ['age', 'trestbps', 'chol', 'target']
selected_data = data[selected_features]

# Step 2: Descriptive Statistics
# Save descriptive statistics to a text file
descriptive_stats = selected_data.describe()
with open('descriptive_statistics.txt', 'w') as file:
    file.write(descriptive_stats.to_string())

# Step 3: Visualizations
# Save histogram for 'chol'
plt.figure(figsize=(12, 8))
plt.hist(selected_data['chol'], bins=20, edgecolor='grey')
plt.title('Distribution of Cholesterol Levels')
plt.xlabel('Cholesterol')
plt.ylabel('Frequency')
plt.savefig('cholesterol_histogram.png')
plt.close()

# Save scatter plot: Age vs Cholesterol
plt.figure(figsize=(12, 8))
plt.scatter(selected_data['age'], selected_data['chol'], alpha=0.5)
plt.title('Age vs Cholesterol Levels')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.savefig('age_vs_cholesterol_scatter.png')
plt.close()

# Step 4: Correlation Matrix
plt.figure(figsize=(8, 6))
correlation_matrix = selected_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".0f")
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.close()

# Step 5: Save Selected Data
selected_data.to_csv('selected_heart_disease_data.csv', index=False)

# End of script
print("Analysis completed. Files saved:")
print("- descriptive_statistics.txt")
print("- cholesterol_histogram.png")
print("- age_vs_cholesterol_scatter.png")
print("- correlation_matrix.png")
print("- selected_heart_disease_data.csv")
