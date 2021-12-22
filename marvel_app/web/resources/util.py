from urllib.parse import urlparse

def get_id_from_url(url):
    # http://gateway.marvel.com/v1/public/comics/21366
    url_parse = urlparse(url)
    id = url_parse.path.split('/')[-1]
    return id

def add_id(dict_val, url_attribute, url_internal=None):
    for item in dict_val:
        item['id'] = get_id_from_url(item[url_attribute])
        #item['url'] = url_internal.format(get_id_from_url(url_attribute)) 
    
    return dict_val
