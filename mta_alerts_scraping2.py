# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:49:03 2023

@author: sachi

Command to run: spider runspider mta_alerts_scraping2.py
"""

import scrapy
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
from scrapy import FormRequest
import random
import time
import pandas as pd


class MTASpider(scrapy.Spider):
    name = 'prices'
    start_urls = ['https://mtamarylandalerts.com/MessageArchive.aspx']
    
    def parse(self, response):
        data = {
            
            	"ctl00_ctl06_TSM": ";;System.Web.Extensions,+Version=4.0.0.0,+Culture=neutral,+PublicKeyToken=31bf3856ad364e35:en-US:669ca791-a838-4419-82bc-9fa647338708:ea597d4b:b25378d2;Telerik.Web.UI,+Version=2019.2.514.45,+Culture=neutral,+PublicKeyToken=121fae78165ba3d4:en-US:2e526c17-29b2-48b8-905d-11b7bd399312:16e4e7cd:33715776:f7645509:88144a7a:7c926187:8674cba1:b7778d6c:c08e9f8a:a51ee93e:59462f1:58366029",
            	"ctl00$ContentPlaceHolder1$dtpStartDate": "2011-01-01",
            	"ctl00$ContentPlaceHolder1$dtpStartDate$dateInput": "01/01/2011",
            	"ctl00_ContentPlaceHolder1_dtpStartDate_dateInput_ClientState": "{\"enabled\":true,\"emptyMessage\":\"\",\"validationText\":\"2011-01-01-00-00-00\",\"valueAsString\":\"2011-01-01-00-00-00\",\"minDateStr\":\"1980-01-01-00-00-00\",\"maxDateStr\":\"2099-12-31-00-00-00\",\"lastSetTextBoxValue\":\"01/01/2011\"}",
            	"ctl00_ContentPlaceHolder1_dtpStartDate_calendar_SD": "[]",
            	"ctl00_ContentPlaceHolder1_dtpStartDate_calendar_AD": "[[1980,1,1],[2099,12,30],[2023,10,26]]",
            	"ctl00_ContentPlaceHolder1_dtpStartDate_ClientState": "",
            	"ctl00$ContentPlaceHolder1$dtpStopDate": "2023-10-26",
            	"ctl00$ContentPlaceHolder1$dtpStopDate$dateInput": "10/26/2023",
            	"ctl00_ContentPlaceHolder1_dtpStopDate_dateInput_ClientState": "{\"enabled\":true,\"emptyMessage\":\"\",\"validationText\":\"2023-10-26-00-00-00\",\"valueAsString\":\"2023-10-26-00-00-00\",\"minDateStr\":\"1980-01-01-00-00-00\",\"maxDateStr\":\"2099-12-31-00-00-00\",\"lastSetTextBoxValue\":\"10/26/2023\"}",
            	"ctl00_ContentPlaceHolder1_dtpStopDate_calendar_SD": "[]",
            	"ctl00_ContentPlaceHolder1_dtpStopDate_calendar_AD": "[[1980,1,1],[2099,12,30],[2023,10,26]]",
            	"ctl00_ContentPlaceHolder1_dtpStopDate_ClientState": "",
            	"ctl00$ContentPlaceHolder1$btnGetData": "Update",
            	"ctl00_ContentPlaceHolder1_gridMessages_ClientState": ""
            }
        # using a rate limiting step to not tax server
        time.sleep(3)
        yield FormRequest.from_response(response,formdata=data, callback=self.step2)
        
    def step2(self, response): 
        dfs = pd.read_html(response.text)
        dfs[8].to_csv(f'data_2.csv')
        data = {
            
            	"ctl00$ContentPlaceHolder1$gridMessages$ctl00$ctl02$ctl01$ctl28": "+",
            	"ctl00$ContentPlaceHolder1$gridMessages$ctl00$ctl02$ctl01$PageSizeComboBox": "50",
            	"ctl00_ContentPlaceHolder1_gridMessages_ctl00_ctl02_ctl01_PageSizeComboBox_ClientState": "",
            	"ctl00$ContentPlaceHolder1$gridMessages$ctl00$ctl03$ctl02$PageSizeComboBox": "50",
            	"ctl00_ContentPlaceHolder1_gridMessages_ctl00_ctl03_ctl02_PageSizeComboBox_ClientState": "",
            	"ctl00_ContentPlaceHolder1_gridMessages_ClientState": ""
                }
        # using a rate limiting step to not tax server
        time.sleep(3)
        yield FormRequest.from_response(response,formdata=data, callback=self.step3)
    
    #Essentially we have to call the same function 1107 times to loop through all of the pages
    def step3(self, response): 
        dfs = pd.read_html(response.text)
        dfs[8].to_csv(f'data_3.csv')
        data = {
            
            	"ctl00$ContentPlaceHolder1$gridMessages$ctl00$ctl02$ctl01$ctl28": "+",
            	"ctl00$ContentPlaceHolder1$gridMessages$ctl00$ctl02$ctl01$PageSizeComboBox": "50",
            	"ctl00_ContentPlaceHolder1_gridMessages_ctl00_ctl02_ctl01_PageSizeComboBox_ClientState": "",
            	"ctl00$ContentPlaceHolder1$gridMessages$ctl00$ctl03$ctl02$PageSizeComboBox": "50",
            	"ctl00_ContentPlaceHolder1_gridMessages_ctl00_ctl03_ctl02_PageSizeComboBox_ClientState": "",
            	"ctl00_ContentPlaceHolder1_gridMessages_ClientState": ""
                }
        # using a rate limiting step to not tax server
        time.sleep(3)
        yield FormRequest.from_response(response,formdata=data, callback=self.step4)
    
    def step4(self, response):
        open_in_browser(response)