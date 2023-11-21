from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('create-book', create_book, name='create_book'),
    path('show-html', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/<int:id>', edit_product, name='edit'),
    path('delete/<int:id>', delete_product, name='delete'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_product_ajax/', delete_product_ajax, name='delete_product_ajax'),
    path('', show_main, name='show_main'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]

