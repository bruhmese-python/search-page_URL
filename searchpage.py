class search:

    def __new__(self):  # Prevent Instantiation
        return None

    PRE = 0
    POST = 1
    
    #Assigning values
    GOOGLE = ["https://www.google.com/search?q=", ""]
    YAHOO = ["https://in.search.yahoo.com/search?p=",
             "&fr=yfp-t&ei=UTF-8&fp=1"]
    AOL = ["https://search.aol.co.uk/aol/search?q=",
           "&s_it=aoluk-homePage100&s_chn=hp&rp=&s_qt=ac"]
    DUCKGO = ["https://search.aol.co.uk/aol/search?q=", "&t=h_&ia=images"]
    YANDEX = ["https://yandex.com/search/?text=", "&lr=20983"]
    WOLFRAM = ["https://www.wolframalpha.com/input/?i=", ""]
    LYCOS = ["https://search13.lycos.com/web/?q=", ""]
    ASK = ["https://www.ask.com/web?q=", ""]
    EXCITE = ["https://results.excite.com/serp?q=", ""]
    BING = ["https://www.bing.com/search?q=", ""]

    #Single line lambda functions for-each engine
    google = lambda string: search.query(string, search.GOOGLE)
    yahoo = lambda string: search.query(string, search.YAHOO)
    aol = lambda string: search.query(string, search.AOL)
    duckduckgo = lambda string: search.query(string, search.DUCKGO)
    yandex = lambda string: search.query(string, search.YANDEX)
    wolfram = lambda string: search.query(string, search.WOLFRAM)
    lycos = lambda string: search.query(string, search.LYCOS)
    ask = lambda string: search.query(string, search.ASK, separator="%")
    excite = lambda string: search.query(string, search.EXCITE, separator="%")
    bing = lambda string: search.query(string, search.BING)

    #Function to generate query
    def query(string: str, ENGINE, separator: str = "+"):

        string = [string][0].split(' ')
        query_text = ""

        for x in range(len(string)):
            query_text = query_text + string[x] + \
                separator * (int(len(string) > x + 1))

        query_text = ENGINE[search.PRE] + query_text + ENGINE[search.POST]
        return query_text


# EXAMPLE : USAGE WITH BEAUTIFUL SOUP

# import requests
# from bs4 import BeautifulSoup
# import searchpage

# URL = searchpage.search.google("Hey whatchu doin")
# response = requests.get(URL)
# content = BeautifulSoup(response.text, "html.parser")
# print(content)
