import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Styling
plt.style.use('seaborn-whitegrid') 


mydb = sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://NadyaSaffira:12345@localhost:3306/world'
)
Q_ASEAN = "select Name as Negara_ASEAN, SurfaceArea as Luas_Daratan from country where Name in ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam') order by Name;"
ASEAN = pd.read_sql(Q_ASEAN, mydb)

# print(ASEAN.head())
plt.figure('Persentase Luas Daratan ASEAN')

ax,labels, autotexts = plt.pie(
    ASEAN['Luas_Daratan'], labels=ASEAN['Negara_ASEAN'], autopct='%1.1f%%', 
    textprops={'fontsize': 10},
    labeldistance=1.07
)
for autotext in autotexts:
    autotext.set(color='white', fontsize=8)
    
plt.title('Persentase Luas Daratan ASEAN')
plt.tight_layout()
plt.show()