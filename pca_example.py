import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create a PCA instance with 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Print the explained variance ratio
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total explained variance: {sum(pca.explained_variance_ratio_):.2f}")

# Plot the results
plt.figure(figsize=(10, 7))
colors = ['navy', 'turquoise', 'darkorange']
targets = ['Setosa', 'Versicolor', 'Virginica']

for color, target, i in zip(colors, targets, [0, 1, 2]):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], color=color, alpha=0.8, lw=2, label=target)
    
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA of Iris Dataset')
plt.legend(loc='best')
plt.grid(True)

# Show component contribution
plt.figure(figsize=(10, 7))
features = iris.feature_names
components = pca.components_
plt.matshow(components, cmap='viridis')
plt.xticks(range(len(features)), features, rotation=60)
plt.yticks([0, 1], ['First component', 'Second component'])
plt.colorbar()
plt.title('Feature weights in PCA components')

plt.tight_layout()
plt.show() 