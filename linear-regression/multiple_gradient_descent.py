import numpy as np

# Size(ft) Bedrooms	Floors	Age 
# 2104	   5	    1	    45	
# 1416	   3	    2	    40	
# 852 	   2	    1	    35	


# Input (features)
X = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])

# Output (target)
y = np.array([460, 232, 178])

# Model
b = 0
w = 0
alpha = .001
max_iterations = 100000


y_i_prediction = lambda x_i, w = w, b = b: w*x_i+b

# Cost function
def calculate_error(X = X, y = y, b = b, w = w):
    error = 0
    
    for i in range(len(X)):
        error = error + (y_i_prediction(X[i], w = w, b = b) - y[i])**2

    return error/(2*len(X))

# Aquí calculamos la derivada (slope) de MSE sobre w
def calculate_dw(X = X, y = y, b = b, w = w):
    y_i_prediction = lambda x_i: w*x_i+b
    error = 0
    
    for i in range(len(X)):
        error = error + (y_i_prediction(X[i]) - y[i]) * X[i]

    return error/len(X)

# Aquí calculamos la derivada (slope) de MSE sobre b
def calculate_db(X = X, y = y, b = b, w = w):
    y_i_prediction = lambda x_i: w*x_i+b
    error = 0
    
    for i in range(len(X)):
        error = error + (y_i_prediction(X[i]) - y[i])

    return error/len(X)


def gradient_descent(X = X, y = y, b = b, w = w, alpha = alpha, iterations = max_iterations):
    current_w = w
    current_b = b

    for _ in range(max_iterations):
          error = calculate_error(X = X, y = y, b = current_b, w = current_w)
          new_w = current_w - alpha * calculate_dw(X = X, y = y, b = current_b, w = current_w)
          new_b = current_b - alpha * calculate_db(X = X, y = y, b = current_b, w = current_w)
          new_error = calculate_error(X = X, y = y, b = new_b, w = new_w)

          if new_error >= error:
              print(f"new error {new_error}")
              return new_w, new_b            
          
          else: current_w, current_b = new_w, new_b
        
    return current_w, current_b


model = gradient_descent()
model_w, model_b = model
print(f"My model: {model}")
print(f"My model error: {calculate_error( w = model_w, b = model_b )}")


    
