import statistics as stat
import random as random
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Button, TextBox, RadioButtons

mpl.use("tkagg")

mu, s, n, m, c = 10, 3, 20, 100, 0.95

standard_norm = stat.NormalDist(0,1)

(fig, axes) = plot.subplots()

axes.set_ylabel("Simulation")
axes.set_xlabel("Interval Limits")

fig.subplots_adjust(left=0.5, bottom=0.25)

fig.text(0.05, 0.85, "Population Parameters")
fig.text(0.05, 0.59, "Simulation Parameters")
fig.text(0.05, 0.35, "Confidence Level")

button_axes = fig.add_axes([0.81, 0.05, 0.1, 0.075])
simulate_button = Button(button_axes, "Simulate")

mean_axis = fig.add_axes([0.15, 0.75, 0.25, 0.075])
mean_text = TextBox(mean_axis, "μ: ", textalignment="center")

stdev_axis = fig.add_axes([0.15, 0.65, 0.25, 0.075])
stdev_text = TextBox(stdev_axis, "σ: ", textalignment="center")

n_axis = fig.add_axes([0.15, 0.5, 0.25, 0.075])
n_text = TextBox(n_axis, "n: ", textalignment="center")

m_axis = fig.add_axes([0.15, 0.4, 0.25, 0.075])
m_text = TextBox(m_axis, "m: ", textalignment="center")

confidence_axis = fig.add_axes([0.15, 0.25, 0.25, 0.075])
confidence_text = TextBox(confidence_axis, "Confidence: ", textalignment="center")

button_axes = fig.add_axes([0.81, 0.05, 0.1, 0.075])
simulate_button = Button(button_axes, "Simulate")

def significance():
    global c
    return (1 - c)/2

def critical_value():
    alpha = 1 - significance()
    return standard_norm.inv_cdf(alpha)

def standard_error():
    global s
    return s / math.sqrt(n)

def margin_of_error():
    return standard_error() * critical_value()

def set_mean(new_mu):
    global mu
    mu = float(new_mu)

def set_standard_deviation(new_s):
    global s
    s = float(new_s)

def set_n(new_n):
    global n
    n = int(new_n)

def set_m(new_m):
    global m
    m = int(new_m)

def set_confidence(new_c):
    global c
    c = float(new_c)
    
def set_title():
    plot.suptitle(f"Simulated Confidence Intervals \n Obs Per Sim n = {n}, Sims m = {m}")

def simulate(event):
    global m
    global n
    global mu
    
    moe = margin_of_error()

    means = [
        stat.mean([
            random.gauss(mu, s) for _ in range(n)
        ]) for i in range(m)
    ]

    hits, h_indices= [], []
    misses, m_indices = [], []
    
    for i, xbar in enumerate(means):
        if xbar + moe >= mu and xbar - moe <= mu:
            h_indices.append(i)
            hits.append(xbar)
        else:
            m_indices.append(i)
            misses.append(xbar)

    axes.clear()
    axes.axvline(mu, linestyle="-", color="black")

    # hits
    axes.errorbar(
        x=hits,
        y=h_indices,
        xerr=[ moe for i in range(len(hits)) ],
        color="green",
        fmt='o'
    )

    # misses
    
    axes.errorbar(
        x=misses,
        y=m_indices,
        xerr=[ moe for i in range(len(misses)) ],
        color="red",
        fmt='o'
    )

    set_title()
    fig.canvas.draw_idle()

simulate_button.on_clicked(simulate)
mean_text.on_text_change(set_mean)
stdev_text.on_text_change(set_standard_deviation)
n_text.on_text_change(set_n)
m_text.on_text_change(set_m)
confidence_text.on_text_change(set_confidence)

mean_text.set_val(mu)
stdev_text.set_val(s)
n_text.set_val(n)
m_text.set_val(m)
confidence_text.set_val(c)

set_title()
plot.show()
