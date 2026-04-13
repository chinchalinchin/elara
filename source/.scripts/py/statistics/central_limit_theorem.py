import statistics as stat
import random as random
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Button, TextBox, RadioButtons

mpl.use("tkagg")

dist_params = {
    "normal": {
        "key": "Normal(μ = 10, σ = 3)",
        "mu": 10,
        "sigma": 3,
    },
    "beta": {
        "key": "Beta(α = 8, β = 2)",
        "alpha": 8,
        "beta": 2,
    },
    "gamma": {
        "key": "Gamma(κ = 2, θ = 2)",
        "kappa": 2,
        "theta": 2

    },
    "exponential": {
        "key": "Exponential(λ = 1)",
        "lambda": 1
    }
}

pop = []
pop_approx = 10000
sim_approx = 1000
n = 30

distribution = dist_params["normal"]["key"]

(fig, axes) = plot.subplots(2)

axes[0].set_ylabel("%")
axes[0].set_xlabel("Observation")
axes[0].set_title("Population Distribution")
axes[1].set_ylabel("%")
axes[1].set_xlabel("Sample Mean")


fig.subplots_adjust(left=0.5, bottom=0.25)

fig.text(0.05, 0.85, "Population Distribution")
fig.text(0.05, 0.59, "Sampling Parameters")

button_axes = fig.add_axes([0.81, 0.05, 0.1, 0.075])
simulate_button = Button(button_axes, "Simulate")

n_axis = fig.add_axes([0.15, 0.5, 0.25, 0.075])
n_text = TextBox(n_axis, "n: ", textalignment="center")

dist_axis = fig.add_axes([0.15, 0.675, 0.25, 0.15])
dist_radio = RadioButtons(
    dist_axis,
    (
        dist_params["normal"]["key"],
        dist_params["beta"]["key"],
        dist_params["gamma"]["key"],
        dist_params["exponential"]["key"],
    ),
    label_props={
        'color': [ 'red', 'blue', 'green','purple']
    },
    radio_props={
        'facecolor': ['red', 'blue', 'green','purple'],
        'edgecolor': ['darkred', 'darkblue', 'gold', 'black'],
    }
)

button_axes = fig.add_axes([0.81, 0.05, 0.1, 0.075])
sample_button = Button(button_axes, "Sample")

def set_n(new_n):
    global n
    n = int(new_n)
    set_title()
    fig.canvas.draw_idle()

def set_distribution(new_distribution):
    global distribution
    distribution = new_distribution
    
def set_title():
    global n
    plot.suptitle(f"The Central Limit Theorem\n Samples = {n}")

def get_obs():
    global distribution
    
    if distribution == dist_params["beta"]["key"]:
        return random.betavariate(
            dist_params["beta"]["alpha"],
            dist_params["beta"]["beta"]
        )
    if distribution == dist_params["gamma"]["key"]:
        return random.gammavariate(
            dist_params["gamma"]["kappa"],
            dist_params["gamma"]["theta"]
        )
    if distribution == dist_params["exponential"]["key"]:
        return random.expovariate(
            dist_params["exponential"]["lambda"]
        )
    return random.gauss(
        dist_params["normal"]["mu"],
        dist_params["normal"]["sigma"]
    )

def generate(new_distribution):
    global distribution
    global pop_approx
    global pop

    distribution = new_distribution
    
    pop = [
        get_obs() for _ in range(pop_approx)
    ]
    axes[0].clear()
    axes[0].hist(pop, color="lightblue", ec="blue", density=True)
    fig.canvas.draw_idle()

def sample(event):
    global n
    global sim_approx
    global pop

    means = [
        stat.mean([
            random.choice(pop) for _ in range(n)
        ])
        for _ in range(sim_approx)
    ]
    
    axes[1].clear()
    axes[1].hist(means, color="lightblue", ec="blue", density=True)
    fig.canvas.draw_idle()

sample_button.on_clicked(sample)
dist_radio.on_clicked(generate)

n_text.on_text_change(set_n)

n_text.set_val(n)

set_title()
generate(distribution)
plot.show()
