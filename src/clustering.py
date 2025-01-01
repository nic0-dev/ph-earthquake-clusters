import argparse
import joblib

import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def run_kmeans(X_scaled, n_clusters=3, random_state=42):
  """
  Runs K-Means clustering on scaled data.

  Parameters
  ----------
  X_scaled : np.ndarray or pd.DataFrame
      The scaled dataset of shape (n_samples, n_features).
  n_clusters : int, optional (default=3)
      Number of clusters to form as well as the number of centroids to generate.
  random_state : int, optional (default=42)
      Determines random number generation for centroid initialization.

  Returns
  -------
  kmeans_model : KMeans
      The fitted KMeans model.
  labels : np.ndarray
      Cluster labels for each sample in X_scaled.
  sse : float
      Sum of squared distances of samples to their closest cluster center (inertia).
  sil : float
      Silhouette score for the clustering (range: -1 to 1, higher is better).
  """
  kmeans_model = KMeans(n_clusters=n_clusters, random_state=random_state)
  kmeans_model.fit(X_scaled)

  labels = kmeans_model.labels_
  sse = kmeans_model.inertia_
  sil = silhouette_score(X_scaled, labels) if n_clusters > 1 else np.nan

  return kmeans_model, labels, sse, sil

def save_model(kmeans_model, out_path):
  """
  Saves the KMeans model to disk using joblib.

  Parameters
  ----------
  kmeans_model : KMeans
      A fitted KMeans model.
  out_path : str
      File path to save the model, e.g. "../models/kmeans_model_3.pkl"
  """
  joblib.dump(kmeans_model, out_path)
  print(f"Model saved to {out_path}")

def load_model(model_path):
  """
  Loads a previously saved KMeans model from disk.

  Parameters
  ----------
  model_path : str
      Path to the joblib file containing the saved model.

  Returns
  -------
  KMeans
      The loaded KMeans model.
  """
  return joblib.load(model_path)