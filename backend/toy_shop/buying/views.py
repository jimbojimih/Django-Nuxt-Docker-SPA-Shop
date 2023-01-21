from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.db.models import Sum
import requests as requests_lib
from requests.exceptions import RequestException


class Buying(views.APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        if  not user.items.all():
            return Response(status=status.HTTP_400_BAD_REQUEST, 
                            data='Добавьте товары')
        
        for item in user.items.all():
            item.selled = True
            item.save()            

            product = item.item
            product.available = False
            product.save()

        text = self.create_text(user)
        self.send_telegram(text)
        #print(text)

        logout(request)        

        return Response(status=status.HTTP_200_OK, data='Заказ оформлен')

    def create_text(self, user):
        name = user.first_name
        email = user.email

        profile = user.profile
        city = profile.city
        street = profile.street
        house = profile.house
        number_phone = profile.number_phone
        comments = profile.comments

        items = str()
        for item in user.items.all():
            _id = item.item.id
            name_of_item = item.name
            price = item.price
            item_text = (f'Id товара:{_id}, наименование: {name_of_item},' 
                         f'цена: {price}\n')
            items = items + item_text

        total_price = user.items.aggregate(Sum('price'))['price__sum']
        
        text = (f'Новый заказ.\nимя: {name}\nпочта: {email}\nгород: {city}\n'
                f'улица: {street}\nдом: {house}\nтелефон: {number_phone}\n' 
                f'комментарии: {comments}.\nТовары:\n{items}\n'
                f'Общая стоимость: {total_price}'
        )
        return text
        
    def send_telegram(self, text):
           
        token = '5795557189:AAEocnU9A_Gc_2qFbhLcX7YwUUol3VE8cnY'
        method = 'sendMessage'
        url = f'https://api.telegram.org/bot{token}/{method}'

        chats_id = ['526043938', '214455581', ]

        for chat_id in chats_id:
            params = {'chat_id' : chat_id, 'text' : text}
            try:
                response = requests_lib.post(url=url, params=params)
            except RequestException as e:
                #print(e) 
                pass
        
