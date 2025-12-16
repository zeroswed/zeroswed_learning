# import requests

# class Weather:
#     response = ""
#     appid = "33a3a8d605e2bee47f89303108959e0c"

    

#     def __init__(self, city, lat, lon, units="metric"):
#         self.city = city
#         self.lon = lon
#         self.lat = lat
#         self.unitis = units
        
#     def get_data(self):

#         try:
#             self.response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}c&lat={self.lat}&lon={self.lon}&appid={self.appid}")
            
#         except:
#             print("Internet is not working")
        
#         self.response_json = self.response.json()
#         self.temp = response_json["main"]["temp"]
#         self.temp_min = response_json["main"]["temp_min"]
#         self.temp_max = response_json["main"]["temp_max"]
#         print(f"Weather {self.city} is followint. Temp is {self.temp}C, min temp is {self.temp_min}C, max temp is {self.temp_max}C")

# Weather("Split", 43.5147, 16.4435).get_data()



import requests

class Weather:

    def __init__(self, city, lat, lon, units="metric"):
        self.city = city
        self.lon = lon
        self.lat = lat
        self.units = units
        self.temp = ""
        self.temp_min = ""
        self.temp_max = ""
    
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=33a3a8d605e2bee47f89303108959e0c")
            response_json = response.json()    

            print(response_json)

            
               
        except:
            print("Something is not working right.")
    
    def get_data(self):
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
        print(f"Weather in {self.city} is following. Temp is {self.temp}C, min temp is {self.temp_min}C, max temp is {self.temp_max}C")



       

Weather("Split", 43.5081323, 16.4401935)
