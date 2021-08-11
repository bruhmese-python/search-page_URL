# search-page_URL.py
Generate `google`/`yahoo`/`bing`/`Aol`/`duckduckgo`/`yandex`/`wolfram`/`lycos`/`ask`/`excite` searchpage URLs from search string.

            ‎

| Search string | "Hey watchu doin" *("Plain search text")* |
| ------------- | ------------- |

            ‎

| Search Engine  | URL |
| ------------- | ------------- |
| Google  | "https://www.google.com/search?q=Hey+whatchu+doin"  |
| bing  | "https://www.bing.com/search?q=Hey+whatchu+doin" |
| Aol  | "https://search.aol.co.uk/aol/search?q=Hey+whatchu+doin&s_it=aoluk-homePage100&s_chn=hp&rp=&s_qt=ac&t=h_&ia=images"  |
| and so on..| |

##  Prerequisites

- Python 3+
- *(OPTIONAL)* : Any webscraping library like BeautifulSoup 

##  Practical Usage with BeautifulSoup library

```Python

import requests
from bs4 import BeautifulSoup
import searchpage       #Download searchpage.py to your working directory

URL = search.google("Hey whatchu doin")
#     search.aol("Hey whatchu doin")
#     search.wolfram("Hey whatchu doin")
#     search.ask("Hey whatchu doin")
#     search.(...(" ... "))
response = requests.get(URL)
content = BeautifulSoup(response.text, "html.parser")
print(content)

```
