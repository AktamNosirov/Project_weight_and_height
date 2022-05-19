import csv
import pathlib

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    result_data = []
    # WRITE YOUR CODE HERE
    with open(file_path, 'r') as f:
        
        reader = csv.reader(f) 
        for row in reader: 
            result_data.append(row)
    return result_data

path=pathlib.Path('data')
file_path = path / "weight-height.csv"

 
print(read_csv_data(file_path))
    
    

   
   
   



