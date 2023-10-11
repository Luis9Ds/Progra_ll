from django.urls import path , include
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', login_required (views.inicio), name='inicio'),
    path('nosotros/', login_required(views.nosotros), name='nosotros'),
    path('peliculas/', login_required (views.peliculas), name='peliculas'),
    path('peliculas/crear', login_required (views.crear), name='crear'),
    path('peliculas/editar/<int:id>',login_required (views.editar), name='editar'),
    path('peliculas/form', login_required(views.form), name='forms'),
    path('peliculas/eliminar/<int:id>',login_required (views.eliminar), name='eliminar'),
    path('accounts/', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Esto es para agregar imagenes
#Finalmente lo logre, fue un dolor descubrir como forzar el inicio de Sesión pero mi error era querer enforcarlo en views.py donde era mas complicado, descubri que era mas sencillo de lo que parecia, cuando descubri ese import de django, todo fue como un coca cola en el desierto, y encima aplicarlo fue facil, nomas tenia que llamar el login_required en cada ruta, si quisiera podria simplemente dejarlo en todos menos el views inicio, pero en este caso mejor lo deje como esta.