# Basic GET Request

import requests # pip install requests

# Lets say we want the text from a website for this example ill use google.com

resp = requests.get("google.com") # Resp is variable name aka data store. requests is module we are using. get is type of method we want to send and in brackets is the link
# theres many additions to this what can be seen on the documentation
# https://docs.python-requests.org/en/latest/
print(resp.text) # resp mentioning variable. Then we get .text which is text of website and will display this to screen.
