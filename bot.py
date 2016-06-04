import telegram
import pyowm



def send_message():
    bot = telegram.Bot(token='239352413:AAEI2CGw5XoezKBFssdzGVxS-6aDQC8dIio')
    chat_id = bot.getUpdates()[-1].message.chat_id
    owm = pyowm.OWM('cda178269c34730fb6086e150a56b74d')

    observation = owm.weather_at_place('Groningen,nl')
    w = observation.get_weather()

    wind        = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    temperature = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain        = w.get_rain()
    clouds      = w.get_clouds()
    text_status = w.get_status()

    speed = wind.get('speed')
    min_temp = temperature.get('temp_min')
    max_temp = temperature.get('temp_max')
    grade = calculate_grade(max_temp, speed)
    
    message = "Hallo! Fiets Paulusma hier, met een windkracht van %s en een temperatuur van %s geef ik het fietsweer een: %s" % (speed, max_temp,grade)
    bot.sendMessage(chat_id=chat_id, text=message)


def calculate_grade(max_temp, speed):
    grade =  10;

    if max_temp < 10:
        grade - 7

    if max_temp < 15:
        grade - 4

    if max_temp > 25:
        grade - 1

    if speed > 5:
        grade - 2

    if speed > 7:
        grade - 5

    return grade



send_message()
