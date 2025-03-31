import math
import statistics as stat
import matplotlib as mpl
import matplotlib.pyplot as plot
from matplotlib.widgets import Slider
import matplotlib.patches as patches

mpl.use("tkagg")

(fig, axes) = plot.subplots()

fig.subplots_adjust(left=0.25, bottom=0.25)

init_b_zero, init_b_one = 1, 1

squares = []

x_data = [ 1, 4, 5, 8 ]
y_data = [ 4, 5, 9, 11 ]

def regression_line(x, b_zero, b_one):
    return b_zero + b_one * x

def regression_data(b_zero, b_one):
    line = [ regression_line(x, b_zero, b_one) for x in x_data ]
    res = [ act - pred for (pred, act) in zip(line, y_data) ]
    return line, res

def residual_squares(res, line):
    sqs = [
        patches.Rectangle((x, y - math.sqrt(r**2)), math.sqrt(r**2), math.sqrt(r**2), linewidth=1, edgecolor='r', facecolor='none')
        if r > 0 else
        patches.Rectangle((x, y), math.sqrt(r**2), math.sqrt(r**2), linewidth=1, edgecolor='r', facecolor='none')

        for (x, y, l, r) in zip(x_data, y_data, line, res)
    ]
    for s in sqs:
        # Add the patch to the Axes
        axes.add_patch(s)


# Make a horizontal slider to control the intercept
ax_intercept = fig.add_axes([0.25, 0.1, 0.65, 0.03])
intercept_slider = Slider(
    ax=ax_intercept,
    label='Intercept',
    valmin=-30,
    valmax=30,
    valinit=init_b_zero
)

# Make a vertically oriented slider to control the slope
ax_slope = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
slope_slider = Slider(
    ax=ax_slope,
    label="Slope",
    valmin=-10,
    valmax=10,
    valinit=init_b_one,
    orientation="vertical"
)

axes.scatter(x_data, y_data)

predicted_y_data, residuals = regression_data(init_b_zero, init_b_one)
residual_squares(residuals, predicted_y_data)
area = sum(r**2 for r in residuals)
least_squares, = axes.plot(x_data, predicted_y_data, color="green")
least_squares_text = axes.text(0, 0, f"Total Area: {area}")

# The function to be called anytime a slider's value changes
def update(val):
    for p in axes.patches:
        p.remove()
        
    new_predictions, res = regression_data(intercept_slider.val, slope_slider.val)
    residual_squares(res, new_predictions)
    new_area = sum(r**2 for r in res)
    least_squares.set_ydata(new_predictions)
    least_squares_text.set_text(f"Total Area: {new_area}")
    fig.canvas.draw_idle()

intercept_slider.on_changed(update)
slope_slider.on_changed(update)
plot.show()
