# %%
import pandas as pd

## CONSTANTS
DELIMITER_STR = ' '
MULTI_DELIMITER_STR = ',|;'



## data prep
df = pd.DataFrame({
                  'concat_addr':
                 [
                  '34, Brighton Street, Darkwood', 
                  '542, Oak Ave; Sanctuary', 
                  '21A Shassar Street, Zultun', 
                  '1267 ; Madison Ave, Stormpoint',
                  '6745, Westmarch Ave'
                 ]
                })
df




# %%
df2 = df['concat_addr'].str.partition(DELIMITER_STR)[[0, 2]].rename({0: 'HouseNo', 2: 'Address'}, axis=1)
df2
# %%



df3 = df['concat_addr'].str.split(MULTI_DELIMITER_STR,expand=True).add_prefix('addr_')
df3
# %%
