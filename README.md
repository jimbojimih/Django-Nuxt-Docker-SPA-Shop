# 5.-Django-Nuxt-Docker-SPA-Shop
A small hand-made goods store in the form of a single-page application.  
*You can see the finished project at the link: [Bird & star](http://bird-and-star.ru/).*  
Stack used: Django REST framework, Nuxt, Nginx, Docker.  

Небольшой магазин хенд-мейд товаров в виде одностраничного приложения.  
*Посмотреть готовый проект можно по ссылке: [Bird & star](http://bird-and-star.ru/).*   
Используемый стек: Django REST framework, Nuxt, Nginx, Docker.
1) Бекенд представляет собой API написанный на DRF. При добавлении товара в корзину, создаётся пользователь с автоматической авторизацией через сессию. Админка полностью настроена для работы с товарами и отслежевания продаж. Информация о покупке поступает в продавцу в телеграмм с помощью запроса в API telegram.
2) Фронтенд написан на Nuxt. Приложение представляет собой страницу(index) с динамически подгружаемыми компонентами. При добавлении/изменении/удалении категорий, подкатегорий и товаров в админке, изменения отразятся во фронтенде. Приложение имеет адаптивный дизайн и универсальный рендеринг, первичная отрисовка страницы происходит на сервере, последующая навигация по сайту осуществляется на клиенте с помощью запросов в API бекенда.
3) В роли веб сервера выступает Nginx.
4) Приложение настроено на работу с Docker. 
Для запкуска в режиме разработки введите команды:
```
docker-compose -f docker-dev.yml build
docker-compose -f docker-dev.yml up
```
http://localhost:3000/ - фронт  
http://localhost:8000/api - бекенд  
http://localhost:8000/admin - админка  

Для запуска в продакшн:
```
docker-compose -f docker-prod.yml build
docker-compose -f docker-prod.yml up
```
http://localhost:80/ -фронт  
http://localhost:80/api -бекенд  
http://localhost:80/admin -админка  

**Не забудьте устновить свои SECRET_KEY для django и TOKEN_TELEGRAM для бота в переменные окружения ".env.dev" и ".env.prod"!**  
__desktop screens:__   
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen1.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen2.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen3.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen4.png)  
__mobile screens:__  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen5.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen6.png)   
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen7.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen8.png)   

