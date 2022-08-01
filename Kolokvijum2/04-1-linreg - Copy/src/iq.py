from __future__ import print_function
from sklearn.linear_model import LinearRegression

# TODO 4: implementirati primenu visestruke linearne regresije
# nad podacima iz datoteke "data/iq.tsv".
# Korisiti implementaciju linearne regresije u alatu scikit-learn

if __name__ == '__main__':
    data_x = []
    data_y = []
    with open('C:\\Users\\Marija\\Desktop\\04-1-linreg\\data\\iq.tsv', 'r') as file:
        for line in file:
            try:
                row = [float(num) for num in line.split()]
                data_x.append(row[1:])
                data_y.append(row[0])
            except:
                pass
    lr = LinearRegression().fit(data_x, data_y)
    print(lr.coef_)
    print(lr.intercept_)
