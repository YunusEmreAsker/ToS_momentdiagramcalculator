from beambending import Beam
import matplotlib.pyplot as plt


# Creating a function to calculation
def calculator():
    beam = Beam(10)  # # Beam's length

    beam.pinned_support = 0  # Pinned Support Location
    beam.rolling_support = 10  # Rolling Support Location

    from beambending import DistributedLoadV, PointLoadV

    beam.add_loads([
        PointLoadV(-80, 2),  # 80kN downwards, at x=3m
        PointLoadV(-100, 9),  # 100kN downwards, at x=9m
        DistributedLoadV(-16, (0, 7)),  # 16kN/m, downward, for 0m <= x <= 7m
        DistributedLoadV(-8, (4, 10)),  # -8kN/m,  downwards, for 4m <= x <= 10m
    ])

    beam.plot()
    plt.show()


calculator()
