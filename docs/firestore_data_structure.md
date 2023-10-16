# Firestore Data Structure

This document describes the data structure and schema of the Firestore database used in the `match_brands` function in the `cloud_functions/functions.py` file. The Firestore database contains two main collections: `brands` and `influencers`.

## Brands Collection

Each document in the `brands` collection represents a brand and has the following fields:

- `brand_id` (string): The unique identifier for the brand.
- `brand_name` (string): The name of the brand.
- `preferences` (map): A map containing the brand's preferences for matching with influencers. The keys are the preference categories (e.g., `age`, `location`, `interests`), and the values are the preferred values for each category.

## Influencers Collection

Each document in the `influencers` collection represents an influencer and has the following fields:

- `influencer_id` (string): The unique identifier for the influencer.
- `influencer_name` (string): The name of the influencer.
- `profile` (map): A map containing the influencer's profile information. The keys are the profile categories (e.g., `age`, `location`, `interests`), and the values are the influencer's values for each category.

## Matching Process

The `match_brands` function uses the data from these collections to match brands with influencers. The function fetches the brand's preferences and the influencer's profile, compares them, and calculates a matching score based on the similarity between the preferences and the profile. The function then returns a list of influencers sorted by their matching scores.

For more details on the matching algorithm and its enhancements, please refer to the `match_brands_design_document.md` and `match_brands_api_documentation.md` files.