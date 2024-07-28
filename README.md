# Prime Number Fourier Analysis ("f3.py") file

This Python project generates visualizations of prime number distributions using different 2D mapping methods and Fourier analysis. It creates a series of frames that can be combined into videos to show how the Fourier transform of prime number distributions changes with increasing grid sizes.

## Features

f3.py
- Generates prime numbers up to a specified limit
- Maps prime numbers to 2D grids using three different methods:
  - Original: Direct mapping based on prime value
  - Normalized: Normalized mapping to distribute primes more evenly
  - Factor-based: Mapping based on the number of factors
- Performs 2D Fourier transform on the mapped distributions
- Generates frames visualizing the Fourier transform results
- Creates videos from the generated frames using FFmpeg

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SymPy
- SciPy
- FFmpeg (for video generation)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/prime-number-fourier-analysis.git
   ```
2. Install the required Python packages:
   ```
   pip install numpy matplotlib sympy scipy
   ```
3. Ensure FFmpeg is installed on your system. If not, download and install it from [ffmpeg.org](https://ffmpeg.org/).

## Usage

1. Run the script:
   ```
   python prime_fourier_analysis.py
   ```

The script will:
1. Generate prime numbers up to the specified limit
2. Create 2D mappings of the primes using different methods
3. Perform Fourier analysis on each mapping
4. Generate frames visualizing the Fourier transform results
5. Create videos from the generated frames

## How it Works

1. `generate_primes`: Generates prime numbers using SymPy's sieve.
2. Mapping functions (`map_to_2d_original`, `map_to_2d_normalized`, `map_to_2d_factor_based`): Map primes to 2D grids using different strategies.
3. `fourier_analysis`: Performs 2D Fourier transform on the mapped data.
4. `plot_fourier_result`: Creates visualizations of the Fourier transform results.
5. The main script iterates through different grid sizes, generating frames for each mapping method.
6. Finally, it uses FFmpeg to compile the frames into videos.

## Customization

You can adjust the following parameters in the script:
- `max_primes`: Maximum number to consider for prime generation
- `fps`: Frames per second for the output videos
- `start_size`, `end_size`, `step`: Control the range and step size of the grid dimensions

## Output

The script generates:
- Individual frames in the `frames/` directory
- Three video files (one for each mapping method) named `prime_fourier_analysis_{method}.mp4`


## Fourier Analysis of Prime Number Distribution ("fourier.py") file

This Python project generates visualizations of the 2D Fourier transform of prime number distributions mapped onto grids of various sizes. It provides insights into the patterns and structures within prime number distributions.
Features

Generates prime numbers up to a specified limit
Maps prime numbers to 2D grids
Performs 2D Fourier transform on the mapped distributions
Generates visualizations of the Fourier transform results for different grid sizes
Creates images for each grid size

## Requirements

Python 3.x
NumPy
Matplotlib
SciPy
SymPy
OpenCV (cv2)

## Installation

Clone this repository:
Copygit clone https://github.com/yourusername/fourier-prime-analysis.git

Install the required Python packages:
Copypip install numpy matplotlib scipy sympy opencv-python


## Usage
Run the script using Python:
Copypython fourier.py
The script will:

Generate prime numbers up to the maximum needed count
Create 2D mappings of the primes for various grid sizes
Perform Fourier analysis on each mapping
Generate and save visualizations for each grid size
Clean up temporary files after processing

## How it Works

generate_primes: Uses SymPy's sieve to generate prime numbers efficiently.
map_to_2d: Maps prime numbers to a 2D grid.
fourier_analysis: Performs 2D Fourier transform on the mapped data.
plot_fourier_result: Creates and saves visualizations of the Fourier transform results.

The main script iterates through different grid sizes, generating a Fourier transform visualization for each.
Customization
You can adjust the following parameters in the script:

prime_counts: List of prime number counts to analyze
size_range: Range of grid sizes to use for mapping
max_primes_needed: Maximum number of primes to generate (adjust based on your needs)

## Output

I found interesting patterns on primes that do not appear when analyzing a random distribution. Likley to the buckets that the // bucketing brings.

The script generates:

Temporary PNG images for each grid size (these are deleted after processing)
![fourier_820](https://github.com/user-attachments/assets/a10e79d9-0f8b-487a-9cf2-864a99415852)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
