import pandas as pd
import matplotlib.pyplot as plt
import os


file_paths = [
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect10.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect50.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect100.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect500.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect1000.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect2000.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect5000.txt"
]


def plot_histogram(file_path):
    
    data = pd.read_csv(file_path, header=None, names=['Distance'])
    plt.figure(figsize=(10, 6))
    plt.hist(data['Distance'], bins='auto', edgecolor='black')
    plt.title(f'Histogram of Distances - {os.path.basename(file_path)}')
    plt.xlabel('Distance')
    plt.ylabel('Frequency')
    plt.xlim(left=0)
    plt.show()


for file_path in file_paths:
    plot_histogram(file_path)
