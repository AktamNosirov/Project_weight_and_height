from numpy import result_type
from read_data import read_csv_data
from get_data import get_data
import matplotlib.pyplot as plt

def show(gender, weight, height):
    """
    Show data.
    Args:
        gender(list): 0 and 1
        weight(list): weight
        height(list): height
    Returns:
        None
    """
    w_male = []
    w_female = []
    h_male = []
    h_female = []
    
    #WRITE YOUR CODE HERE
    for i in range(len(gender)):
        if gender[i]==0:
            w_male.append(weight[i])
            h_male.append(height[i])
        if gender[i]==1:
            w_female.append(weight[i])
            h_female.append(height[i])
    plt.scatter(h_male,w_male,c="black", label="male")
    plt.scatter(h_female,w_female,c="red",label="female")
    
    return plt.show()
    
data = read_csv_data('data/weight-height.csv')
gender, weight, height = get_data(data)

show(gender, weight, height)