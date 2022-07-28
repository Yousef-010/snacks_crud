from django.urls import path
from .views import SnackCreateView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView

urlpatterns = [
    # SnackListView page, GET ''
    path("", SnackListView.as_view(), name="snack_list"),

    # SnackDetailView it needs and id, GET /id/
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),

    # SnackCreateView it needs an id , POST 'create/'
    path("create/", SnackCreateView.as_view(), name="snack_create"),

    # SnackUpdateView it needs an id , POST '/id/update/'
    path("<int:pk>/update/", SnackUpdateView.as_view(), name="snack_update"),

    # SnackDeleteView it needs an id , POST '/id/delete/'
    path("<int:pk>/delete/", SnackDeleteView.as_view(), name="snack_delete"),
]

