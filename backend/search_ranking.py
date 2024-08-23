import firebase
import heapq

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
    total_resources = resources_for_campus | resources_cunywide

    rankings = []

    print(total_resources.items())

    for resource_name, resource in total_resources.items():
        # find Jaccard similarity
        resource_keywords = resource['keywords']
        current_jaccard_similarity = getJaccardSimilarity(target_keywords, resource_keywords)

        # only find top-amount_desired resources by using heap
        heapq.heappush(rankings, (current_jaccard_similarity, resource_name, resource))

        if len(rankings) == amount_desired:
                    heapq.heappop(rankings)


    # since rankings is sorted as the minimum similarity having the most priority,
    # append to result by traversing from the end to beginning of rankings
    result = [x[2] for x in rankings[::-1]]
    
    return result

