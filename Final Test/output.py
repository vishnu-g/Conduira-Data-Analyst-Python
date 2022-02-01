import glob
import os
import pandas as pd
from sqlalchemy import create_engine, text

folder_name = 'Final Assessment'
file_type = 'csv'
seperator =','
dataframe = pd.concat([pd.read_csv(f, sep=seperator) for f in glob.glob(folder_name + "/*."+file_type)],ignore_index=True)

db_url = "mysql+pymysql://root:root@localhost:13306/data"
engine = create_engine(db_url, pool_size=5, pool_recycle=3600)
conn = engine.connect()

sql_text = text("SELECT _source FROM data JOIN activity_data WHERE data._id = activity_data._id and _score > 742 ORDER BY _source")
result = conn.execute(sql_text)

print(result)
result.export()