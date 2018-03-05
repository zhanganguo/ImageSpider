from util import Util
import time


class Baidu:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    def retrieve_image(self, storing_folder):
        Util.create_dir(storing_folder)

        url = self.web_driver.find_element_by_class_name("currentImg")
        currentIndex = 0
        while url is not None:
            url = url.get_attribute('src')
            image_format = url.split('.')[-1]
            print'IMAGE URL: ', url
            image_name = str(currentIndex) + '.' + image_format
            if Util.download_image(url, storing_folder, image_name):
                currentIndex += 1
            self.web_driver.find_elements_by_class_name("img-switch-btn")[1].click()
            time.sleep(2)
            url = self.web_driver.find_element_by_class_name("currentImg")

