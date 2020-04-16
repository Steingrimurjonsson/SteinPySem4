import os
import urllib.request as req
from urllib.parse import urlparse
import urllib
import requests
import concurrent
import re
import threading
import multiprocessing

class Module:
    def __init__(self, url_list):
        self.url_list = url_list

    def download(self, url, file_name=None):
        class NotFoundException(ValueError):
                def __init__(self, *args, **kwargs):
                    ValueError.__init__(self, *args, **kwargs) 
        if file_name:
            local_file = file_name
        else:
            file_name = os.path.basename(urlparse(url).path)
            local_file = os.path.join('.', file_name)
        res = requests.get(url)
        if res.status_code == 404:
            raise NotFoundException('Not found')
        else:
            print('Success')
            with open(file_name, 'wb') as file:
                for chunk in res.iter_content(chunk_size=1024):
                    file.write(chunk) 

                    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.url_list) == 0:
            raise StopIteration()
        else:
            for url in self.url_list:
                file_name = os.path.basename(urlparse(url).path)
                with open(file_name) as file:
                    print(file_name)
                    return file_name
            
    def url_list_generator(self):
        for url in self.url_list:
            print(url)

    def avg_vowels(self, text):
        with open(text) as file:
            lines = file.readlines()
        vowel_string = ''
        for line in lines:
            vowel_string += line
        word = len(re.findall(r'\w+', vowel_string)) 
        vowel = len(re.findall(r'[aeiou]', vowel_string, flags=re.IGNORECASE))
        print(word/vowel)
        return word/vowel