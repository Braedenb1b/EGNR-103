#CONSTANTS
import math
RHO = 1.2
#asking for users input values
wind_speed = float(input("Enter average wind speed (m/s): "))
turbine_radius = float(input("Enter turbine blade radius (m): "))
efficiency = float(input("Enter operational efficiency (%): "))
#actual calculations
area = math.pi * turbine_radius ** 2
p_max = 0.5 * RHO * area * wind_speed ** 3
efficiency_d = efficiency * 0.01
p_act = p_max * efficiency_d
#showing final calculations
print("The maximum power output is:", p_max, "Joules")
print("The actual power output is:", p_act, "Joules")
