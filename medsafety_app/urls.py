from django.urls import path
from .views import web_views, api_views

urlpatterns = [
    # Web views
    path('', web_views.index, name='index'),
    path('login', web_views.login_page, name='login'),
    path('register', web_views.register_page, name='register'),
    path('dashboard', web_views.dashboard, name='dashboard'),
    path('saved', web_views.saved_medicines_page, name='saved_medicines'),
    path('search', web_views.search_page, name='search'),
    path('scanner', web_views.scanner_page, name='scanner'),
    path('interaction', web_views.interaction_page, name='interaction'),
    path('medicine/ai', web_views.medicine_ai_detail_page, name='medicine_ai_detail'),
    path('medicine/<int:id>', web_views.medicine_detail_page, name='medicine_detail'),

    # API views
    path('api/auth/login', api_views.login_api, name='login_api'),
    path('api/auth/register', api_views.register_api, name='register_api'),
    path('api/auth/logout', api_views.logout_api, name='logout_api'),
    
    path('api/medicines/search', api_views.search_medicine_api, name='search_medicine_api'),
    path('api/medicines/<int:id>', api_views.get_medicine_api, name='get_medicine_api'),
    
    path('api/user/save/<int:medicine_id>', api_views.save_medicine_api, name='save_medicine_api'),
    path('save/<int:medicine_id>', api_views.unsave_medicine_api, name='unsave_medicine_api'),
    path('save/status/<int:medicine_id>', api_views.check_save_status_api, name='check_save_status_api'),
    
    path('api/user/recent-searches', api_views.recent_searches_api, name='recent_searches_api'),
    path('api/user/saved', api_views.saved_medicines_api, name='saved_medicines_api'),
    path('api/user/search-history', api_views.log_search_history_api, name='log_search_history_api'),
    path('search-history', api_views.log_search_history_api, name='log_search_history_api_alias'),
    
    path('api/ai/interaction', api_views.check_interaction_api, name='check_interaction_api'),
    path('api/medicines/scan', api_views.scan_prescription_api, name='scan_prescription_api'),
    path('api/ocr/scan', api_views.scan_prescription_api, name='scan_prescription_api_alias'),
]
