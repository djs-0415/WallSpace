import flickr_api
import win32api, win32con, win32gui

username = 'NASA Goddard Photo and Video'

flickr_api.set_keys(api_key='73ec08be7826d8b0a608151ce5faaf9d', api_secret='fbb2fcd772ce44a6')

user = flickr_api.Person.findByUserName(username)

photos = user.getPublicPhotos()
print photos[0]
photos[0].save(photos[0].title+".jpg")

def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

if __name__== "__main__":
    path = r'C:\Users\djs04_000\documents\visual studio 2013\Projects\WallSpace\WallSpace\Hubble Observes One-of-a-Kind Star Nicknamed ?Nasty?.jpg'
    setWallpaper(path)