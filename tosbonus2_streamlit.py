$ pip install beambending
$ pip install matplotlib

import streamlit as st
from beambending import Beam
import matplotlib.pyplot as plt
from io import BytesIO


# Creating a function to calculation
def calculator():
    beam = Beam(10)  # Beam's length
    beam.pinned_support = 0  # Pinned Support Location
    beam.rolling_support = 10  # Rolling Support Location

    from beambending import DistributedLoadV, PointLoadV

    # Define loads and locations. [load,location]
    beam.add_loads([
        PointLoadV(-80, 2),  # 80kN downwards, at x=3m
        PointLoadV(-100, 9),  # 100kN downwards, at x=9m
        DistributedLoadV(-16, (0, 7)),  # 16kN/m, downward, for 0m <= x <= 7m
        DistributedLoadV(-8, (4, 10)),  # -8kN/m,  downwards, for 4m <= x <= 10m
    ])

    # Create a new figure and axes
    plt.subplots()
    # Use the plot method on the Beam object
    beam.plot()
    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer


def main():
    st.title("Moment Diagram Calculator")

    # Call the calculator function to get the plot buffer
    plot_buffer = calculator()

    # Display the plot using Streamlit
    st.image(plot_buffer, use_column_width=True)


if __name__ == "__main__":
    main()
