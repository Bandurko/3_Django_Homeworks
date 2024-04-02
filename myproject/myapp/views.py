from django.shortcuts import render

# Create your views here.

import logging
from django.http import HttpResponse, HttpRequest


logger = logging.getLogger(__name__)


def index(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Главная</title>
</head>
<body>
    <h1>Это Главная страница сайта на Django.</h1>
</body>
</html>
"""
    logger.info('Index page requested.')

    return HttpResponse(html)


def about(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Обо мне</title>
</head>
<body>
    <p><h1>Эта страница обо мне.</h1></p>
    <h3>Меня зовут Вася Пупкин.<br>
    Я живу в Бобруйске.<br>
    Учу албанский.</h3>
    <p>
    <img src="https://p1.hiclipart.com/preview/412/169/291/emoticon-smiley-yellow-facial-expression-head-nose-mouth-eye-png-clipart.jpg" 
    width="300"  height="300" alt="Смайлик"></p>
</body>
</html>
"""
    logger.info('About page requested.')

    return HttpResponse(html)