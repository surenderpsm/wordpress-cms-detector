# WordPress CMS Detector
This Python Script makes use of web-scraping to detect if a given domain is hosted by a WordPress CMS
## Dependencies to be installed
Install BeautifulSoup library and a HTML parser
### `python3 -m pip install bs4`
### `pip3 install html5lib`
## Run the script
Go to the directory of the script and type
### `python code.py`
## How it works?
. The script uses the idea that `wp-content` tags are very prevelant in WordPress Website source pages.
. Additionally, the `robots.txt` is also scanned for `wp-*` and `*-wp` tags to check for WordPress signs if the above method fails.
