import h5py
import numpy as np
import re

def extract_weights(h5file_path):
    with h5py.File(h5file_path, 'r') as h5file:
        print(f"Opening file: {h5file_path}\n")
        
        # Function to explore datasets for weights
        def explore_weights(name, obj):
            if isinstance(obj, h5py.Dataset):  # Ensure we're working with a dataset
                data = obj[()]
                if isinstance(data, np.ndarray):  # Check if data is an array
                    if data.dtype == np.float32 or data.dtype == np.float64:
                        # Try interpreting as ASCII
                        data_int = np.round(data).astype(int)
                        ascii_data = data_int[(data_int >= 32) & (data_int <= 126)]
                        message = ''.join([chr(c) for c in ascii_data])
                        if message:
                            print(f"Dataset: {name}")
                            print("Extracted Message:")
                            print(message)
                            # Look for potential flags
                            flags = re.findall(r'flag\{.*?\}|FLAG\{.*?\}', message)
                            if flags:
                                for flag in flags:
                                    print(f"Flag Found in dataset {name}: {flag}")
                    elif data.dtype == np.uint8:  # Interpret as bytes
                        message = data.tobytes().decode('utf-8', errors='ignore')
                        if message:
                            print(f"Dataset: {name}")
                            print("Extracted Message:")
                            print(message)
                            # Look for potential flags
                            flags = re.findall(r'flag\{.*?\}|FLAG\{.*?\}', message)
                            if flags:
                                for flag in flags:
                                    print(f"Flag Found in dataset {name}: {flag}")

        # Visit all items in the HDF5 file
        h5file.visititems(explore_weights)

# Specify the path to the .h5 file
h5file_path = 'DeepFake_Detector_Sherpa.h5'
extract_weights(h5file_path)
