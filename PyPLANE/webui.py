
"""
TODO: Info about UI
"""

from nicegui import ui

# Function to take data and generate a plot
def clicked_plot(x_prime: str, y_prime, params: dict = dict()):
    ui.notification("test")

with ui.row():
    with ui.card():
        """
        Card to contain equation and parameter inputs
        """

        # Use markdown for formatting of headings
        ui.markdown("# Inputs\n## Equations")

        # Inputs for the derivative of x and y
        x_prime_input = ui.input(label="x' = ")
        y_prime_input = ui.input(label="y' = ")

        # Inputs for the limits of the x and y axes on the plot that will be generated
        ui.markdown("## Limits of plot axes")
        with ui.row():
            lower_x_input = ui.input(label="Lower x limit:")
            ui.label("< x <")
            upper_x_input = ui.input(label="Upper x limit:")

        with ui.row():
            lower_y_input = ui.input(label="Lower y limit:")
            ui.label("< y <")
            upper_y_input = ui.input(label="Upper y limit:")

        # Parameters that can be added optionally
        ui.markdown("## Parameters")
        with ui.row():
            ui.input(label="Parameter name")
            ui.label(" = ")
            ui.input(label="Parameter Value", placeholder="<a number>")
        
        ui.button("Plot", on_click=lambda: clicked_plot(x_prime_input.value, y_prime_input.value))


    with ui.card():
        ui.markdown("# Placeholder for plots")

ui.run(title="CoolHandyODESolver")