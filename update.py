import base64
from PIL import Image
from io import BytesIO
import json
import sqlite3
import pandas as pd


#path = "/var/www/aspendb/probesearch/SensorsData/Data-Store_backup.db"
path = "/var/www/aspendb/probesearch/SensorsData/Data-Store.db"

def readSqlite(query):
    conn = sqlite3.connect(path)
    df = pd.read_sql_query(query, conn)
    return df
    
    
def saveSqlite(query):
    conn = sqlite3.connect(path)
    try:
        conn.execute(query)
        conn.commit()
        conn.close()
        return 1
    except:
        return 0 
        
def get_brightness(data):
    # Decoding the base64 encoded string
    img_data = base64.b64decode(data)
    # Opening the decoded image data using PIL
    img = Image.open(BytesIO(img_data)).convert('L')
    hist = img.histogram()
    brightnessval = sum(i * hist[i] for i in range(256)) / (img.size[0] * img.size[1])
    return round(brightnessval,2)
    
    
#df = readSqlite("select * from blackbox where brightness is NULL")
'''df = readSqlite("select * from wendy_king where brightness is NULL")
print(df.head())


id_ = list(df["ImgRef"])
imageList = list(df["image"])


for i in range(len(id_)):
    brightness = get_brightness(imageList[i])
    query = "UPDATE blackbox set brightness={} where ImgRef='{}'".format(brightness,id_[i])
    saveSqlite(query)'''
    
    
    
query = '''CREATE TABLE "lilli_speight" (
	"Humidity"	NUMERIC,
	"IPAddress"	TEXT,
	"ImgRef"	TEXT,
	"Motion"	INTEGER,
	"Temperature"	NUMERIC,
	"timestamp"	TEXT,
	"flag"	INTEGER,
	"image"	,
	"location"	INTEGER,
	"brightness"	NUMERIC
)'''

#query = "drop table lilli_speight"

#print(saveSqlite(query))
print(readSqlite("select * from sonya_cummings" )[["Humidity","location","IPAddress","Temperature"]])