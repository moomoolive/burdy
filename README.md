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

> is a little burdy to tell you what your customers are saying; without you moving > an inch. 

Originally meant to be commericial software, but for various reasons isn't viable anymore.

This is a web-based application, using Vue for frontend and python-based backend microservices.

Microservices:
* Scraper: Built with the scrapy library, and turned into a API thanks to the generous help of the [scrapyrt](https://scrapyrt.readthedocs.io/en/stable/) library. 
* Authentication/Entry point API:
* Tensorflow Prediction API:

In a nutshell, burdy goes to amazon.ca to find interesting 'copy-worthy' statements from amazon reviews. It uses a scraper to gather the reviews, then performs sentimental analysis on the reviews.

Sentimental analysis is done with a custom-made Tensorflow machine learning Algorithm. The weights and data of the model are too big to upload to Github tho.

Feel free to use any of the code - hope it helps you out.