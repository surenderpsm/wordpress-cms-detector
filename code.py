from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
import urllib.error


# Final function to check if WordPress CMS
#   Returns True if the page is detected to be running on WordPress CMS
#   Returns False otherwise
def check_wordpress_cms(page_url):
    try:
        if check_source(page_url) or check_robots_file(page_url):
            return True
    except urllib.error.HTTPError as e:
        raise e  
    except urllib.error.URLError as e:
        raise e

# Helper Functions

# Get Webpage content. 
# Returns a bytes object containing content of the webpage
# if an exception is encountered appropriate message is printed and None object is returned
def get_webpage_content(page_url):
    # added header attribute to bypass security feature of being a bot
    request = Request(url=page_url, headers={'User-Agent':'Mozilla/5.0'})
    # return the content of the webpage
    try:
        content = urlopen(request).read()
        return content
    # Return None if an HTTP 404 error is encountered
    except urllib.error.HTTPError as e:
        # print("debug: HTTP 404 Error")
        raise Exception("HTTP 404")
    except urllib.error.URLError as e:
        # print("debug: Unknown error encountered")
        raise e
    return None


# robots.txt is a file which is accessed by search engines to access the sitemap of the webpage
# Checks robots.txt for signs for WordPress CMS
def check_robots_file(page_url):
    page_url = page_url+'robots.txt'
    content = get_webpage_content(page_url)
    if(content):
        soup = BeautifulSoup(content, 'html5lib')
        # Regex to match "wp-" or "-wp" which is a sign that the CMS is WordPress
        if(soup.find(string=re.compile("(?:wp-)|(?=.-wp)"))):
            # print("debug: found via robots")
            return True
    return False


# checking the source file for signs of WordPress CMS
def check_source(page_url):
    content = get_webpage_content(page_url)
    if(content):
        soup = BeautifulSoup(content, 'html5lib')
        # Regex to match "wp-" or "-wp" which is a sign that the CMS is WordPress
        if soup.find(src=re.compile("(?:wp-)")):
            # print('debug: found via source')
            return True
    else:
        print("ERROR: The webpage was not found")
        return False

print("\n################################################## WordPress CMS Detector Script ########################################################")
print("# This script checks if a given domain utilises WordPress CMS.                                                                          #")
print("# The script uses the idea that \"wp-content\" tags are very prevelant in WordPress Website source pages.                                 #")
print("# Additionally, the robots.txt is also scanned for \"wp-*\" and \"*-wp\" tags to check for WordPress signs if the above method fails.       #")
print('#########################################################################################################################################')

domain = input("\n\nInput the domain: ")
page_url = "https://" + domain + "/"
try:
    if(check_wordpress_cms(page_url)):
        print("Yes")
    else:
        print("No")
except urllib.error.HTTPError:
    print("ERROR : HTTP 404 - page not found")
except urllib.error.URLError:
    print("ERROR : URL error encountered")
