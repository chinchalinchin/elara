import statistics as stat
import random as random
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Button, TextBox, RadioButtons

mpl.use("tkagg")

mu, s, n, m = 10, 3, 20, 100

simulation_goal = "sample mean"

(fig, axes) = plot.subplots()

fig.subplots_adjust(left=0.5, bottom=0.25)

axes.set_xlabel("Simulated Statistic")
axes.set_ylabel("Probability Density")

fig.text(0.05, 0.85, "Population Parameters")
fig.text(0.05, 0.59, "Simulation Parameters")
fig.text(0.05, 0.35, "Simulated Statistic")

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

stat_axis = fig.add_axes([0.05, 0.04, 0.35, 0.3])
stat_radio = RadioButtons(
    stat_axis,
    (
        'sample mean',
        'sample median',
        'sample variance(n)',
        'sample variance(n-1)',
        'sample iqr',
        'sample range'
    ),
    label_props={
        'color': [ 'red', 'blue', 'green', 'orange', 'yellow', 'purple']
    },
    radio_props={
        'facecolor': ['red', 'blue', 'green', 'orange', 'yellow', 'purple'],
        'edgecolor': ['darkred', 'darkblue', 'darkgreen', 'darkorange', 'gold', 'black'],
    }
)

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

def set_simulation_goal(goal):
    global simulation_goal
    simulation_goal = goal

def set_title():
    plot.suptitle(f"Simulated Sampling Distributions \n Obs Per Sim n = {n}, Sims m = {m}")

def simulate(event):
    # simulate samples from a normal population
    
    sampling_distribution = []
    
    for i in range(m):
        sim_sample = [
            random.gauss(mu, s) for _ in range(n)
        ]

        if simulation_goal == "sample mean":
            sampling_distribution.append(
                stat.mean(sim_sample)
            )
            
        elif simulation_goal == "sample median":
            sampling_distribution.append(
                stat.median(sim_sample)
            )

        elif simulation_goal == "sample variance(n)":
            sampling_distribution.append(
                stat.pvariance(sim_sample)
            )
        
        elif simulation_goal == "sample variance(n-1)":
            sampling_distribution.append(
                stat.variance(sim_sample)
            )

        elif simulation_goal == "sample iqr":
            percentiles = stat.quantiles(sim_sample, n=100)
            iqr = percentiles[74] - percentiles[24]
            sampling_distribution.append(
                iqr
            )
            
        elif simulation_goal == "sample range":
            s_range = max(sim_sample) - min(sim_sample)
            sampling_distribution.append(
                s_range
            )
            
    axes.clear()
    axes.set_xlabel("Observation")
    axes.set_ylabel("Probability Density")

    simulated_stat = stat.mean(sampling_distribution)

    if simulation_goal == "sample mean":
        axes.axvline(mu, linestyle="-", color="red", label="True Value")

    elif simulation_goal == "sample variance(n)" \
       or simulation_goal == "sample variance(n-1)":
        axes.axvline(s**2, linestyle="-", color="red", label="True Value")

    elif simulation_goal == "sample median":
        axes.axvline(mu, linestyle="-", color="red", label="True Value")


    elif simulation_goal == "sample iqr":
        dist = stat.NormalDist(mu, s)
        iqr = dist.inv_cdf(0.75) - dist.inv_cdf(0.25)
        axes.axvline(iqr, linestyle="-", color="red", label="True Value")

    elif simulation_goal == "sample range":
        axes.axvline(6*s, linestyle="-", color="red", label="True Value")
        
    axes.axvline(simulated_stat, linestyle="--", color="green", label="Estimated Value")
    
    axes.hist(sampling_distribution, density=True, color="lightblue", ec="darkblue")

    axes.legend()

    set_title()
    
    fig.canvas.draw_idle()

simulate_button.on_clicked(simulate)
stat_radio.on_clicked(set_simulation_goal)

mean_text.on_text_change(set_mean)
stdev_text.on_text_change(set_standard_deviation)
n_text.on_text_change(set_n)
m_text.on_text_change(set_m)

mean_text.set_val(mu)
stdev_text.set_val(s)
n_text.set_val(n)
m_text.set_val(m)

set_title()
plot.show()
