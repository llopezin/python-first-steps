import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D 

# Dataset 1: Very noisy, random data - creates steep "bowl of soup" surface
X1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [15, 3, 22, 8, 1, 18, 7, 25, 12, 5]  # Very random, no clear pattern

# Dataset 2: Perfect linear relationship - creates flat surface
X2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Perfect linear: y = 2x

# Model parameters for comparison
w1, b1 = 0.5, 2    # Poor parameters for dataset 1 (far from optimal)
w2, b2 = 2, 0      # Perfect parameters for dataset 2

def get_y_hat(x_i, w, b):
    return x_i * w + b

def get_error_y_hat(x_i, y_i, w, b):
    y_hat = get_y_hat(x_i, w, b)
    return (y_hat - y_i)**2

def get_mean_squared_error(x, y, w, b):
    total_error = 0 
    for i in range(len(x)):
        total_error += get_error_y_hat(x[i], y[i], w, b)
    
    return total_error / (2 * len(x))

def plot_linear(ax, X, y, w, b, title_suffix=""):
    # Generate predictions using the model
    y_hat = [get_y_hat(x_i, w, b) for x_i in X]
    
    # Calculate current MSE
    current_mse = get_mean_squared_error(X, y, w, b)
    
    # Plot the target data points and model predictions
    ax.scatter(X, y, color='blue', label='Target Data Points', s=60)
    ax.plot(X, y_hat, color='red', label='Model Predictions', linewidth=2)
    
    # Add labels and legend
    ax.set_xlabel("X (Features)")
    ax.set_ylabel("y (Target)")
    ax.set_title(f"Model Predictions vs Target Data{title_suffix}\nMSE: {current_mse:.2f}")
    ax.legend()
    ax.grid(True, alpha=0.3)

def plot_3d_surface(ax, fig, X, y, w, b, w_range, b_range, title_suffix=""):
    # Calculate current MSE
    current_mse = get_mean_squared_error(X, y, w, b)
    
    # Create meshgrid
    W, B = np.meshgrid(w_range, b_range)
    
    # Calculate MSE for each w,b pair
    Z = np.zeros_like(W)
    for i in range(len(w_range)):
        for j in range(len(b_range)):
            Z[j, i] = get_mean_squared_error(X, y, w=w_range[i], b=b_range[j])
    
    # Plot the surface
    surf = ax.plot_surface(W, B, Z, cmap=cm.viridis, alpha=0.8, linewidth=0)
    
    # Mark the current model parameters
    ax.scatter([w], [b], [current_mse], color='red', s=100, marker='o')
    
    # Add labels
    ax.set_xlabel('w (Weight)')
    ax.set_ylabel('b (Bias)')
    ax.set_zlabel('Mean Squared Error')
    ax.set_title(f'3D MSE Surface{title_suffix}\nCurrent MSE: {current_mse:.2f}')
    
    # Add colorbar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

def plot_contour(ax, fig, X, y, w, b, w_range, b_range, title_suffix=""):
    # Calculate current MSE
    current_mse = get_mean_squared_error(X, y, w, b)
    
    # Create meshgrid
    W, B = np.meshgrid(w_range, b_range)
    
    # Calculate MSE for each w,b pair
    Z = np.zeros_like(W)
    for i in range(len(w_range)):
        for j in range(len(b_range)):
            Z[j, i] = get_mean_squared_error(X, y, w=w_range[i], b=b_range[j])
    
    # Create contour plot
    contour = ax.contourf(W, B, Z, 50, cmap=cm.viridis)
    ax.contour(W, B, Z, 10, colors='k', linewidths=0.5, alpha=0.3)
    
    # Mark the current model parameters
    ax.scatter([w], [b], color='red', s=100, marker='o')
    
    # Add labels
    ax.set_xlabel('w (Weight)')
    ax.set_ylabel('b (Bias)')
    ax.set_title(f'MSE Contour Plot{title_suffix}\nCurrent MSE: {current_mse:.2f}')
    
    # Add colorbar
    fig.colorbar(contour, ax=ax, shrink=0.5, aspect=5)

