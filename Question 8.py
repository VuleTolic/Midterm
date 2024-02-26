from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

url_to_check = "https://blackboard.ie.edu/ultra/courses/_79431_1/outline/file/_1264693_1"
if is_valid_url(url_to_check):
    print(f"{url_to_check} is a valid URL.")
else:
    print(f"{url_to_check} is not a valid URL.")
