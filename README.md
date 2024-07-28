# Prime Number Fourier Analysis

This Python project generates visualizations of prime number distributions using different 2D mapping methods and Fourier analysis. It creates a series of frames that can be combined into videos to show how the Fourier transform of prime number distributions changes with increasing grid sizes.

## Features

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
   git clone https://github.com/yourusername/prime-fourier-analysis.git
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
