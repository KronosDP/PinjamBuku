from django.urls import path
from main.views import show_main, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id, show_html, register, login_user, logout_user, edit_product, delete_product 

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
    path('', show_main, name='show_main'),
]

