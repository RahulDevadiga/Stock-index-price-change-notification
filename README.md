# Stock-index-price-change-notification
Live increase or decrease in the stock index prices are notified

#Installation instructions:
pip install beautifulsoup4
pip install requests
pip install pandas
pip install os
pip install plyer

To run python file
python stock.py --refreshRate [time in seconds]   

#Description
The increase or decrease in the stock market index prices is notified to the user via Desktop notification.
Web scraping is used to scrape the data about the stock index prices. After every 'refreshRate' seconds, the data is scraped. The previously scraped data
which was stored in json format is retrieved. 
The data is converted to Pandas dataframe which can be further used for easy processing in case large data has been scraped.
However, in this case it wasn't required.
Both data are compared and the change if any is notified to the user by using plyer library.
