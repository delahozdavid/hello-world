import requests

url = 'https://7f77-2806-230-6014-bee0-8018-afbe-b0c3-fcbc.ngrok-free.app'

# Datos para enviar mediante una solicitud POST
datos_registro = {
    "correo": "castrodavidd@hotmail.com",
    "nombre": "David Castro Encinia"
}

# Datos para enviar mediante una solicitud GET para buscar por correo
correo_a_buscar = "castrodavidd@hotmail.com"



try:
    # Enviar una solicitud POST para registrar los datos
    response_post = requests.post(url, json=datos_registro)
    
    # Verificar si la solicitud POST fue exitosa (código de estado 201)
    if response_post.status_code == 201:
        print("Datos enviados correctamente!")
        
        # Si la solicitud POST fue exitosa, hacer una solicitud GET para obtener los datos
        # asociados al correo específico
        params = {"correo": correo_a_buscar}
        response_get = requests.get(url, params=params)
        
        # Verificar si la solicitud GET fue exitosa (código de estado 200)
        if response_get.status_code == 200:
            print("Datos recibidos correctamente:")
            print(response_get.json())
        else:
            print("Error al obtener los datos:", response_get.status_code)
    else:
        print("Error al enviar los datos:", response_post.status_code)
        
except requests.RequestException as e:
    print("Error:", e)
