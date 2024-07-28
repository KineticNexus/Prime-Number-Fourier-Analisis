# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:21:02 2024

@author: halif
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import sieve
from scipy.fft import fft2, fftshift
import time
import os
import subprocess
import gc

def generate_primes(n):
    return list(sieve.primerange(2, n))

def map_to_2d_original(numbers, size):
    grid = np.zeros((size, size), dtype=np.float32)
    for num in numbers:
        x, y = num % size, (num // size) % size
        grid[y, x] += 1
    return grid

def map_to_2d_normalized(numbers, size):
    grid = np.zeros((size, size), dtype=np.float32)
    for num in numbers:
        x = (num % size) / size
        y = ((num // size) % size) / size
        grid[int(y * size), int(x * size)] += 1
    return grid

def map_to_2d_factor_based(numbers, size):
    grid = np.zeros((size, size), dtype=np.float32)
    for num in numbers:
        x = num % size
        y = sum(int(num % p == 0) for p in range(2, min(num, size))) % size
        grid[y, x] += 1
    return grid

def fourier_analysis(data):
    ft = fft2(data)
    return np.abs(fftshift(ft))

def plot_fourier_result(fourier_result, title, size, frame_number, mapping_method):
    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(np.log(1 + fourier_result), cmap='viridis', aspect='equal')
    ax.set_title(f'{title}\nTamaño de cuadrícula: {size}x{size}\nMétodo: {mapping_method}')
    ax.set_xlabel('Frecuencia Dimensión 1')
    ax.set_ylabel('Frecuencia Dimensión 2')
    plt.colorbar(im, ax=ax, label='Magnitud logarítmica')
    plt.savefig(f'frames/frame_{mapping_method}_{frame_number:04d}.png')
    plt.close(fig)

# Configuration
max_primes = 1000000
fps = 5
start_size = 50
end_size = 7500
step = 5

# Create directory for frames
if not os.path.exists('frames'):
    os.makedirs('frames')

# Generate primes
primes = generate_primes(max_primes)

# Mapping methods
mapping_methods = {
    'original': map_to_2d_original,
    'normalized': map_to_2d_normalized,
    'factor_based': map_to_2d_factor_based
}

# Generate frames
print("Generating frames...")
start_time = time.time()

for method_name, mapping_function in mapping_methods.items():
    frame_number = 0
    for size in range(start_size, end_size + 1, step):
        try:
            prime_grid = mapping_function(primes, size)
            fourier_result = fourier_analysis(prime_grid)
            plot_fourier_result(fourier_result, 'Transformada de Fourier 2D de números primos', 
                                size, frame_number, method_name)
            frame_number += 1
            if frame_number % 10 == 0:
                print(f"Generated frame {frame_number} for {method_name} mapping")
        except Exception as e:
            print(f"Error in size {size} for {method_name} mapping: {str(e)}")
        finally:
            gc.collect()

end_time = time.time()
print(f"Frames generated. Total time: {end_time - start_time:.2f} seconds")

# Create videos with FFmpeg
print("Creating videos...")
for method_name in mapping_methods.keys():
    ffmpeg_command = f"ffmpeg -framerate {fps} -i frames/frame_{method_name}_%04d.png -c:v libx264 -pix_fmt yuv420p prime_fourier_analysis_{method_name}.mp4"
    subprocess.run(ffmpeg_command, shell=True, check=True)
    print(f"Video generated: prime_fourier_analysis_{method_name}.mp4")

print("All videos generated.")