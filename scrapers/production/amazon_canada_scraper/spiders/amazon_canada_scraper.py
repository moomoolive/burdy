from __future__ import absolute_import

import scrapy
from .preprocess import preprocess_review

class Amazon_review_spider(scrapy.Spider):

    name = "burdy_production"  
    start_urls = [
        "https://www.amazon.ca/Echo-Dot-3rd-gen-Charcoal/product-reviews/B07PDHT5XP/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
    ]    

    def parse(self, response): 
        for review in response.css('div.review'):
            opinion_units = preprocess_review(
                    review_headline=review.css('div.a-row a.review-title span::text').get().replace('<br>', ' '),
                    review_body=review.css('div.a-row.a-spacing-small.review-data span span').get()[9:-8].replace('<br>', ' '), 
                    )
            for opinion_unit in opinion_units:
                yield{
                    'Opinion Unit' : opinion_unit
                }