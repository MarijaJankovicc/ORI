from __future__ import print_function

import matplotlib.pyplot as plt
from linreg_simple import linear_regression, create_line, predict

if __name__ == '__main__':

    patientAge = []
    glucose = []

    with open('./../../04-1-linreg - Copy/data/dataset.csv', 'r') as file:
        for line in file:
            data = line.split(',')
            try:
                glucose.append(float(data[8]))
                patientAge.append(float(data[2]))
            except:
                pass

    slope, intercept = linear_regression(patientAge, glucose)

    avg_glucose_level25 = predict(25, slope, intercept)
    avg_glucose_level45 = predict(45, slope, intercept)
    avg_glucose_level65 = predict(65, slope, intercept)

    print(avg_glucose_level25, avg_glucose_level45, avg_glucose_level65)

    line_glucose = create_line(patientAge, slope, intercept)

    plt.plot(patientAge, glucose, '.')
    plt.plot(patientAge, line_glucose, 'r')
    plt.title('Slope: {0}, intercept: {1}'.format(slope, intercept))
    plt.show()