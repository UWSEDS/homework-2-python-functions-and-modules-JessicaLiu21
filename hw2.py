##1. Create a DataFrame from a URL that points to a CSV file. 

import pandas as pd

def download_to_csv(url):
    
    df = pd.read_csv(url)   
    return df 

##2. Create a function that takes a pandas df AND a list of columns name as input. 
def test_create_dataframe(df,columns):
    # condition1: there are at least 10 rows in the DataFrame
    if len(df) < 10: 
        return False
    # condition2: The values in each column have the same python tye 
    elif not df.equals(df.dtypes): 
        return False
    # condition3: The dataframe contains only the columns that you specified as the second argument 
    elif set(columns)!=set(df.columns) or len(columns)!=len(df.columns): 
        return False
    else:
        return True
    
### test case 

### Uncomment it if you need to test the module 

# url='https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
# columns=['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']
# df=download_to_csv(url)
# test_create_dataframe(df,columns)


