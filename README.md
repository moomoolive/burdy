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

## Structure

```bash
├── README.md               # This file
├── burdy_enviroment/
    ├── enviromental_requirements.txt
    └── pyvenv.cfg
└── data_collection/
    ├── __pycache__/     
        ├── opinion_unit_devider.cpython-38.pyc
        └── opinion_unit_divider.cpython-38.pyc 
    ├── amazon_canada_scraper/     
        ├── scrapy.cfg
        ├── amazon_canada_scraper/
            ├── __init__.py
            ├── items.py
            ├── middlewares.py
            ├── pipelines.py
            ├── settings.py
            ├── __pycache__/
                ├── __init__.cpython-38.pyc  
                └── settings.cpython-38.pyc
            └── spiders/
                ├── __init__.py 
                ├── amazon_canada_scraper.py
                ├── opinion_unit_divider.py 
                ├── preprocess.py 
                └── __pycache__/
                    ├── __init__.cpython-38.pyc 
                    ├── amazon_canada_scraper.cpython-38.pyc
                    ├── opinion_unit_divider.cpython-38.pyc
                    └── preprocess.cpython-38.pyc 
        └── logs/ burdy_scraper/
```
