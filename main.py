from lib import *
app_banner = """
FETCHY
"""
version = '0.1.0'
menu_items = """
1. Weather
2. Youtube Video
3. Cryptocurrency
4. Quotes
"""

def Menu():
   print("====== Fetchy", version)
   print("A command-line tools for fetching data")
   print("======================================")
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
   else:
      print("Error")

Menu()
Select_Menu()