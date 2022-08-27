
import Daxes as dxs
from sys import path
import pandas as pd
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')

from pyadomd import Pyadomd

def Query_SSAS(Query):
    query = Query
    conn_str = 'Provider=MSOLAP;Data Source=TXBI-DWA-02\TXBIDB;Catalog=TaxVat_All_in;'
    
    with Pyadomd(conn_str) as conn:
        with conn.cursor().execute(query) as cur:
            df = pd.DataFrame(cur.fetchone(), columns=[i.name for i in cur.description])
            return df





df = pd.DataFrame({'ID':dxs.All_Ids,'Daxes':dxs.All_Daxes})
df.set_index('ID',inplace=True)
#df.head(10)


for i, row in df.iterrows():
    Query_SSAS(row.Daxes).to_csv('Dax_Number_{}.csv'.format(i))






