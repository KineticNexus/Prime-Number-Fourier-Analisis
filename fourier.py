
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift
from sympy import sieve
import cv2
import os

def generate_primes(n):
    return list(sieve.primerange(2, n))

def map_to_2d(numbers, size):
    grid = np.zeros((size, size))
    for num in numbers:
        x, y = num % size, (num // size) % size
        grid[y, x] += 1
    return grid

def fourier_analysis(data):
    ft = fft2(data)
    return np.abs(fftshift(ft))

def plot_fourier_result(fourier_result, title, size):
    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(np.log(1 + fourier_result), cmap='viridis', aspect='equal')
    ax.set_title(title)
    ax.set_xlabel('Frecuencia Dimensión 1')
    ax.set_ylabel('Frecuencia Dimensión 2')
    fig.colorbar(im, ax=ax, label='Magnitud logarítmica')
    plt.tight_layout()
    plt.savefig(f'fourier_{size}.png')
    plt.close(fig)

# Parámetros
prime_counts = [10000, 100000, 1000000, 10000000]
size_range = range(100, 7600, 10)

# Generar números primos una vez para eficiencia
max_primes_needed = max(prime_counts) * 20
primes = generate_primes(max_primes_needed)

# Generar imágenes para cada tamaño de cuadrícula
for size in size_range:
    prime_grid = map_to_2d(primes[:size*20], size)
    fourier_result = fourier_analysis(prime_grid)
    plot_fourier_result(fourier_result, f'Transformada de Fourier 2D con tamaño de cuadrícula {size}', size)


# Limpiar archivos temporales
for size in size_range:
    os.remove(f'fourier_{size}.png')

print("Video creado exitosamente.")
