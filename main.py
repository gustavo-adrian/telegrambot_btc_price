"""
Bot con Python, que enviará todos los días mensajes con el precio actual de Bitcoin a Telegram.
"""

# bs4 para obtener el precio de bitcoin
from bs4 import BeautifulSoup # del modulo bs4, solo necesitamos BeautifulSoup
# Para conectarse con Telegram con peticiones HTTP
import requests
# Para que los mensajes del bot sean recurrentes
import schedule


def bot_send_text(bot_message):
    """Función que envía un mensaje a Telegram"""

    bot_token = 'YOUR_TOKEN'
    bot_chatID = 'YOUR_CHATID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response


def btc_scraping():
    """Ingresa a la página web y analiza su estructura html para poder acceder a sus elementos"""

    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'text-larger text-price'})
    format_result = result.text
    return format_result


def report():
    """Ejecuta las funciones 'bot_send_text' y 'btc_scraping'."""

    btc_price = f'El precio de Bitcoin es de {btc_scraping()}'
    bot_send_text(btc_price)


if __name__ == '__main__':
    schedule.every().day.at("02:00").do(report)
    while True:
        schedule.run_pending()
