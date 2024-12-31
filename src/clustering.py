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

def main():
  """
  A simple command-line interface to run K-Means on a CSV file of scaled data.
  This is optional; you can remove or modify if you prefer to call run_kmeans from a notebook.
  """
  parser = argparse.ArgumentParser(description="Run K-Means clustering on scaled CSV data.")
  parser.add_argument("--csv", type=str, required=True,
                      help="Path to the CSV file containing scaled data (numeric features only).")
  parser.add_argument("--k", type=int, default=3,
                      help="Number of clusters (default=3).")
  parser.add_argument("--save", type=str, default="",
                      help="Path to save the trained model (optional).")

  args = parser.parse_args()
  data_path = args.csv
  k = args.k
  save_path = args.save

  # 1) Load scaled data from CSV
  X_scaled = pd.read_csv(data_path).values  # all columns are numeric

  # 2) Run K-Means
  kmeans_model, labels, sse, sil = run_kmeans(X_scaled, n_clusters=k)

  print(f"K-Means finished with k={k}")
  print(f"SSE (Inertia) = {sse:.2f}")
  print(f"Silhouette Score = {sil:.3f}")

  # 3) Optionally save model
  if save_path:
      save_model(kmeans_model, save_path)

if __name__ == "__main__":
  main()
