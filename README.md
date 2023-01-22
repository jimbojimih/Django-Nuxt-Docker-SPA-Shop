# 5.-Django-Nuxt-Docker-SPA-Shop
A small shop selling hand-made goods.

Небольшой магазин хенд-мейд товаров в виде одностраничного приложения. Используемый стек: Django REST framework, Nuxt, Nginx, Docker.
Бекенд представляет собой API, При добавлении товара в корзину, автоматически создаётся пользователь, авторизация через сессию. В админке настроены
фильтры. 
Фронтенд написан на Nuxt. Приложение представляет собой страницу(index) с перезагружаемыми компонентами. Все данные в приложении реактивно связаны с бекендом. При добавлении/изменении/удалении категорий, подкатегорий и товаров в админке, изменения отразятся во фронте. Приложение имеет адаптивный дизайн. Универсальный рендеринг, первичная отрисовка страницы происходит на сервере, последующая навигация по сайту осуществляется на клиенте с помощью запросов в API бекенда.
В роли веб сервера выступает Nginx.
Приложение настроено на работу с Docker.
Для запкуска в режиме разработки введите команды
```
docker-compose -f docker-dev.yml build
docker-compose -f docker-dev.yml up
```

Не забудьте устновить свои SECRET_KEY для django и TOKEN_TELEGRAM для бота в переменные окружения ".env.dev" и ".env.prod"

![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen1.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen2.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen3.png)  
![](https://github.com/jimbojimih/5.-Django-Nuxt-Docker-SPA-Shop/blob/master/!screenshots%20for%20github/screen4.png)  


