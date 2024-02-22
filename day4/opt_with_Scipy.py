import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt


exp_data = np.load('I_q_IPA_exp.npy')
model_data = np.load('I_q_IPA_model.npy')


###add interpolate function
interp_func = interp1d(model_data[:, 0], model_data[:, 1])

# loss function
def loss(scale):
    scaled_model_data = interp_func(exp_data[:, 0]) * scale
    return np.sum((scaled_model_data - exp_data[:, 1])**2)

#find the best scaling factor
result = minimize_scalar(loss)

# 
best_scale = result.x
scaled_model_data = interp_func(exp_data[:, 0]) * best_scale

# Visualize the result
plt.plot(exp_data[:, 0], exp_data[:, 1], label='Experimental Data')
plt.plot(exp_data[:, 0], scaled_model_data, label='Scaled Model Data')
plt.xlabel('Scattering Vector')
plt.ylabel('Scattering Strength')
plt.legend()
plt.show()
