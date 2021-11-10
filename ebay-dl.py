import argparse
import requests
from bs4 import BeautifulSoup
import json



def parse_itemssold(text):

    '''
    Takes as input a string and returns the number of items sold, as specified in the string
    
    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0


def parse_shippingcost(text):

    '''
    >>> parse_shippingcost('+$8.49 shipping')
    849
    >>> parse_shippingcost('Free 3 day shipping')
    0
    
    '''
    
    shipping_cost = ''
    if 'Free' in text and 'shipping' in text:
        return 0
    else:
        for char in text:
            if char in '1234567890':
                shipping_cost += char
        return int(shipping_cost)

def parse_itemcost(text):

    '''
    >>> parse_itemcost('$8.49')
    849
    >>> parse_itemcost('$50.00')
    5000
    >>> parse_itemcost('$150.50')
    15050
    >>> parse_itemcost('$21.92 to $179.05')
    2192
    
    '''
    
    item_cost = ''
    updated_text = text.split()
    important_text = updated_text[0]
    for char in important_text:
        if char in '1234567890':
            item_cost += char
    return int(item_cost)



if __name__ == '__main__':

    #get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10)
    parser.add_argument('--csv', action="store_true")
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    #list of all items found in all ebay webpages
    items = []

    #loop over ebay webpages
    for page_number in range(1,int(args.num_pages)+1):
        
        #build the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url += args.search_term 
        url += '&_sacat=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
        print('url=', url)
     
        #download the html
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        tags_items = soup.select('.s-item')
        for tag_item in tags_items:
            #print('tag_item=', tag_item)
            
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text


            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True


            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness, .s-item__additionalItemHotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)
                print('tag=', tag)

            status = None
            tags_name = tag_item.select('.s-item__subtitle')
            for tag in tags_name:
                status = tag.text

            shipping_cost = None
            tags_shippingcost = tag_item.select('.s-item__logisticsCost, .s-item__shipping, .s-item__freeXDays')
            for tag in tags_shippingcost:
                shipping_cost = parse_shippingcost(tag.text)

            item_cost = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                item_cost = parse_itemcost(tag.text)

            item = {
                'name' : name,
                'item_cost' : item_cost,
                'status' : status,
                'shipping_cost' : shipping_cost,
                'free_returns' : freereturns,
                'items_sold': items_sold,
            }
            items.append(item)


        #print('len(tags_items)=', len(tags_items))

        #print('len(items)=', len(items))

        for item in items:
            print('item=', item)

    # write the json to a file
    if args.csv:
        filename = args.search_term + '.csv'
    else:
        filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))
    