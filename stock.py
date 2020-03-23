from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import json
from os import path
from plyer import notification
import time

def sendNotification(title, msg):
	notification.notify(
	title = title,
	message = msg,
	timeout = 3   #how much seconds the notification should be dispalyed
	)


url = "https://www.moneycontrol.com/stocksmarketsindia/"

while True:
	r = requests.get(url) 
	soup = BeautifulSoup(r.content , 'html5lib')
	table = soup.find( "table", {"class":"mctable1"} )

	rows = list()
	for row in table.findAll("tr"):
		rowContent = re.split('\n\t +', row.get_text())
		rows.append(rowContent[1:5])

	currDf = pd.DataFrame(rows[1:], columns = rows[0]) 
	print("Current prices are ")
	print(currDf)

	currentDataJson = currDf.to_json()

	if path.exists("stocks.json"):
		with open("stocks.json", "r") as f:
			oldDataJson = json.load(f) 
		oldDf = pd.DataFrame(oldDataJson)
		
		for i in range(0,currDf.shape[0]):
			if(float(oldDf["Price"][i]) != float(currDf["Price"][i])):
				if(float(oldDf["Price"][i]) > float(currDf["Price"][i])):
					print(f'Price of {currDf["Index"][i]} decreased from {oldDf["Price"][i]} to {currDf["Price"][i]}')
					sendNotification('Price decreased', f'{currDf["Index"][i]} :  {oldDf["Price"][i]} ==> {currDf["Price"][i]}')
				else:
					print(f'Price of {currDf["Index"][i]} increased from {oldDf["Price"][i]} to {currDf["Price"][i]}')
					sendNotification('Price increased', f'{currDf["Index"][i]} :  {oldDf["Price"][i]} ==> {currDf["Price"][i]}')
				time.sleep(5)  #wait for 5 seconds
	with open("stocks.json", "w") as f:
		f.write(currentDataJson)
		
	#time.sleep(600) #uncomment this if data is to be updated every 10 minutes
	
