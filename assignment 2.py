import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
class Program:
    def generate_camber_line(self, func, x_values):
        y_values = func(x_values)
        return y_values

    def compute_slope(self, func_derivative, x_value):
        return func_derivative(x_value)

    def thin_airfoil_cl(self, alpha, camber_slope):
        return 2 * np.pi * alpha

    # def plot_vector_field(circulation_distribution):
    #     # Plotting vector field based on circulation distribution
    #     pass

    # def compute_circulation(line_integral_func):
    #     circulation, _ = quad(line_integral_func, 0, 1)
    #     return circulation

    def main(self):
        # User input for camber line function
        def camber_func(x):
            return 10*(x- x*x)

        # User input for camber line slope function
        def camber_slope_func(x):
            return 2

        # # User input for circulation distribution function
        # def circulation_distribution(x, y):
        #     return 1.0

        # User input for angle of attack
        alpha = 5.0  # degrees

        # Generate x values from 0 to 1
        x_values = np.linspace(0, 1, 100)

        # Generate camber line
        camber_line = self.generate_camber_line(camber_func, x_values)

        # Compute slope of camber line at a given point
        camber_slope = self.compute_slope(camber_slope_func, 0.5)

        # Compute Cl of the thin airfoil
        cl = self.thin_airfoil_cl(np.deg2rad(alpha), camber_slope)

        
        # Print lift coefficient
        print("Lift coefficient (Cl):", cl)

        # Plot camber line
        plt.plot(x_values, camber_line, label='Camber Line')

        # Plot airfoil
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('Chord Length (x)')
        plt.ylabel('Camber Line (y)')
        plt.title('Airfoil')
        plt.legend()
        plt.grid()
        plt.show()

        # Plot vector field around the airfoil
        # plot_vector_field(circulation_distribution)

        # # Compute circulation around the airfoil
        # circulation = compute_circulation(circulation_distribution)
        # print("Circulation around the airfoil:", circulation)







airfoil1 = Program()
airfoil1.main()
