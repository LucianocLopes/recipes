from django.urls import include, path

from .views import RecipeListViewHome, RecipeListViewSearch, \
    RecipeListViewTag, RecipeListViewCategory, RecipeDetail

app_name = 'recipes'

urlpatterns = [
    path(
        '',
        RecipeListViewHome.as_view(),
        name="home"
    ),
    path(
        'recipes/search/',
        RecipeListViewSearch.as_view(),
        name="search"
    ),
    path(
        'recipes/tags/<slug:slug>/',
        RecipeListViewTag.as_view(),
        name="tag"
    ),
    path(
        'recipes/category/<int:category_id>/',
        RecipeListViewCategory.as_view(),
        name="category"
    ),
    path(
        'recipes/<int:pk>/',
        RecipeDetail.as_view(),
        name="recipe"
    ),
]
