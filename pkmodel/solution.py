#
# Solution class
#

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=44):
        self.value = value
    def plot():
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


import numpy as np
import matplotlib.pyplot as plt
t_eval = np.linspace(0,10,100)
q_c = t_eval +2
q_p1 = t_eval +3

def visualise(t_eval, q_c, q_p1):
    fig, ax = plt.subplots()
    #plt.plot(t_eval, q_c, label=Model.name + '- q_c')
    #plt.plot(t_eval, q_p1, label=Model.name + '- q_p1')
    ax.plot(t_eval, q_c)
    ax.plot(t_eval, q_p1)
    #plt.legend()
    ax.set_ylabel('drug mass (ng)')
    ax.set_xlabel('time [h]')

    plt.show()
    return fig

visualise(t_eval, q_c, q_p1)



## package importing

