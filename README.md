[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/made-with-vue.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://github.com/moomoolive/burdy)
# Burdy
Voice of customer software ==> is a little burdy to tell you what your customers are saying; without you moving an inch.

This is a web-based application, using Vue(Javascript) in the front-end and Flask(Python) in the back-end.

In a nutshell, burdy goes to amazon.ca to find interesting 'copy-worthy' statements from amazon reviews. It uses a scraper to gather the reviews, then performs sentimental analysis on the reviews.

Sentimental analysis is done with a custom-made Tensorflow machine learning Algorithm. The weights and data of the model are too big to upload to Github tho.

Feel free to use any of the code at your own liking - hope it helps you out.

The 'Enviroment' folder is a folder that contains the virtual enviroment you will need to develop the script. I used virtualenv to create it.