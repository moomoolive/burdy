import unittest
import requests

## dev server must be turned on

class testMainRoutes(unittest.TestCase):

    def test_home(self):
        r = requests.get('http://localhost:5000/')
        self.assertEqual(r.status_code, 200)

    def test_review_mine(self):
        data = {'url': 'https://www.amazon.ca/Echo-Dot-3rd-gen-Charcoal/product-reviews/B07PDHT5XP/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1'}
        r = requests.post('http://localhost:5000/review_mine', data)
        values = 0
        keys = []
        for key, value in r.text:
            keys.append(key)
            values += len(value)
        self.assertEqual([0,1,2,3], keys)
        self.assertEqual(130, values)

if __name__ == '__main__':
    unittest.main()
