import numpy as np
import matplotlib.pyplot as plt

def create_complex_grid(x_min, x_max, y_min, y_max, width, height):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    return X + 1j * Y

def mandelbrot_set(c, n_max, threshold):
    z = 0
    for _ in range(n_max):
        z = z**2 + c
        if abs(z) > threshold:
            return False
    return True

def generate_mandelbrot_mask(x_min, x_max, y_min, y_max, width, height, n_max, threshold):
    c_grid = create_complex_grid(x_min, x_max, y_min, y_max, width, height)
    mask = np.zeros(c_grid.shape, dtype=bool)

    for i in range(height):
        for j in range(width):
            c = c_grid[i, j]
            if mandelbrot_set(c, n_max, threshold):
                mask[i, j] = True
            else:
                mask[i, j] = False

    return mask


def plot_mandelbrot(mask, x_min, x_max, y_min, y_max):
    plt.figure(figsize=(10, 10))
    plt.imshow(mask.T, extent=[x_min, x_max, y_min, y_max], cmap='gray')
    plt.title("Mandelbrot Set")
    plt.xlabel("Real part")
    plt.ylabel("Imaginary part")
    plt.savefig('mandelbrot.png')
    plt.show()

def main():
    n_max = 50
    threshold = 50
    x_min, x_max = -2, 1
    y_min, y_max = -1.5, 1.5
    width, height = 800, 800
    mask = generate_mandelbrot_mask(x_min, x_max, y_min, y_max, width, height, n_max, threshold)
    plot_mandelbrot(mask, x_min, x_max, y_min, y_max)

if __name__ == "__main__":
    main()
