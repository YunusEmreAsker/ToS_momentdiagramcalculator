import streamlit as st
from beambending import Beam
import matplotlib.pyplot as plt
from io import BytesIO


def calculator():
    beam = Beam(10)
    beam.pinned_support = 0
    beam.rolling_support = 10

    from beambending import DistributedLoadV, PointLoadV

    beam.add_loads([
        PointLoadV(-80, 2),
        PointLoadV(-100, 9),
        DistributedLoadV(-16, (0, 7)),
        DistributedLoadV(-8, (4, 10)),
    ])

    # Create a new figure and axes
    _, ax = plt.subplots()

    # Use the plot method on the Beam object (without passing axes)
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
