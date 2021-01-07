from util.util import Util
from engine.engine import Engine
import time


class Bing(Engine):
    HOME_URL = 'https://cn.bing.com/images/'

    def __init__(self, web_driver, key, storing_folder):
        Engine.__init__(self, web_driver)
        self.storing_folder = storing_folder
        self.key = key

    def retrieve_image(self):
        Engine.retrieve_image(self)
        self.web_driver.get(Bing.HOME_URL)

        search_box = self.web_driver.find_element_by_class_name("b_searchbox")
        search_box.send_keys(self.key)
        search_box.submit()

        self.web_driver.find_elements_by_css_selector("[class='mimg']")[0].click()
        time.sleep(2)

        current_url = self.web_driver.current_url
        self.web_driver.get(current_url)

        img = self.web_driver.find_elements_by_css_selector("div.imgContainer > img")[0]
        current_index = 0
        while img is not None:
            img_src = img.get_attribute('src')
            image_format = 'jpg'
            print('IMAGE URL: ', img_src)
            image_name = str(current_index) + '.' + image_format
            if Util.download_image(img_src, self.storing_folder, image_name):
                current_index += 1
            self.web_driver.find_element_by_id("navr").click()
            time.sleep(2)
            img = self.web_driver.find_elements_by_css_selector("div.imgContainer > img")[0]
