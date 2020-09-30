# Glasses Bestsellers

scrape all the available glasses from this website and get the product url, product image link, product name and the product price
- https://www.glassesshop.com/bestsellers

## Code style

- This project is written in python 3.
- Use Scrapy.

## Clone/Run app
````
# Clone repo
$ git clone https://github.com/MotazBellah/glasses_shop

# Install all dependencies
$ pip install -r requirements.txt

# Run
$ cd glassesshop
$ scrapy crawl bestsellers -o glasses_bestsellers.csv

````
