import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from tutorial.items import * #FreshItem, WebItem, Web1Item, Web2Item, Veg2Item, VegItem, Kaki0Item, Kaki9Item, DatagovItem, PropertyItem, VsItem, AoucrItem, OnemgItem, FundoodataItem, CouponsItem, QuickItem, TimesItem,  NaukriItem, VizagTelDirItem, MoviesItemnew,  MoviesItem, VizagInfoItem,HinduItem, AgriItem, BazarItem, OxItem,JustItem, GoogleItem, VsptelItem,BrainyItem, JustMovieItem, JustDialItem, IndiaMartItem, PumpBizItem, AnWatchItem, AutoItem, SpecialItem
from scrapy.contrib.spiders import CrawlSpider
import datetime
import time
import MySQLdb
import urllib
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


        
class Web1ItemSpider(CrawlSpider): 
     name = "stuff1"
     allowed_domains = ["url"]
     a = "url"
     b=[]
     for i in range(10):
         b.append(str(a)+str(i))
         
     start_urls = b
     
     def parse(self, response):
        for i in response.xpath("//div[@class='listing-header']/div/a/@href"):
            linka = i.extract()
            link = "url" + linka
            request = Request(link, callback=self.parse_comp, dont_filter=True)
            yield request

            .
     def parse_comp(self, response):
        item = Web1Item()
        print "parsing"
        conn1 = MySQLdb.connect('127.0.0.1','user','pswd','db_name')
        curs1 = conn1.cursor()
        item['Name'] = response.xpath("//div[@class='job_margin'][1]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['Caption'] = response.xpath("//div[@class='job_margin'][2]/div[@class='main_padding_detail1_new'][1]/a/text()").extract()[0].replace('\r', '').replace('\n', '') 
        item['functionalarea'] = response.xpath("//div[@class='job_margin'][3]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['Description'] = response.xpath("//div[@class='job_margin'][4]/div[@class='main_padding_detail1_new'][1]/text()").extract() [0].replace('\r', '').replace('\n', '')
        item['Qualification'] = response.xpath("//div[@class='job_margin'][5]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['Experience'] = response.xpath("//div[@class='job_margin'][6]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['Salary'] = response.xpath("//div[@class='job_margin'][7]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['Address'] = response.xpath("//div[@class='job_margin'][8]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['landmark'] = response.xpath("//div[@style='margin-top:5px;']/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('\r', '').replace('\n', '')
        item['mobile'] = response.xpath("//div[@id='details_block'][1]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace('(M)','').replace(' ','').replace(u'\xa0', u' ')
        item['slug'] = response.xpath("//div[@class='job_margin'][1]/div[@class='main_padding_detail1_new'][1]/text()").extract()[0].replace(' ','-').replace('(','-').replace(')','-').replace('--','-').replace('-','-').replace('\r', '').replace('\n', '')
        curs1.execute("INSERT INTO table_name(Name, Caption, functionalarea, Qualification, Experience, Salary, Address, landmark, mobile, slug) VALUES (   %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ( str(item['Name']), str(item['Caption']), str(item['functionalarea']),str(item['Qualification']),str(item['Experience']),str(item['Salary']),str(item['Address']),str(item['landmark']),str(item['mobile']),str(item['slug'])))
        conn1.commit()
        yield item

