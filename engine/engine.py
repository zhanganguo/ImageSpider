from util import Util
import time


class Engine:
    def __init__(self, web_driver, start_url, storing_folder):
        self.web_driver = web_driver
        self.start_url = start_url
        self.storing_folder = storing_folder
        Util.create_dir(storing_folder)

    def retrieve_image(self):
        self.web_driver.get(self.start_url)
        time.sleep(6)
