from firebase_admin import storage
from uuid import uuid4
import firebase_admin
from firebase_admin import credentials, storage

# Ruta al archivo JSON descargado desde Firebase Console
cred = credentials.Certificate("/home/abisai/Escritorio/escuela/adm/RCP/RDP/RC/Scripts/key.json")

# Inicializar Firebase
firebase_admin.initialize_app(cred, {
    'storageBucket': 'felipe-proyectos.appspot.com'
})


def subir_imagen_usuario_a_firebase(user, file):
    """
    Sube una imagen al almacenamiento de Firebase organizándola por usuario.

    Args:
        user_id (str): .
        file: Archivo tipo `InMemoryUploadedFile` o archivo binario.

    Returns:a
        str: URL pública de la imagen subida.
    """
    # Generar un nombre único para la imagen
    nombre_archivo = f"{uuid4()}.png"  

    # Definir la ruta en Firebase (carpeta por usuario)
    ruta_archivo = f"imagenes/{user}/{nombre_archivo}"

    # Obtener una referencia al bucket
    bucket = storage.bucket()

    # Crear un blob en la ruta del bucket y subir la imagen
    blob = bucket.blob(ruta_archivo)
    blob.upload_from_file(file, content_type=file.content_type)

    # Hacer que el archivo sea público
    blob.make_public()

    # Retornar la URL pública
    return blob.public_url

