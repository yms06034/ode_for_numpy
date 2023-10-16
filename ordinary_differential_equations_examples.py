import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from ode_helpers import state_plotter

def state_plotter(times, states, fig_num):
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    plt.figure(fig_num)
    plt.clf()
    fig, ax = plt.subplots(num_rows, num_cols, num=fig_num, clear=True,
                         squeeze=False)
    for n in range(num_states):
        row = n // num_cols
        col = n % num_cols
        ax[row][col].plot(times, states[n], 'k.:')
        ax[row][col].set(xlabel='Time',
                         ylabel='$y_{:0.0f}(t)$'.format(n),
                         title='$y_{:0.0f}(t)$ vs. Time'.format(n))
        
    for n in range(num_states, num_rows * num_cols):
        fig.delaxes(ax[n // num_cols][n % num_cols])

    fig.tight_layout()

    return fig, ax

def f(t, y, c):
    dydt = [c[0]]
    return dydt

tspan = np.linspace(0, 10, 100)
yinit = [6]
c = [1.2]

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)

state_plotter(sol.t, sol.y, 1)

def f(t, y, c):
    dydt = np.polyval(c, t)
    return dydt
    
tspan = np.linspace(0, 4, 20)
yinit = [6]
c = [2, -6, 3]

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)

state_plotter(sol.t, sol.y, 1)

def f(t, y, c):
    dydt = [c[0] * y[0]]
    return dydt
    
tspan = np.linspace(0, 3, 25)
yinit = [10]
c = [1.02]

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)

state_plotter(sol.t, sol.y, 1)

def f(t, y, c):
    dydt = [c[0]*np.cos(c[1]*t), c[2]*y[0]+c[3]*t]
    return dydt

tspan = np.linspace(0, 5, 100)
yinit = [0, -3]
c = [4, 3, -2, 0.5]

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)

state_plotter(sol.t, sol.y, 1)

def f(t, y, c):
    dydt = [y[1], y[2], c[0]]
    return dydt

tspan = np.linspace(0, 8, 50)
yinit = [6, 2, -4]
c = [1.3]

sol = solve_ivp(lambda t, y: f(t, y, c), 
                [tspan[0], tspan[-1]], yinit, t_eval=tspan, rtol = 1e-5)

state_plotter(sol.t, sol.y, 1)