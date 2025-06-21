import statistics as stat
import math as math
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Button, TextBox, Slider

null_mean = 11
alternate_mean = 10
stdev = 3
n = 15
significance = 0.05
increments = 1000

std_err = stdev / math.sqrt(n)

(fig, axes) = plot.subplots()

axes.set_ylabel("Probability Density")
axes.set_xlabel("Sample Mean")

fig.subplots_adjust(left=0.5, bottom=0.10)

fig.text(0.05, 0.85, "Null Distribution")
fig.text(0.05, 0.70, "Alternate Distribution")

null_axis = fig.add_axes([0.20, 0.75, 0.15, 0.075])
null_slider = Slider(
    ax=null_axis,
    label="μ_null",
    valmin=10,
    valmax=14,
    valinit=null_mean,
    orientation="horizontal"
)
         
alternate_axis = fig.add_axes([0.20, 0.60, 0.15, 0.075])
alternate_slider = Slider(
    ax=alternate_axis,
    label="μ_alternate",
    valmin=7,
    valmax=11,
    valinit=alternate_mean,
    orientation="horizontal"
)
         
significance_axis = fig.add_axes([0.20, 0.475, 0.15, 0.075])
significance_text = TextBox(significance_axis, "Significance: ", textalignment="center")

n_axis = fig.add_axes([0.20, 0.375, 0.15, 0.075])
n_text = TextBox(n_axis, "n: ", textalignment="center")

fig.text(0.05, 0.30, "Results")

power_axis = fig.add_axes([0.20, 0.20, 0.15, 0.075])
power_text = TextBox(power_axis, "Power: ", textalignment="center")

error_axis = fig.add_axes([0.20, 0.10, 0.15, 0.075])
error_text = TextBox(error_axis, "P(Type II Error): ", textalignment="center")

def set_title():
    line = "Null vs Alternative Distribution \n"
    line += f"Ho: μ = {round(null_mean,2)} vs Ha: μ < {round(null_mean,2)} when  μ = {round(alternate_mean,2)} \n"
    line += f"Known Std Dev σ of  = {stdev}, n = {n}"
    plot.suptitle(line)

def redraw():
    axes.clear()
    
    start = int(
        min([ null_mean - 3 * std_err, alternate_mean - 3 * std_err])
    )
    end = int(
        max([null_mean + 3 * std_err, alternate_mean + 3 * std_err])
    )
    delta = (end - start)/increments
    
    null = stat.NormalDist(null_mean, stdev/math.sqrt(n))
    alternate = stat.NormalDist(alternate_mean, stdev/math.sqrt(n))

    null_crit = crit = null.inv_cdf(significance)
    power = alternate.cdf(null_crit)
    
    power_text.set_val(round(power, 4))
    error_text.set_val(round(1-power, 4))

    axis = [ start + delta*i for i in range(increments+1) ]
    null_density = [ null.pdf(x) for x in axis ]
    alternate_density = [ alternate.pdf(x) for x in axis ]

    axes.plot(axis, null_density, label = "Null", color = "black")
    axes.plot(axis, alternate_density, label = "Alternate", color = "gray")

    lower_null_axis = [ x for x in axis if x < null_crit ]
    lower_null_region = [ null.pdf(x) for x in lower_null_axis ]
    axes.fill_between(lower_null_axis, lower_null_region, 0, color = "green", alpha = 0.5)

    upper_alternate_axis = [ x for x in axis if x > null_crit ]
    upper_alternate_region = [ alternate.pdf(x) for x in upper_alternate_axis ]
    axes.fill_between(upper_alternate_axis, upper_alternate_region, 0, color = "red", alpha = 0.5)

    lower_alternate_axis = [ x for x in axis if x <= null_crit ]
    lower_alternate_region = [ alternate.pdf(x) for x in lower_alternate_axis ]
    axes.fill_between(lower_alternate_axis, lower_alternate_region, 0, color = "green", alpha = 0.5)
    
    fig.legend()
    set_title()
    fig.canvas.draw_idle()

def set_n(new_n):
    global n
    n = float(new_n)
    redraw()
    
def set_null_mean(new_mu):
    global null_mean
    null_mean = float(new_mu)
    redraw()
    
def set_alternate_mean(new_mu):
    global alternate_mean
    alternate_mean = float(new_mu)
    redraw()
    
def set_significance(new_alpha):
    global significance
    significance = float(new_alpha)
    redraw()


null_slider.on_changed(set_null_mean)
alternate_slider.on_changed(set_alternate_mean)
significance_text.on_text_change(set_significance)
n_text.on_text_change(set_n)

significance_text.set_val(significance)
n_text.set_val(n)
plot.show()
