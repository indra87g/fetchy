#from lib import *
import quotes
import weather
import youtube
import crypto
app_banner = """                                                                
  ______   _       _           
 |  ____| | |     | |          
 | |__ ___| |_ ___| |__  _   _ 
 |  __/ _ \ __/ __| '_ \| | | |
 | | |  __/ || (__| | | | |_| |
 |_|  \___|\__\___|_| |_|\__, |
                          __/ |
                         |___/ 
"""

version = '0.1.0'
menu_items = """
1. Weather
2. Youtube Video
3. Cryptocurrency
4. Quotes

===================
0. Exit
===================
"""

def Menu():
   print(app_banner)
   print(version)
   print(menu_items)

def Select_Menu():
   select_menu = int(input("Select menu: "))
   if select_menu == 1:
      city_name = input("Enter city name: ")
      weather.Fetch(city_name)
   elif select_menu == 2:
      youtube.Fetch()
   elif select_menu == 3:
      crypto.Fetch()
   elif select_menu == 4:
      quotes.Fetch()
   elif select_menu == 0:
      exit()
   else:
      print("Error")

Menu()
Select_Menu()