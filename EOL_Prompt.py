#https://endoflife.date/docs/api - website for API 
import requests
import pandas as pd
import os

##Get full list of softwares from API
response2 = requests.get("https://endoflife.date/api/all.json")
data2 = response2.json()
print(data2)

#Prompts
software = input("Please input the software you want to view End Of Life for: ")
final = ("https://endoflife.date/api/" + software + ".json")

#Get specific software EOL data from API
response = requests.get(final)
data = response.json()

##Locates the folder
folder_path = '/Users/admin/Desktop/Data Analytics/Software EOL Data'  # This is a direct path; adjust it as needed
filename = software + '.xlsx'
full_path = os.path.join(folder_path, filename)

import os
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

##Output into Excel and save into Folder above
df = pd.DataFrame(data)
writer = pd.ExcelWriter(full_path, engine='xlsxwriter')
df.to_excel(writer, sheet_name=software, index=False)
writer.save()