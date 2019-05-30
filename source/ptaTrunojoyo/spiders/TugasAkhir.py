# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ptaTrunojoyo.items import ItemTugasAkhir
import re
situsKe = 0

class TugasakhirSpider(CrawlSpider):
    name = "TugasAkhir"
    allowed_domains = ['id.wikipedia.org']
    start_urls = ['https://id.wikipedia.org/wiki/Jembatan_Nasional_Suramadu']

   
    def parse(self, response):
        global situsKe
        situsKe+=1
        linkKe = 0
        deep = 1
        
        soup = BeautifulSoup(response.body , features="lxml")
        print("situsKe = ",situsKe ," url = ",response.url)
        links = soup.find_all('a')
        linkDiperbaiki=list()
        for x in links:
            tmp = str(x.get('href'))
            if(("/wiki/" in tmp[0:6]) and (":" not in tmp)):
   
                tmp1 = str("https://id.wikipedia.org" + tmp)
                linkDiperbaiki.append(tmp1)

        print("panjang links  = ",len(linkDiperbaiki))
        for x in linkDiperbaiki:        
            linkKe+=1
            print("linkKe = ",linkKe,"url = ",x)
            item = ItemTugasAkhir()
            item['url'] = response.url
            item['link_keluar'] = x
            item['situsKe'] = situsKe				
            item['linkKe'] = linkKe
            item['deep'] = deep
            yield item
        for x in linkDiperbaiki:  
            next_page = response.urljoin(x)
            yield scrapy.Request(next_page, callback=self.parse_deep2)
        print("===============================end deep1===========================")
    def parse_deep2(self, response):
        global situsKe
        situsKe+=1
        linkKe = 0
        deep = 2
        
        soup = BeautifulSoup(response.body , features="lxml")
        print("situsKe = ",situsKe ," url = ",response.url)
        links = soup.find_all('a')
        linkDiperbaiki=list()
        for x in links:
            tmp = str(x.get('href'))
            if(("/wiki/" in tmp[0:6]) and (":" not in tmp)):
   
                tmp1 = str("https://id.wikipedia.org" + tmp)
                linkDiperbaiki.append(tmp1)

        print("panjang links  = ",len(linkDiperbaiki))
        for x in linkDiperbaiki:        
            linkKe+=1
            print("linkKe = ",linkKe,"url = ",x)
            item = ItemTugasAkhir()
            item['url'] = response.url
            item['link_keluar'] = x
            item['situsKe'] = situsKe				
            item['linkKe'] = linkKe
            item['deep'] = deep
            yield item
        for x in linkDiperbaiki:  
            next_page = response.urljoin(x)
            yield scrapy.Request(next_page, callback=self.parse_deep3)
        print("===============================end deep2===========================")
    def parse_deep3(self, response):
        global situsKe
        situsKe+=1
        linkKe = 0
        deep = 3
        
        soup = BeautifulSoup(response.body , features="lxml")
        print("situsKe = ",situsKe ," url = ",response.url)
        links = soup.find_all('a')
        linkDiperbaiki=list()
        for x in links:
            tmp = str(x.get('href'))
            if(("/wiki/" in tmp[0:6]) and (":" not in tmp)):
                tmp1 = str("https://id.wikipedia.org" + tmp)
                linkDiperbaiki.append(tmp1)

        print("panjang links  = ",len(linkDiperbaiki))
        for x in linkDiperbaiki:        
            linkKe+=1
            print("linkKe = ",linkKe,"url = ",x)
            item = ItemTugasAkhir()
            item['url'] = response.url
            item['link_keluar'] = x
            item['situsKe'] = situsKe				
            item['linkKe'] = linkKe
            item['deep'] = deep
            yield item
        print("===============================end deep3===========================")
