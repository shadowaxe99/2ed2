```python
import firebase_admin
from firebase_admin import firestore

# Initialize Firestore DB
db = firestore.client()

def match_brands():
    # Fetch all influencers and brands from Firestore
    influencers_ref = db.collection('influencers')
    brands_ref = db.collection('brands')

    influencers = influencers_ref.get()
    brands = brands_ref.get()

    # Convert documents to dictionaries
    influencers_list = [doc.to_dict() for doc in influencers]
    brands_list = [doc.to_dict() for doc in brands]

    # Initialize matches dictionary
    matches = {}

    # Iterate over each influencer
    for influencer in influencers_list:
        # Initialize match score dictionary for each influencer
        match_scores = {}

        # Iterate over each brand
        for brand in brands_list:
            # Calculate match score based on profiles and preferences
            match_score = calculate_match_score(influencer, brand)

            # Add match score to match_scores dictionary
            match_scores[brand['name']] = match_score

        # Sort match_scores dictionary by score in descending order
        sorted_match_scores = dict(sorted(match_scores.items(), key=lambda item: item[1], reverse=True))

        # Add top 3 matches to matches dictionary
        matches[influencer['name']] = list(sorted_match_scores.keys())[:3]

    return matches

def calculate_match_score(influencer, brand):
    # Initialize match score
    match_score = 0

    # Compare influencer and brand categories
    common_categories = set(influencer['categories']).intersection(set(brand['categories']))
    match_score += len(common_categories)

    # Compare influencer and brand target demographics
    common_demographics = set(influencer['target_demographics']).intersection(set(brand['target_demographics']))
    match_score += len(common_demographics)

    # Compare influencer and brand preferred social platforms
    common_platforms = set(influencer['preferred_platforms']).intersection(set(brand['preferred_platforms']))
    match_score += len(common_platforms)

    return match_score
```