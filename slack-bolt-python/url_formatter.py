import requests
import re
pub="pub"
auth="author"
def formaturl(url):
    if re.match(".*aws12[25].organization.com$", url) or re.match(".*corp.organization.com$", url):
        if not re.match('(?:http)://', url):
            if pub in url:
                return f"http://{url}:8080/services/systemcheck"
            elif auth in url:
                if re.match(".*corp.organization.com$", url):
                    return f"https://{url}/services/systemcheck"
                else:
                    return f"http://{url}:4502/services/systemcheck"
    return url
x=formaturl(page)
y=requests.get(x)
print(y.text)
