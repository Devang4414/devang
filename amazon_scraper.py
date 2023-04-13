import requests
from bs4 import BeautifulSoup
from lxml import html
import time
import json




class ProductInfoScraper:
    
    def __init__(self, soup, dom):
        self.soup = soup
        self.dom = dom
    
    def get_title(self):
        try:
            title = self.soup.find("span", attrs={"id":'productTitle'}).text.strip()
        except AttributeError:
            try:
                title = self.dom.xpath('//*[@id="productTitle"]')[0].text.strip()
            except:
                title = "No Data"
        return title
    
    def get_price(self):
        try:
            price = self.soup.find('span',attrs={"class":"a-price-whole"}).text
        except AttributeError:
            try:
                price = self.dom.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')[0].text.strip()
            except:
                price = "No Data"
        return price

    def get_mrp(self):
        try:
            mrp = self.soup.find('table',attrs={'class':'a-lineitem a-align-top'}).find('span',attrs={'class':'a-offscreen'}).text.strip()
        except AttributeError:
            try:
                mrp = self.dom.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span/span[1]')[0].text.strip()
            except:
                mrp = "No Data"
        return mrp
    
    def get_rating(self):
        try:
            rating = self.soup.find("span", attrs={"id":'acrPopover'}).text.strip()
        except AttributeError:
            try:
                rating = self.dom.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span')[0].text.strip()
            except:
                rating = "No Data Available"
        return rating
    
    def get_features(self):
        try:
            features = self.soup.find('div',attrs={"id":"feature-bullets"}).text.strip().replace('   ','|')
        except AttributeError:
            try:
                features = self.dom.xpath('//*[@id="feature-bullets"]')[0].text.strip().replace('   ','|')
            except IndexError:
                features = "No data"
        return features

    def get_tech_details(self):
        try:
            t = self.soup.find('table',attrs={"id":"productDetails_techSpec_section_1"}).text.strip().replace('\n                \u200e',' ')
            tech_details = t.replace("    ",'|')
        except AttributeError:
            try:
                t = self.dom.xpath('//*[@id="productDetails_techSpec_section_1"]')
                if t:
                    t = t[0].text.strip().replace('\n                \u200e',' ')
                    tech_details = t.replace("    ",'|')
                else:
                    tech_details = "No Data"
            except:
                tech_details = "No Data"
        return tech_details

    def get_add_info(self):
        try:
            add_info = self.soup.find('table',attrs={"id":"productDetails_detailBullets_sections1"}).text.strip().replace('   ','|')
        except AttributeError:
            try:
                add_info = self.dom.xpath('//*[@id="productDetails_detailBullets_sections1"]')
                if add_info:
                    add_info = add_info[0].text.strip().replace('   ','|')
                else:
                    add_info = "No Data"
            except:
                add_info = "No Data"
        return add_info 
    
    #Function to extract Product Description
    def get_desc(self):
        try:
            desc = self.soup.find('div',attrs={'id':'productDescription'}).text.strip()
        except:
            desc = "No Data"

        return desc
    
    #Function to extract image link
    def get_img_link(self):
        try:
            img_div = self.soup.find('div',attrs={'id':'imgTagWrapperId'})
            time.sleep(7)
            img_str = img_div.img.get('data-a-dynamic-image')
            img_dict = json.loads(img_str)

            img_link_list = list(img_dict.keys())
                    
        except (TypeError,AttributeError):
            try:
                img_link_list = list(json.loads(self.dom.xpath(' //*[@id="landingImage"]')[0].get('data-a-dynamic-image')).keys())
        
            except:
                img_link_list = "No Data"
        
        return img_link_list
    
           
