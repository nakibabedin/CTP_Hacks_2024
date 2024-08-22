import firebase

# rank relevant resources
# return: a list of resource objects in descending order of correlation with target_keywords
def rank_resources(campus, target_keywords):
    resources_for_campus = firebase.get_data_for_campus(campus) 
    resources_cunywide = firebase.get_data_for_campus('CUNY')
    

