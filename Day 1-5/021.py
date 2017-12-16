import pyowm

myOwm = pyowm.OWM('dbf6aaf008f3591e4eeb64257fd2d985')
# owm = pyowm.OWM('dbf6aaf008f3591e4eeb64257fd2d985')

location = 'Bergen, Norway'

myWeather = myOwm.weather_at_place(location)

print(myWeather.get_weather().get_humidity())
print(myWeather.get_weather().get_temperature('celsius'))
