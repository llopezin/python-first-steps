import numpy as np

# Size(ft) Bedrooms	Floors	Age
# 2104	   5	    1	    45	
# 1416	   3	    2	    40	
# 852 	   2	    1	    35	


# Input (features)
X = np.array([
    [2.104, 5, 1, 4.5],
    [1.416, 3, 2, 4.0],
    [0.852, 2, 1, 3.5],
])

# Output (target)
y = np.array([460, 232, 178])

# Model
b = 0
w = np.array([0.1,0.1,0.1,0.1])
alpha = .01
max_iterations = 1000
iteration = 0

# 1. Aplicar la función de coste

# 1.1 Aplicar la función para conocer el valor determinado por el model
def get_predicted_values(w, b):
    return np.dot(X, w) + b

# 1.2 Obtener la diferencia elevada al cuadrado entre predicción y error de cada feature y hacer la media
def get_error_per_feature(prediction, i):
    error = (prediction - y[i])
    return error
   
def get_model_mean_error(w, b):
    predictions = get_predicted_values(w, b)
    errors_sum = 0

    for i, feature_prediction in enumerate(predictions):
        errors_sum = errors_sum + get_error_per_feature(feature_prediction, i)**2
    
    error_mean = errors_sum / (len(predictions)*2)
    return error_mean

# 1.3 Calcular derivada de error sobre w, es decir, el ratio al que aumenta el error con respecto a w cuando w tiene un valor x
def get_error_derivate_w(w, b, w_x_index):
    predictions = get_predicted_values(w, b)
    errors_sum = 0

    for i, feature_prediction in enumerate(predictions):
        errors_sum = errors_sum + get_error_per_feature(feature_prediction, i)*X[i][w_x_index]
    
    return errors_sum / len(predictions)

# 1.4 Calcular derivada de error sobre b, es decir, el ratio al que aumenta el error con respecto a b cuando b tiene un valor x
def get_error_derivate_b(w, b):
    predictions = get_predicted_values(w, b)
    errors_sum = 0

    for i, feature_prediction in enumerate(predictions):
        errors_sum = errors_sum + get_error_per_feature(feature_prediction, i)
    
    return errors_sum / len(predictions)

# 2. Aplicar la función de corrección del modelo
def get_new_w(w ,b, w_x_index):
    new_w = w[w_x_index] - alpha * get_error_derivate_w(w, b, w_x_index)
    return new_w

def get_new_b(w,b):
    new_b = b - alpha * get_error_derivate_b(w, b)
    return new_b

# El problema de esta aplicación es el uso de recursión qu elimita el número de iteraciones posible
# TO DO - mejorar implementación utilizando loops
def run(w,b):
    model_error = get_model_mean_error(w, b)

    new_b = get_new_b(w,b)
    new_w = np.array([0.,0.,0.,0.])

    for i, w_x in enumerate(w):
        new_w[i] = get_new_w(w, b, i)
    
    new_model_error = get_model_mean_error(new_w, new_b)
    print('old error', model_error)
    print('new error', new_model_error)
    print('over 1.9', round(new_model_error, 2))


    if model_error > new_model_error and round(new_model_error, 2) >= 1.99:
        run(new_w, new_b)

    else: 
        print('Result:')
        print(new_w, new_b)
        print('Prediction', get_predicted_values(new_w, new_b))


run(w, b)


# Derivadas

# Ejemplo lineal
# min 10 - 50m por minuto
# min 15 - 60m por minuto

# velocidad = 60 - 50 / 15 - 10 --> 10 / 5 --> velocidad 2m por minuto  

# Ejemplo no lineal (solo se puede saber el ratio en un punto concreto, pues al no ser lineal este varía en cada punto)
# Se despejan utilizando un derivada en la que el distancia entre el punto concreto y el otro 
# punto que se toma como referencia tiende a cero

