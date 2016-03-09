import os
import platform
import tempfile
import shutil
import json
import requests

class Wallpaper:
    system = platform.system()
    headers = {'user-agent': system.lower() + ':reddit_wallpaper:v.1.0 (by /u/dereddy)'}

    def __init__(self, reddits = ['earthporn', 'spaceporn', 'skyporn', 'cityporn', 'abandonedporn'], delete=True):
        self.tmpdir = tempfile.mkdtemp('', 'reddit_wallpaper-') + '\\'
        self.reddits = reddits
        self.delete_flag = delete
        if self.system == 'Linux':
            import tkinter as tk
            root = tk.Tk()
            self.width = root.winfo_screenwidth()
            self.height = root.winfo_screenheight()
        elif self.system == 'Windows':
            import ctypes
            user32 = ctypes.windll.user32
            self.width = user32.GetSystemMetrics(0)
            self.height = user32.GetSystemMetrics(1)
        self.get_image_url()
        self.download_image()
        self.set_wallpaper(self.tmpdir + self.img_url.split('/')[-1])

    def __del__(self):
        if self.delete_flag == True:
            shutil.rmtree(self.tmpdir, True)

    def get_url(self, amount=5):
        url = 'https://www.reddit.com/r/'
        for r in self.reddits:
            url = url + r + '+'
        url += '/top.json?t=day&limit=' + str(amount)
        return url

    def get_json(self, amount=5):
        r = requests.get(self.get_url(amount), headers=self.headers)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception('No valid subreddit specified')

    def get_image_url(self):
        for amount in range(5, 105, 5):
            json = self.get_json(amount)
            for image in json['data']['children']:
                image_width = image['data']['preview']['images'][0]['source']['width']
                image_height = image['data']['preview']['images'][0]['source']['height']
                if image_width > image_height and image_width >= self.width and image_height >= self.height:
                    img_url = image['data']['url']
                    img_url_ext = os.path.splitext(img_url)[1]
                    if img_url_ext in ['.jpg', '.jpeg', '.png', '.bmp']:
                        self.img_url = img_url
                        return
        raise Exception('No image could be retrieved')

    def download_image(self):
        r = requests.get(self.img_url, headers=self.headers, stream=True)
        if r.status_code == 200:
            with open(self.tmpdir + self.img_url.split('/')[-1], 'wb') as f:
                for chunk in r:
                    f.write(chunk)

    def set_wallpaper(self, path_img):
        if self.system == 'Linux':
            gsettings = Gio.Settings.new("org.gnome.desktop.background")
            gsettings.set_string("picture-uri", "file://" + path_img)
            gsettings.apply()
        elif self.system == 'Windows':
            from ctypes import windll
            windll.user32.SystemParametersInfoW(0x14, 0, path_img, 3)


if __name__ == '__main__':
    w = Wallpaper()
    print(w.img_url)
