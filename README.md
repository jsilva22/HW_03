# HW03: Ebay Scraping
I. What does my ebay-dl.py program do?

Essentially, my program is collecting lots of different information from ebay depending on the item I'm searching for. In ebay, a search bar appears for you to search for the item you're interested in buying. Similarly, when I run my program I give it a search item so that it knows what item I want to focus on from ebay. In addition to giving it a search item, I also specify the number of pages I want it to go until as if it were on the ebay website. So if I give it 10 pages then I will get the information from the first 10 pages of ebay of whatever item I'm looking for. It's also important to note that I give my program the url for ebay and it will switch as I give it a different search item and as it loops through different pages. My program downloads the url using the request function and from there turns it into html so that I can then use a library called Beautiful soup that is used to extract data. Beautiful soup pulls out data from html files which is why I had to turn the information from the url into an html first before extracting any info. Again just to reiterate, when I say my program downlaods the url I mean that it's downloading the information from lets say the first 10 pages of ebay from the item I'm searching for. Among the various kinds of information that can be found on ebay pages, the information that my program specifically looks at and acquires are: the exact name of the item(if I search marker for example I'll see marker products but the exact names will be different), the price of the item, the status(or condition) of the item, the cost to ship the item, whether or not I can return the item for free, and lastly the number of sells the owner has made(or in other words the items sold). However, it takes a little bit of work to find this information because there are all sorts of other information from the ebay pages my program downloads. So, I go to the ebay page and find which css selectors seem to be associated with for example the item price if that's what I want to look at first. One I find the correct selector, my program then knows which section of my information to look at and will extract the information I'm interested in into a list where each entry is a dictionary with the keys being the 6 different kinds of information I mentioned above. After collecting this info, my program then usies the json library to save the list as either a json file or csv file if I use the csv command that I added and have explained below how to use.

II. How to run my ebay-dl.py file

This is the code needed to run my file and I want to emphasize that the main things we need are to just add a search item with '' around the word so that searches with two words like stuffed animals can work. The the other thing is the number of pages which in this case is 10. The following code is how to run my file and are the exact examples I used for my three items.
```
python3 ebay-dl.py 'marker'  --num_pages=10
python3 ebay-dl.py 'eraser'  --num_pages=10
python3 ebay-dl.py 'pencil sharpener'  --num_pages=10
```
I also added the csv flag which all it does is that instead of converting my list of dictionaries to a json file, my list with every entry as being a dictionary instead gets turned into a csv file. Here is the code for that:
```
python3 ebay-dl.py 'marker' --csv  --num_pages=10
python3 ebay-dl.py 'eraser' --csv  --num_pages=10
python3 ebay-dl.py 'pencil sharpener' --csv  --num_pages=10
```
For anyone interested in doing their own search to get either a json file or csv file here is the general format:
```
python3 ebay-dl.py 'item_of_interest'  --num_pages=desired_pages
python3 ebay-dl.py 'item_of_interest' --csv  --num_pages=desired_pages
```

Lastly, if you need a refresher on what the project details are or want to start all over again click [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)!
