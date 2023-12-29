import streamlit as st
from beambending import Beam
import matplotlib.pyplot as plt
from io import BytesIO

with st.expander("Values"):
    bl = st.number_input("Beam Length  ")
    st.write(bl)
    if bl == 0:
        bl = 10
        st.write("Default value is ", bl)

    ps = st.number_input("Pinned support location  ")
    st.write(ps)
    if ps == 0:
        ps = 0
        st.write("Default value is ", ps)

    rs = st.number_input("Rolling support location  ")
    st.write(rs)
    if rs == 0:
        rs = 10
        st.write("Default value is ", rs)

    p1 = st.number_input("Point Load 1  ")
    st.write(p1)
    if p1 == 0:
        p1 = -80
        st.write("Default value is ", p1)

    p2 = st.number_input("Point Load 2  ")
    st.write(p2)
    if p2 == 0:
        p2 = -100
        st.write("Default value is ", p2)

    d1 = st.number_input("Distributed Load 1  ")
    st.write(d1)
    if d1 == 0:
        d1 = -16
        st.write("Default value is ", d1)

    d2 = st.number_input("Distributed Load 2  ")
    st.write(d2)
    if d2 == 0:
        d2 = -8
        st.write("Default value is ", d2)

    x1 = st.number_input("Type the distance x1  ")
    st.write(x1)
    if x1 == 0:
        x1 = 2
        st.write("Default value is ", x1)
    x2 = st.number_input("Type the distance x2  ")
    st.write(x2)
    if x2 == 0:
        x2 = 9
        st.write("Default value is ", x2)

    xd1 = st.number_input("Type the first distributed loads first distance  ")
    st.write(xd1)
    if xd1 == 0:
        xd1 = 0
        st.write("Default value is ", xd1)

    xd11 = st.number_input("Type the first distributed loads second distance  ")
    st.write(xd11)
    if xd11 == 0:
        xd11 = 7
        st.write("Default value is ", xd11)

    xd2 = st.number_input("Type the second distributed loads first distance  ")
    st.write(xd2)
    if xd2 == 0:
        xd2 = 4
        st.write("Default value is ", xd2)

    xd22 = st.number_input("Type the second distributed loads second distance  ")
    st.write(xd22)
    if xd22 == 0:
        xd22 = 10
        st.write("Default value is ", xd22)

calculate = st.button('Calculate')

with st.expander("Calculator"):
    st.header("Moment Diagram Calculator")
    if calculate:
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

            # Call the calculator function to get the plot buffer
            plot_buffer = calculator()

            # Display the plot using Streamlit
            st.image(plot_buffer, use_column_width=True)


        if __name__ == "__main__":
            main()
