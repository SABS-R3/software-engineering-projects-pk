#
# Model class
#
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

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
    "intraveinous model  : : calls parent class Model"
    def __init__(self, args=[0, 0, 0, 0, 0]):
        super().__init__()
        self.args=args

    def dose(self, t, X):
        return X
    
    #def IV(self, t, y, Q_p1, V_c, V_p1, CL, X):
    def param(self, t, y, Q_p1, V_c, V_p1, CL, X):
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.dose(t, X) - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    # def integrate(self, Q_p1, V_c, V_p1, CL, X):
    #     t_eval = np.linspace(0, 1, 1000)
    #     y0 = np.array([0.0, 0.0])
    #     sol = scipy.integrate.solve_ivp(
    #         fun=lambda t, y: self.param(t, y, Q_p1, V_c, V_p1, CL, X),
    #         t_span=[t_eval[0], t_eval[-1]],
    #         y0=y0,
    #         t_eval=t_eval)
    #     return sol

# iv_model = IV()
# solution = iv_model.integrate(1,2,3,4,5)
# print(solution)

t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0.0, 0.0])
sol = scipy.integrate.solve_ivp(
    fun=lambda t, y: IV.param(self, t, y, 1, 2, 3, 4, 5),
    t_span=[t_eval[0], t_eval[-1]],
    y0=y0,
    t_eval=t_eval)

print(sol)


model1_args = {
    'name': 'model1', 
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,}

class SC(Model):
    "subcutaneous model"
    def __init__(self, name):
        super().__init__(name)
        #self.observations = []

    def dose(self, t, X):
        return X

    #def SC(self, t, y, Q_p1, V_c, V_p1, CL, X, ka):
    def SC(self, t, y, *args):
        q_c, q_p1, q0= y
        dq0_dt = dose(t,X) - ka*q0
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = ka*q0 - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt,dq0_dt]
    
    model2_args = {
    'name': 'model2',
    'Q_p1': 0,
    'V_c': 0,
    'V_p1': 0,
    'CL': 0,
    'X': 0,
    'ka': 0}



### how to make scipy y integration value connected with the visualisation/solution class which acitvely uses scipy