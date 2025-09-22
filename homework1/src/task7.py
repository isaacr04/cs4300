import requests
from bs4 import BeautifulSoup

# GET requests example.com and parses first <p> element to display as plain text
def request_example():
    r = requests.get("http://example.com/get")
    parser = BeautifulSoup(r.text, "html.parser")
    print(parser.p.text)


if __name__ == '__main__':
    request_example()