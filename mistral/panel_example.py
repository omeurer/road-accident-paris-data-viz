import panel as pn
import param
import numpy as np
import pandas as pd
from bokeh.plotting import figure

pn.extension()

# Create a sample dataframe
x = np.linspace(0, 10, 100)
y = np.sin(x)
data = pd.DataFrame({'x': x, 'y': y})

class DynamicLineChart(param.Parameterized):
    cursor = param.Integer(default=0)

    def __init__(self, data):
        super().__init__()
        self.data = data

    @param.depends('cursor')
    def get_plot(self):
        # Filter the data based on the cursor position
        filtered_data = self.data[self.data['x'] <= self.cursor]

        # Create a Bokeh figure
        p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

        # Add a line to the figure
        p.line(filtered_data['x'], filtered_data['y'], line_width=2)

        # Create a Panel pane from the figure
        plot = pn.pane.Bokeh(p)

        # Add a cross selector to the plot
        cross = pn.widgets.CrossSelector(value=[(0, filtered_data.iloc[0]['y'])], sizing_mode='stretch_width')

        # Combine the plot and cross selector into a single pane
        panel = pn.Column(plot, cross)

        # Create a callback to update the cursor position when the cross selector value changes
        def update_cursor_from_cross(event):
            self.cursor = event.new[0]

        # Watch for changes to the cross selector value
        cross.param.watch(update_cursor_from_cross, 'value')

        return panel


# Create a dynamic line chart
chart = DynamicLineChart(data)

# Create a slider widget to control the cursor position
slider = pn.widgets.IntSlider(name='Cursor', start=0, end=len(data), value=0)

# Combine the chart and slider into a single panel
panel = pn.Column(chart.get_plot, slider)

# Create a callback to update the cursor position when the slider value changes
def update_cursor(event):
    chart.cursor = slider.value

slider.param.watch(update_cursor, 'value')

# Create a callback to update the cursor position when the cross selector value changes
def update_cursor_from_cross(event):
    chart.cursor = event.new

# Show the panel
#panel.show()

panel.save("../mistral/mistral.html")
