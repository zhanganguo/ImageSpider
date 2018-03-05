import urllib2
from user_agents import UserAgent
import os


class Util:
    @staticmethod
    def create_dir(dir):
        is_success_creation = False
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
                is_success_creation = True
        except Exception, e:
            pass
        return is_success_creation

    @staticmethod
    def download_image(url, path, name):
        is_success_downloading = False
        try:
            headers = {'User-Agent': UserAgent.get_agent_randomly()}
            request = urllib2.Request(url=url, headers=headers)
            binary_data = urllib2.urlopen(request).read()
            if len(binary_data) > 1000:
                with open(path + name, 'wb') as f:
                    f.write(binary_data)
                    f.flush()
                    f.close()
                    is_success_downloading = True
            else:
                print 'Image too small, skipped.'
        except Exception, e:
            print e
        return is_success_downloading
