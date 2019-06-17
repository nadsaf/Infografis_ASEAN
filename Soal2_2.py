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
Q_ASEAN = "select c.Name as Negara_ASEAN, c.Population as Populasi_Negara, c.GNP, k.Name as Ibukota, k.Population as Populasi_Ibukota from country c, city k where c.Capital = k.ID and c.Name in ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam') order by c.Name"
ASEAN = pd.read_sql(Q_ASEAN, mydb)

plt.figure('Persentase Populasi ASEAN')

ax,labels, autotexts = plt.pie(
    ASEAN['Populasi_Negara'], labels=ASEAN['Negara_ASEAN'], autopct='%1.1f%%', 
    textprops={'fontsize': 10},
    labeldistance=1.05
)

for autotext in autotexts:
    autotext.set(color='white', fontsize=8)

plt.title('Persentase Penduduk ASEAN')
plt.tight_layout()
plt.show()