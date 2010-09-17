import os
import httplib
import urllib
import urllib2


class JSONResponse(object):
    def __init__(self, response):
        self.json = simplejson.loads(response)
        
    def get_object(self, key):
        return self.get_object_from_json(self.json, key)
        
    def get_object_from_json(self, json, key):
        if json and key and key in json:
            return json[key]


class RestAPI(object):

    def __init__(self, base_url, logger, cache_path=None):
        self.base_url = base_url
        self.logger = logger
        self.cache_path = cache_path
        
        if cache_path:
            try:
                os.makedirs(cache_path)
            except:
                self.cache_path = None
        
    def url2filename(self, url):
        return urllib.quote(url).replace('/', '_')
        
    def encode_key_value(self, key, value):
        if value is None:
            return u''
        elif isinstance(value, int):
            return u'%s=%d&' % (key, value)
        else:
            return u'%s=%s&' % (key, urllib.quote(value.encode('utf-8')))
    
    def make_request(self, url, use_cache=False, user_agent=None):
        self.logger.info('requesting: %s' % url)
        
        # Caching
        cache_file = False
        if use_cache == True and self.cache_path:
            pathname = os.path.join(cache_path, self.url2filename(url))
            if os.path.exists(pathname) is True:
                f = open(pathname, 'r')
                return f.read()
            else:
                cache_file = True
                
        opener = urllib2.build_opener()
        req = urllib2.Request(url)
        if user_agent is None:
            user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.451.0 Safari/534.2'
        req.add_header('User-Agent', user_agent)
        
        try:
            urlfile = opener.open(req)
            data = urlfile.read()
        except urllib2.HTTPError, e:
            return
        except urllib2.URLError, e:
            return
        except httplib.BadStatusLine:
            return self.make_request(url, use_cache, user_agent)
        
        if cache_file == True:
            try:
                f = open(pathname, 'w')
                f.write(data)
            except IOError, e:
                if e.errno == 36:
                    #logging.error('filename too long, probably a problem with the page url')
                    return None
                else:
                    raise
        
        return data
        
    def make_api_call(self, parameters):
        end_url = u'?'
        for key, value in parameters.items():
            end_url += self.encode_key_value(key, value)
        return self.make_request('%s%s' % (self.base_url, end_url))
