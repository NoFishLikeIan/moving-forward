import smtplib
import time
import numpy as np
from email.mime.text import MIMEText
from datetime import datetime
from threading import Timer
from newsapi import NewsApiClient
import wikipedia
import requests

today = datetime.today()
#filename = f'mails/email_{today.day}_{today.month}.txt'

parameters = {
    'mood': ['I love you', 'I think you are beutiful', 'I hope you have a great day'],
    'your_day': ['the day might make you stressed but know that I am thinking about you', 'you might find it hard to cope with the stress today but if you read this, I am here for you', 'the day could be hard so if you want just text me @nofishlikeian on Telegram', 'hopefully today is going to be a bit relaxing and fun']
}

days_of_week = {
    'monday': ['the worst day of the week, you can do this', 'you know what they say "In all possible universes, Monday was the same."'],
    'tuesday': ['at least it is not monday', 'it is your work day! Remember to go and to tell me you love me', "today's quote is from Popeye 'There are days when spelling Tuesday simply doesn't count."],
    'wednesday': ['we are halfway through the work days, treat yourself to some nice food today', 'on this day I am thinking of your nice smile', 'I know you want to just press this link today https://www.reddit.com/r/Longreads/'],
    'thursday': ['it is the best day of the week because you can feel the excitement', "I'll try and update the playlist today", 'as Arthur Dent said "This must be Thursday.  I never could get the hang of Thursdays."'],
    'friday': ['almost the weekend already! Text me what you are doing this weekend', 'did you remember to do everything before this weekend?', 'https://www.youtube.com/watch?v=kfVsfOSbJY0 play this RIGHT NOW!'],
    'saturday': ['the weekend came so I am not going to bother you much, just "I love you', 'guess what? It is the weekend, get out of bed and do somethign for Christ sake-comma-s', 'watch a movie today!'],
    'sunday': ['the weekend came so I am not going to bother you much, just "I love you', 'guess what? It is the weekend, get out of bed and do somethign for Christ sake-comma-s', 'watch a movie today!']
}


def news(source='bbc-news'):
    api = NewsApiClient(api_key='4ee615eaac954a4da19324f7d02b2ef8')
    r = api.get_everything(sources=source)['articles'][0]
    title = r['title']
    article = r['description']
    url = r['url']
    output = f'Here is the article from this url {url}:\n{title}\n{article}'
    output = ''.join([i if ord(i) < 128 else ' ' for i in output])
    return output


def wiki():
    random_wiki = wikipedia.random()
    page = wikipedia.page(random_wiki)
    url = page.url
    summary = f'{wikipedia.summary(random_wiki)} for more just go to {url}'
    return summary


def reddit_random():
    url = 'http://www.reddit.com/r/longreads/random.json'
    r = requests.get(url)
    data = r.json()
    try:
        article_url = data[0]['data']['children'][0]['data']['url']
        return article_url
    except KeyError:
        return 'Something went wrong with your url, I think we made too many requests'


random_api = {'news': news(),
              'wiki': wiki(),
              'reddit': reddit_random()
              }


def random_choice(dictionary, input):
    choice = np.random.choice(dictionary[input])
    return choice


from_addr = 'ianfisherma@gmail.com'
to_addr = 'philippa.johnson@hotmail.com'
pwd = 'random_pswd_32'


def sendemail(from_addr=from_addr, to_addr=[to_addr], subject='Daily email from Andrea',
              ogin=from_addr, password=pwd,
              smtpserver='smtp.gmail.com:587', login=from_addr, send=True):

    weekdays = list(days_of_week.keys())
    day_today = weekdays[datetime.today().weekday()]
    random_api_choice = np.random.choice(list(random_api.keys()))
    message = f'''Goodmorning Phil, today is {day_today.title()}: {random_choice(days_of_week, day_today)}! Anyhow, I just wanted to say that {random_choice(parameters, 'mood')} and that {random_choice(parameters, 'your_day')}\nYou even get a random api... let's see: {random_api_choice}, here you go.\n{random_api[random_api_choice]}
    '''

    msg = "\r\n".join([
        f"From: {from_addr}",
        f"To: {to_addr}",
        f"Subject: {subject}",
        f"",
        f"{message}"
    ])

    if send == True:
        server = smtplib.SMTP(smtpserver)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(login, password)
        #problems = server.sendmail(from_addr, to_addr, msg)
        server.quit()

    return message


# if cond == 'y':
#     send = True
#     text = sendemail(send=send)
#     if not send:
#         print('The email was not sent because "sent" was set to False')
#     print(f'Email sent with text:\n{text}')
# else:
#     print('See you')

if __name__ == '__main__':
    sendemail(send=True)
