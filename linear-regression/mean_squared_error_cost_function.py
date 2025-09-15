import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D 


# Input (features)
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Output (target)
y = [52, 57, 62, 65, 68, 73, 78, 82, 88, 94]

# Model
b = 48
w = 4.1

def get_y_hat(x_i,w,b):
    return x_i*w+b

def get_error_y_hat(x_i, y_i,w,b):
    y_hat = get_y_hat(x_i, w,b)
    return (y_hat - y_i)**2

def get_mean_squared_error(x,y,w = w,b = b):
    total_error = 0 
    for i in x:
        total_error += get_error_y_hat(x[i-1],y[i-1],w,b)
    
    return total_error/(2*len(x))

def plot_model():
    y_hat = [get_y_hat(x_i, w, b) for x_i in X]

    plt.figure()
    plt.scatter(X, y, color='blue', label='Target Data Points')
    plt.plot(X, y_hat, color='red', label='Model Predictions') 

    plt.xlabel("X (Features)")
    plt.ylabel("y (Target)")
    plt.title("Model Predictions vs Target Data")
    plt.legend()

    plt.show()


def plot_2D():
    b_options = [47,48,49,50,51,52,53,54]
    w_options = [3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4]

    b_options_mse = list(map(lambda b: get_mean_squared_error(X,y, b=b), b_options))
    print("For b options error is:")

    for e in b_options_mse:
       print(e)
   
    w_options_mse = list(map(lambda w: get_mean_squared_error(X,y, w=w), w_options))
    print("For w options error is:")
    for e in w_options_mse:
       print(e)

     # Plot para w_options
    plt.figure()  
    plt.plot(w_options, w_options_mse)
    plt.xlabel("w values")
    plt.ylabel("Mean Squared Error")
    plt.title("MSE vs w")
    plt.show(block=False)

    # Plot para b_options
    plt.figure()  
    plt.plot(b_options, b_options_mse)
    plt.xlabel("b values")
    plt.ylabel("Mean Squared Error")
    plt.title("MSE vs b")
    plt.show(block=False)

    input("Press Enter to close all plots...")
    plt.close('all')



    print(f"Manually optimized error is: {get_mean_squared_error(X,y)}")

def plot_3D():
    # b_options = [50,51,52,53,54,55,56]
    b_options = [46,47,48, 49, 50,51,52,53,54,55,56]
    w_options = [3.2,3.3,3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 4.2]

    B, W = np.meshgrid(b_options, w_options)

    MSE = np.array([[get_mean_squared_error(X, y, w=w, b=b) for b in b_options] for w in w_options])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(B, W, MSE, cmap='viridis', edgecolor='k')

    ax.set_xlabel("b values")
    ax.set_ylabel("w values")
    ax.set_zlabel("Mean Squared Error")
    ax.set_title("3D Surface Plot of MSE")

    plt.show()


def main():
    # plot_2D()
    # plot_3D()
    plot_model()

main()