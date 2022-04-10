import pandas as pd
data=pd.read_csv(r'D:\repository\CapstoneProject\datasets\cc fraud short\bsNET140513_032310.csv')
df=pd.DataFrame(data, columns=['Source','fraud'])
print(df)
