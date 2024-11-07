from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

app_name = 'notes'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', NoteListView.as_view(), name='note_list'),             
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),  
    path('note/add/', NoteCreateView.as_view(), name='note_add'),          
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note_edit'),  
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'), 
]
