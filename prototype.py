import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

def dose(t, X):
    return X

#intravenous injection model

def IV(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]
print(IV(2,[1,2],3,4,5,6,7))
model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

#subcutaneous dosing
def SC(t, y, Q_p1, V_c, V_p1, CL, X, ka):
    q_c, q_p1, q0= y
    dq0_dt = dose(t,X) - ka*q0
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = ka*q0 - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt,dq0_dt]


model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
    'ka':1.0
}

t_eval = np.linspace(0, 1, 1000)
y0 = np.array([0.0, 0.0])

fig = plt.figure()

args = [
    model1_args['Q_p1'], model1_args['V_c'], model1_args['V_p1'], model1_args['CL'], model1_args['X']
]
sol = scipy.integrate.solve_ivp(
    fun=lambda t, y: IV(t, y, *args),
    t_span=[t_eval[0], t_eval[-1]],
    y0=y0, t_eval=t_eval
)
plt.plot(sol.t, sol.y[0, :], label=model1_args['name'] + '- q_c')
plt.plot(sol.t, sol.y[1, :], label=model1_args['name'] + '- q_p1')



y0 = np.array([0.0, 0.0, 0.0])

args = [
    model2_args['Q_p1'], model2_args['V_c'], model2_args['V_p1'], model2_args['CL'], model2_args['X'], model2_args['ka']
]
sol = scipy.integrate.solve_ivp(
    fun=lambda t, y: SC(t, y, *args),
    t_span=[t_eval[0], t_eval[-1]],
    y0=y0, t_eval=t_eval
)
plt.plot(sol.t, sol.y[0, :], label=model2_args['name'] + '- q_c')
plt.plot(sol.t, sol.y[1, :], label=model2_args['name'] + '- q_p1')

plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')

plt.savefig('plot.png')

