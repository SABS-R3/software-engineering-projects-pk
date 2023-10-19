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

## package importing

