import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset (replace 'dataset.csv' with your actual dataset file)
data = pd.read_csv('dataset.csv')


# Perform descriptive analysis
# Summary statistics
summary_stats = data.describe()
print(summary_stats)

# Visualize key behavioral metrics
plt.figure(figsize=(10, 6))
plt.hist(data['session_duration_minutes'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Session Durations')
plt.xlabel('Session Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Select features for clustering
features = data[['total_play_time', 'num_skips', 'avg_session_duration']]

# Normalize features
normalized_features = (features - features.mean()) / features.std()

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(normalized_features)

# Add cluster labels to the dataset
data['cluster'] = clusters

# Visualize clustering results
plt.figure(figsize=(10, 6))
plt.scatter(data['total_play_time'], data['avg_session_duration'], c=data['cluster'], cmap='viridis', alpha=0.5)
plt.title('Clustering of User Behavior')
plt.xlabel('Total Play Time (minutes)')
plt.ylabel('Average Session Duration (minutes)')
plt.show()

