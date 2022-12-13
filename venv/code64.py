import base64

Codigo_Base64 = input('cole aqui ')
base64_bytes = Codigo_Base64.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
decodificado = message_bytes.decode('ascii')

print(decodificado)
