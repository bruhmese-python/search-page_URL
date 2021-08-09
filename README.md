# search-page_URL.py
Generate `google`/`yahoo`/`bing`/`Aol`/`duckduckgo`/`yandex`/`wolfram`/`lycos`/`ask`/`excite` searchpage URLs from search string.


"Hey watchu doin" *("Plain search text")*

👇

| Search Engine  | URL |
| ------------- | ------------- |
| Google  | "https://www.google.com/search?q=Hey+whatchu+doin"  |
| bing  | "https://www.bing.com/search?q=Hey+whatchu+doin" |
| Aol  | "https://search.aol.co.uk/aol/search?q=Hey+whatchu+doin&s_it=aoluk-homePage100&s_chn=hp&rp=&s_qt=ac&t=h_&ia=images"  |
| and so on..| |


##  Practical Usage with BeautifulSoup library

```Python

import requests
from bs4 import BeautifulSoup
import searchpage

URL = searchpage.search.google("Hey whatchu doin")
response = requests.get(URL)
content = BeautifulSoup(response.text, "html.parser")
print(content)

```