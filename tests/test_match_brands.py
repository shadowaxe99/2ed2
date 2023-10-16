```python
import unittest
from cloud_functions.functions import match_brands

class TestMatchBrands(unittest.TestCase):

    def setUp(self):
        self.influencer_profile = {
            'name': 'Influencer A',
            'interests': ['fashion', 'technology', 'travel'],
            'followers': 5000
        }
        self.brand_profile = {
            'name': 'Brand A',
            'industry': 'fashion',
            'budget': 10000
        }

    def test_match_brands(self):
        result = match_brands(self.influencer_profile, self.brand_profile)
        self.assertIsInstance(result, dict)
        self.assertIn('match_score', result)
        self.assertIn('match', result)

    def test_match_brands_no_match(self):
        self.brand_profile['industry'] = 'automotive'
        result = match_brands(self.influencer_profile, self.brand_profile)
        self.assertEqual(result['match'], False)

    def test_match_brands_perfect_match(self):
        self.influencer_profile['interests'] = ['fashion']
        result = match_brands(self.influencer_profile, self.brand_profile)
        self.assertEqual(result['match'], True)
        self.assertEqual(result['match_score'], 1.0)

if __name__ == '__main__':
    unittest.main()
```