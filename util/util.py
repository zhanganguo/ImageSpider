import urllib.request
from util.user_agents import UserAgent
import os


class Util:
    @staticmethod
    def create_dir(dir):
        is_success_creation = False
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
                is_success_creation = True
        except Exception as e:
            print(e)
        return is_success_creation

    @staticmethod
    def download_image(url, path, name):
        is_success_downloading = False

        headers = {'User-Agent': UserAgent.get_agent_randomly()}
        request = urllib.request.Request(url=url, headers=headers)
        try:
            binary_data = urllib.request.urlopen(request, timeout=30).read()
            if len(binary_data) > 1000:
                if not os.path.exists(path):
                    Util.create_dir(path)
                with open(os.path.join(path, name), 'wb') as f:
                    f.write(binary_data)
                    f.flush()
                    f.close()
                    is_success_downloading = True
            else:
                print('Image too small, skipped.')
        except Exception as e:
            print(e)
        return is_success_downloading
