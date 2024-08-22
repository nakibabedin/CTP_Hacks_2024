import firebase

def getJaccardSimilarity(target_keywords, resource_keywords):
    target_set = set(target_keywords)
    resource_set = set(resource_keywords)

    common_elements = target_set.intersection(resource_set)
    all_elements = target_set.union(resource_set)

    # return the Jaccard Similarity to 3 decimal places
    return int( len(common_elements) / len(all_elements) * 1000 ) / 1000

# rank relevant resources
# return: a list of resource objects in descending order of correlation with target_keywords
def rank_resources(campus, target_keywords, amount_desired):
    resources_for_campus = firebase.get_data_for_campus(campus) 
    resources_cunywide = firebase.get_data_for_campus('CUNY')
    
    rankings = []

    for resource in resources_for_campus:
        resource_keywords = resource['keywords']
        current_jaccard_similarity = getJaccardSimilarity(target_keywords, resource_keywords)
        