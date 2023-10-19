#
# Model class
#
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate
from scipy.integrate import odeint

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=42):
        self.value = value   

class IV(Model):
    # Your class definition here
    def __init__(self, parameters=[0, 0, 0, 0, 0]):
        super().__init__()
        self.parameters = parameters

    def param(self, y, t):
        Q_p1, V_c, V_p1, CL, X = self.parameters
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = X - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]


# Create an instance of the IV class
iv_instance = IV()

# Define the time points at which you want to evaluate the solution
t_eval = np.linspace(0, 1, 1000)

# Initial conditions
y0 = [0.0, 0.0]

# Parameters
parameters = [0.7, 1, 2, 3, 4]

# Set the parameters in the instance
iv_instance.parameters = parameters

# Solve the ODEs using odeint
solution = odeint(iv_instance.param, y0, t_eval)

# Extract the results
q_c, q_p1 = solution.T

# Print the results
print(q_c)
print(q_p1)


class SC(Model):
    "subcutaneous model"
    def __init__(self, parameters=[0, 0, 0, 0, 0,0]):
        super().__init__()
        self.parameters = parameters

    def param(self, y, t):
        Q_p1, V_c, V_p1, CL, X, ka = self.parameters
        q_c, q_p1, q0= y
        dq0_dt = X - ka*q0
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = ka*q0 - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt,dq0_dt]


# Create an instance of the IV class
sc_instance = SC()

# Define the time points at which you want to evaluate the solution
t_eval = np.linspace(0, 1, 1000)

# Initial conditions
y0 = [0.0, 0.0,0]

# Parameters
parameters = [0.7, 1, 2, 3, 4,7]

# Set the parameters in the instance
sc_instance.parameters = parameters

# Solve the ODEs using odeint
solution = odeint(sc_instance.param, y0, t_eval)

print(solution.shape)

# Extract the results
print(solution.T.shape)
q_c, q_p1, q_0 = solution.T

# Print the results
print(q_c.shape)
print(q_p1.shape)
print(solution.y[0, :])
