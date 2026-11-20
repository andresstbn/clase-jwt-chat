from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from chat.models import Canal, Mensaje

CANALES = {
    'general': 'Avisos y conversación del curso',
    'dudas-django': 'Preguntas sobre el backend',
    'react': 'Todo lo del frontend',
    'random': 'Cualquier otra cosa',
}

# (canal, autor, texto), en orden cronológico.
MENSAJES = [
    ('general', 'ana', 'Hola, ¿ya quedó montado el chat del curso?'),
    ('general', 'beto', 'Sí, acabo de crear los canales. Falta que entre el resto.'),
    ('general', 'ana', 'Listo. ¿La entrega del proyecto sigue para el viernes?'),
    ('general', 'beto', 'Sí, viernes a medianoche. El profe dijo que no hay prórroga.'),
    ('general', 'ana', 'Entonces toca repartirnos el trabajo hoy.'),
    ('general', 'beto', 'Yo tomo el backend y tú el frontend, ¿te sirve?'),
    ('general', 'ana', 'Me sirve. Cualquier cosa nos escribimos por aquí.'),
    ('dudas-django', 'beto', '¿Alguien sabe por qué me sale 401 cuando hago POST a /api/mensajes/?'),
    ('dudas-django', 'ana', 'Porque no estás mandando el token. Leer es libre, pero escribir pide login.'),
    ('dudas-django', 'beto', '¿Y el token de dónde lo saco?'),
    ('dudas-django', 'ana', 'Haces POST a /api/token/ con usuario y contraseña y te devuelve access y refresh.'),
    ('dudas-django', 'beto', '¿Y después cómo lo mando?'),
    ('dudas-django', 'ana', 'En el encabezado: Authorization: Bearer y el access.'),
    ('dudas-django', 'beto', 'Funcionó. ¿Y cuando se vence?'),
    ('dudas-django', 'ana', 'Pides otro en /api/token/refresh/ con el refresh. Eso lo vemos en clase.'),
    ('react', 'ana', 'Ya tengo la lista de canales pintando con fetch.'),
    ('react', 'beto', '¿Usaste axios?'),
    ('react', 'ana', 'No, fetch a secas. Para lo que necesitamos alcanza.'),
    ('react', 'beto', '¿Dónde vas a guardar el token cuando haya login?'),
    ('react', 'ana', 'Todavía no sé. Tengo el formulario listo pero sin conectar.'),
    ('react', 'beto', 'Dejémoslo así, eso lo conectamos en la clase.'),
    ('random', 'beto', '¿Alguien va a la cafetería? Tráiganme un tinto.'),
    ('random', 'ana', 'Voy en diez minutos. ¿Con azúcar?'),
    ('random', 'beto', 'Sin azúcar, gracias.'),
    ('random', 'ana', 'Me debes dos ya, por cierto.'),
]


class Command(BaseCommand):
    help = 'Carga usuarios, canales y mensajes de prueba. Se puede correr varias veces.'

    def handle(self, *args, **options):
        User = get_user_model()
        usuarios = {}
        for nombre, clave, es_admin in [
            ('ana', 'clave-ana-123', False),
            ('beto', 'clave-beto-123', False),
            ('admin', 'admin123', True),
        ]:
            usuario, _ = User.objects.get_or_create(username=nombre)
            usuario.set_password(clave)
            usuario.is_staff = usuario.is_superuser = es_admin
            usuario.save()
            usuarios[nombre] = usuario

        Canal.objects.filter(nombre__in=CANALES).delete()  # borra también sus mensajes
        canales = {
            nombre: Canal.objects.create(nombre=nombre, descripcion=descripcion, creador=usuarios['ana'])
            for nombre, descripcion in CANALES.items()
        }

        # Un mensaje cada 7 minutos, terminando ahora. `creado` es auto_now_add,
        # así que la fecha se fija con update() después de crear.
        inicio = timezone.now() - timedelta(minutes=7 * len(MENSAJES))
        for i, (canal, autor, texto) in enumerate(MENSAJES):
            mensaje = Mensaje.objects.create(canal=canales[canal], autor=usuarios[autor], texto=texto)
            Mensaje.objects.filter(pk=mensaje.pk).update(creado=inicio + timedelta(minutes=7 * i))

        self.stdout.write(self.style.SUCCESS(
            f'Listo: {len(usuarios)} usuarios, {len(canales)} canales y {len(MENSAJES)} mensajes.'
        ))
