import urllib.request
# place your code to clean up the data file below.
import urllib.parse
parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant/')
print(parse_url)
print("\n")
unparse_url = urlunparse(parse_url)
print(unparse_url)

def munge():
    request_url = urllib.request.urlopen('https://data.cityofnewyork.us/City-Government/Capital-Budget/46m8-77gv/data')
    print(request_url.read())

if __name__ == '__main__':
    munge()
