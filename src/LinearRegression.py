import numpy as np
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
# lib name : scikit-learn

# import LinearRegression.csv
# importe LinearRegression.csv


def regression_2opt():

    data = pd.read_csv('../Datas/linearRegression2opt.csv', index_col=0)
    data.head()

    # Create the object Linear regression
    # créer un objet reg lin
    modele_reg = LinearRegression()

    # Create y and X
    # créer y et X
    axes = data.columns.drop("time")
    y = data.time
    x = data[axes]

    modele_reg.fit(x, y)

    print("intercept: ")
    print(modele_reg.intercept_)
    print("coef: ")
    print(modele_reg.coef_)

    # Calculate R²
    # calcul du R²
    modele_reg.score(x, y)

    RMSE = np.sqrt(((y - modele_reg.predict(x)) ** 2).sum() / len(y))
    print("RMSE: ")
    print(RMSE)
    plt.plot(x,y)
    plt.grid()
    plt.title("Regression 2-opt Algorithm", fontsize=10)
    plt.xlabel('Matrix size (cities)')
    plt.ylabel('time (s)')
    plt.show()

    plt.plot(y, modele_reg.predict(x), '.')
    plt.grid()
    plt.title("Regression 2-opt Algorithm", fontsize=10)
    plt.xlabel('Root mean square error')
    plt.ylabel('time (s)')
    plt.show()

    # plt.plot(y, y-modele_reg.predict(x), '.')
    # plt.show()


def regression_sa():

    data = pd.read_csv('../Datas/linearRegressionSA.csv', index_col=0)
    data.head()
    # xaxe = pd.read_csv(r'../Datas/linearRegressionSA.csv', usecols=[2], skiprows=1)
    # yaxe = pd.read_csv(r'../Datas/linearRegressionSA.csv', usecols=[2], skiprows=1)
    # xaxes = (list([xaxe]))
    # yaxes = (list([yaxe]))
    #
    # lr = sc.stats.linregress(xaxes, yaxes)

    # fit = np.polyfit(xaxes, yaxes, 1)
    # print(fit)
    #np.polyfit(np.x), y, 1)

    # Create the object Linear regression
    # créer un objet reg lin
    modele_reg = LinearRegression()

    # Create y and X
    # créer y et X
    axes = data.columns.drop("time")
    y = data.time
    x = data[axes]

    modele_reg.fit(x, y)

    print("intercept: ")
    print(modele_reg.intercept_)
    print("coef: ")
    print(modele_reg.coef_)

    # Calculate R²
    # calcul du R² (coefficent de determination(coefficient de correlation²))
    modele_reg.score(x, y)

    #Root Mean Square Error
    RMSE = np.sqrt(((y - modele_reg.predict(x)) ** 2).sum() / len(y))
    print("RMSE: ")
    print(RMSE)
    plt.plot(x,y)
    plt.grid()
    plt.title("Linear Regression Simulated Annealing Algorithm", fontsize=10)
    plt.xlabel('Matrix size (cities)')
    plt.ylabel('time (s)')
    plt.show()

    plt.plot(y, modele_reg.predict(x), '.')
    plt.grid()
    plt.title("Linear Regression Simulated Annealing Algorithm", fontsize=10)
    plt.xlabel('Root mean square error')
    plt.ylabel('time (s)')
    plt.show()


    # plt.plot(y, y - modele_reg.predict(x), '.')
    # plt.show()


regression_sa()
regression_2opt()