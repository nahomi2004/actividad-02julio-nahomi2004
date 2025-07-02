
from django.urls import path
# se importa las vistas de la aplicación
from administrativo import views

urlpatterns = [
        path('', views.index, name='index'),
        
        path('detalle/matricula/<int:id>', views.detalle_matricula,
            name='detalle_matricula'),
        
        path('crear/nueva/matricula', views.crear_matricula,
            name='crear_matricula'),
        
        path('editar/matricula/<int:id>', views.editar_matricula,
                name='editar_matricula'),
        
        path('detalle/estudiante/<int:id>', views.detalle_estudiante,
            name='detalle_estudiante'),

        # URLs nuevas
        path('lista_modulos', views.lista_modulos, name='lista_modulos'),
        
        path('listar_estudiantes', views.listar_estudiantes, name='listar_estudiantes'),
        
        # crear_modulo
        path('crear_modulo', views.crear_modulo, name='crear_modulo'),
        
        # crear_estudiantes
        path('crear_estudiantes', views.crear_estudiantes, name='crear_estudiantes'),
 ]