def plot_steep_bowl():
    """Plot visualizations for noisy data that creates a steep bowl-shaped surface"""
    # Define range for w and b - much broader range to show the steep sides
    w_range = np.linspace(-3, 6, 50)
    b_range = np.linspace(-10, 25, 50)
    
    # Set up the figure with 3 subplots
    fig = plt.figure(figsize=(18, 6))
    fig.suptitle('Steep "Bowl of Soup" Surface - Very Noisy Data', fontsize=16, fontweight='bold')
    
    # 1. Linear plot with data points and model predictions
    ax1 = fig.add_subplot(131)
    plot_linear(ax1, X1, y1, w1, b1, " (Very Noisy)")
    
    # 2. 3D Surface plot of MSE
    ax2 = fig.add_subplot(132, projection='3d')
    plot_3d_surface(ax2, fig, X1, y1, w1, b1, w_range, b_range, " (Steep Bowl)")
    
    # 3. Contour plot of MSE
    ax3 = fig.add_subplot(133)
    plot_contour(ax3, fig, X1, y1, w1, b1, w_range, b_range, " (Steep Bowl)")
    
    plt.tight_layout()
    plt.show()

def plot_flat_surface():
    """Plot visualizations for perfect linear data that creates a flat surface"""
    # Define range for w and b - focused around the optimal values
    w_range = np.linspace(1.5, 2.5, 50)
    b_range = np.linspace(-2, 2, 50)
    
    # Set up the figure with 3 subplots
    fig = plt.figure(figsize=(18, 6))
    fig.suptitle('Flat Surface - Perfect Linear Data', fontsize=16, fontweight='bold')
    
    # 1. Linear plot with data points and model predictions
    ax1 = fig.add_subplot(131)
    plot_linear(ax1, X2, y2, w2, b2, " (Perfect)")
    
    # 2. 3D Surface plot of MSE
    ax2 = fig.add_subplot(132, projection='3d')
    plot_3d_surface(ax2, fig, X2, y2, w2, b2, w_range, b_range, " (Flat)")
    
    # 3. Contour plot of MSE
    ax3 = fig.add_subplot(133)
    plot_contour(ax3, fig, X2, y2, w2, b2, w_range, b_range, " (Flat)")
    
    plt.tight_layout()
    plt.show()

def plot_comparison():
    """Plot side-by-side comparison of both scenarios"""
    # Set up the figure with 6 subplots (2 rows, 3 columns)
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle('Comparison: Steep Bowl vs Flat Surface', fontsize=16, fontweight='bold')
    
    # Top row: Steep bowl (noisy data)
    w_range_steep = np.linspace(-3, 6, 30)
    b_range_steep = np.linspace(-10, 25, 30)
    
    ax1 = fig.add_subplot(231)
    plot_linear(ax1, X1, y1, w1, b1, " - Noisy Data")
    
    ax2 = fig.add_subplot(232, projection='3d')
    plot_3d_surface(ax2, fig, X1, y1, w1, b1, w_range_steep, b_range_steep, " - Steep Bowl")
    
    ax3 = fig.add_subplot(233)
    plot_contour(ax3, fig, X1, y1, w1, b1, w_range_steep, b_range_steep, " - Steep Bowl")
    
    # Bottom row: Flat surface (perfect data)
    w_range_flat = np.linspace(1.5, 2.5, 30)
    b_range_flat = np.linspace(-2, 2, 30)
    
    ax4 = fig.add_subplot(234)
    plot_linear(ax4, X2, y2, w2, b2, " - Perfect Data")
    
    ax5 = fig.add_subplot(235, projection='3d')
    plot_3d_surface(ax5, fig, X2, y2, w2, b2, w_range_flat, b_range_flat, " - Flat Surface")
    
    ax6 = fig.add_subplot(236)
    plot_contour(ax6, fig, X2, y2, w2, b2, w_range_flat, b_range_flat, " - Flat Surface")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Generating visualizations...")
    print("\n1. Steep 'Bowl of Soup' Surface (Noisy Data):")
    plot_steep_bowl()
    
    print("\n2. Flat Surface (Perfect Linear Data):")
    plot_flat_surface()
    
    print("\n3. Side-by-side Comparison:")
    plot_comparison()