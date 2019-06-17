import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Styling
sns.set(style='whitegrid')    


mydb = sqlalchemy.create_engine(
    # namaDBsys://user:pass@host:port/namaDatabase
    'mysql+pymysql://NadyaSaffira:12345@localhost:3306/world'
)
Q_ASEAN = "select Name as Negara_ASEAN, Population as Populasi from country where Name in ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam') order by Name;"
ASEAN = pd.read_sql(Q_ASEAN, mydb)
# print(ASEAN.info())

plt.figure('Populasi ASEAN', figsize=(10,6))
ax1 = sns.barplot('Negara_ASEAN', 'Populasi', data = ASEAN, palette="cubehelix")

ax1.set_xlabel('Negara', fontsize=12)
ax1.set_ylabel('Populasi (x100jt jiwa)', fontsize=12)
ax1.set_xticklabels(ASEAN['Negara_ASEAN'],rotation=30, fontsize=10)
ax1.set_title('Populasi Negara ASEAN',fontsize=15)

for p in ax1.patches:
    height = p.get_height()
    ax1.text(p.get_x()+p.get_width()/2., height + 0.2, int(height) ,ha="center", fontsize=8)

plt.grid(True)
plt.tight_layout()

plt.show()