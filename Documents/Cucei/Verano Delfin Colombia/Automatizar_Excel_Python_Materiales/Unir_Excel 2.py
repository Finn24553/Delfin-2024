# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:51:17 2024

@author: Alan
"""

import os
import pandas as pd
import numpy as np

def load_data_from_folders(base_folder):
    X = []
    y = []

    for label_folder in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, label_folder)
        
        for label2_folder in os.listdir(folder_path):
            folder2_path = os.path.join(folder_path, label2_folder)
        
            if os.path.isdir(folder2_path):
                for csv_file in os.listdir(folder2_path):
                    if csv_file.endswith('.csv'):
                        file_path = os.path.join(folder2_path, csv_file)
                        data = pd.read_csv(file_path)
                        # Suponemos que las columnas son 'Tiempo' y 'Amplitud'
                        if data.shape[1] == 2:
                            X.append(data.values)
                            y.append(label_folder)

    X = np.array(X)
    y = np.array(y)
    
    return X, y

base_folder = r'C:\Users\Alan\Documents\Cucei\Verano Delfin Colombia\Mediciones\Datos Centro\Frente'
X, y = load_data_from_folders(base_folder)
print(X.shape)  # Debe imprimir (n_samples, 5132, 2)
print(y.shape)  # Debe imprimir (n_samples,)