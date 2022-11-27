#!/usr/bin/env python3

import pandas as pd

"""
Write function cities() that returns the following
DataFrame of top Finnish cities by population:

                 Population Total area
Helsinki         643272     715.48
Espoo            279044     528.03
Tampere          231853     689.59
Vantaa           223027     240.35
Oulu             201810     3817.52
"""

def cities():
    city_data =  {
            'Population':[643272, 279044, 231853, 223027, 201810],
            'Total area':[715.48, 528.03, 689.59, 240.35, 3817.52]
            }

    city_index = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']

    cities_dataframe = pd.DataFrame(city_data, index=city_index)
    cities_dataframe = cities_dataframe.sort_values(by=['Population'], ascending=False)

    return cities_dataframe
    
def main():
    city_data = cities()
    print(city_data)
    
if __name__ == "__main__":
    main()
