from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name="note_list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="detail_note"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="update_note"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="delete_note"),
    path('notes/new/', views.NotesCreateView.as_view(), name="create_note"),
    
]
