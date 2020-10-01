[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/made-with-vue.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://github.com/moomoolive/burdy)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://github.com/moomoolive/burdy)
# Burdy
Voice of Customer Software

This is a git repository for all things related to the Burdy.

The 'Enviroment' folder is a folder that contains the virtual enviroment you will need to develop the script. I used virtualenv to create it.

Idea_testing_code is a folder where I try any relevant ideas to the software, like libraries, make prototypes for main program script.

The main_program_loop is as clear as day - it's the actual script that will be used in the back-end insha'Allah. DO NOT ADD TO THE SCRIPT THERE UNLESS YOU'RE COMPLETELY SURE IT WILL BE IN THE PROGRAM. 


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
