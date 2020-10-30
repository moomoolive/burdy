[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/made-with-vue.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://github.com/moomoolive/burdy)

# Burdy
Voice of customer software 

Inspiration for name:

> is a little burdy to tell you what your customers are saying; without you moving an inch. 

In a nutshell, burdy goes to amazon.ca to find interesting 'copy-worthy' statements from amazon reviews. It uses a scraper to gather the reviews, then performs sentimental analysis on the reviews. After that, it shows you all the scaped reviews under their relavent categories, and allows you to export it to a csv format.

Originally meant to be commericial software, but for various reasons isn't viable anymore. So, because of that I've open-sourced it, perhaps it may help someone out.

Burdy a web-based application, using Vue for frontend and python-based backend microservices. Backend microservices are connected via a Docker Network.

Microservices:
* Authentication/Entry point API: This one is pretty obvious. All authentication and user information interaction were made here, and frontend would access this API ONLY. This API would then forward requests to other microservices if neccessary. This API was build with Flask.

* Scraper: built with the scrapy library and turned into a API thanks to the generous help of the contributors at [scrapyrt](https://scrapyrt.readthedocs.io/en/stable/) library. The scraper's role was to go to an inputted product on amazon.ca and scrape your desired amount of reviews.

* Tensorflow Prediction API: the role of this microservice was to take all scraped amazon reviews and classify them into classes that may be useful to a copywriter. Look at classifications PDF if you're interested. This was a Flask Based API, and housed a custom-made Tensorflow ML Algorithim. 

Use any of the code at your liking, and if you have any questions just send me message.