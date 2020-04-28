


''' 
================================================================================ 
================================================================================ 
                            APP-LEVEL URLS.PY: note_app 
================================================================================ 
================================================================================ 
''' 



from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('register/', views.register), 
    path('update/<int:id>', views.updateNote), 
    path('updateRender/<int:id>', views.update), 
    path('delete/<int:id>', views.deleteNote), 

] 









