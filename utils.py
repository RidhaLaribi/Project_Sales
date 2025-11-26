import pandas as pd
import numpy as np



def generate_month_for_year(start_date,end_date):
    
   return pd.date_range(start=start_date, end=end_date, freq='MS')

def generate_random_seles(min_value, max_value, size):
    return np.random.randint(min_value, max_value, size)
   









