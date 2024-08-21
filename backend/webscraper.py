import requests

# given a url, will extract its HTML contents
def get_html_contents(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to extract the html contents for {url}: {e}")
        return None


# print( get_html_contents("https://www.cuny.edu/current-students/student-affairs/student-services/counseling/") )