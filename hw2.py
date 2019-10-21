##1. Create a DataFrame from a URL that points to a CSV file. 

import pandas as pd

def download_to_csv(url):
    
    df = pd.read_csv(url)   
    return df 

##2. Create a function that takes a pandas df AND a list of columns name as input. 
def test_create_dataframe(df,columns):
    # condition1: there are at least 10 rows in the DataFrame
    # condition2: The values in each column have the same python data type
    # condition3: The dataframe contains only the columns that you specified as the second argument 
    if  len(df) >= 10 and df.equals(df.dtypes) and  sorted(df.columns)==sorted(columns):
        return True
    return False 

### test case 

### Uncomment it if you need to test the module 

# url='https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
# columns=['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']
# df=download_to_csv(url)
# test_create_dataframe(df,columns)


