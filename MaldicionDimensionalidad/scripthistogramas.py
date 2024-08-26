import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the file paths
file_paths = [
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect10.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect50.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect100.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect500.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect1000.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect2000.txt",
    "/Users/williambarrios/Documents/EDA/MaldicionDimensionalidad/MaldicionDimensionalidad/distances_vect5000.txt"
]

# Function to read data from file and plot histogram
def plot_histogram(file_path):
    # Read the data from the file into a Pandas DataFrame
    data = pd.read_csv(file_path, header=None, names=['Distance'])
    
    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data['Distance'], bins='auto', edgecolor='black')
    
    # Set the title and labels
    plt.title(f'Histogram of Distances - {os.path.basename(file_path)}')
    plt.xlabel('Distance')
    plt.ylabel('Frequency')
    
    # Ensure X-axis starts at 0
    plt.xlim(left=0)
    
    # Show the plot
    plt.show()

# Generate histograms for each file
for file_path in file_paths:
    plot_histogram(file_path)
