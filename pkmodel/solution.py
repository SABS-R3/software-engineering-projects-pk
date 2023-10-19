import numpy as np
import matplotlib.pylab as plt
import model

def visualise(modeldata):
    time=np.linspace(0,1,1000)
    fig, ax = plt.subplots()
    # Plot q_c
    plt.plot(time, modeldata[0,:], label = 'q_c')
    # Plot q_p1
    plt.plot(time, modeldata[1,:], label = 'q_p1')
    # Plot q_0
    if np.shape(modeldata) == (3, 1000):
        plt.plot(time, modeldata[2,:], label = 'q_0')
        plt.title('Subcutaneous model')
    else:
        plt.title('IV model')
    plt.legend()
    ax.set_ylabel('drug mass (ng)')
    ax.set_xlabel('time [h]')
    #plt.savefig('plot.png')
    plt.show()

parameter=[1,2,3,4,5]

result=visualise(model.IV.integrate())
print(result)