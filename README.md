# info de la materia: ST0263 Tópicos Espec. en Telemática
#
# Estudiante(s): Juan David Echeverri Villada, jdecheverv@eafit.edu.co
#
# Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co
#

# Reto 2
#
# 1. Breve descripción de la actividad
El proposito de esta actividad era probar estrategias de comunicacion tanto sincronas como asincronas, mediante el consumo dos microservicios simples, los requerimientos solicitados para la actividad propuesta fueron implementados en su totalidad

# 2. Información general de diseño de alto nivel y arquitectura
La aplicacion tiene un diseño simple, el cual consta de 4 componentes. Un API Gateway, implementado en Flask, que se encarga de decidir basado en disponibilidad que servicio se encargara de contestar la peticion. Cuenta tambien
con una conexion GRPC a una instancia con 2 microservicios (python), un MOM creado en rabbitMQ y por ultimo una instancia mas capaz de consumir los topicos creados en bigqueue para resolver las peticiones en caso de que la instancia 1 falle

# 3. Descripción del ambiente de desarrollo y técnico
Como lenguaje principal se uso python, y a continuacion se mencionan las librerias utilizadas:
- **grpcio**: 1.57.0
- **grpcio-tools**: 1.57.0
- **protobuf**: 4.24.2
- **pika**: 1.2.0
- **flask**: 2.0.1
- **flask-restful**: 0.3.9
- **python-dotenv**: 0.17.1

## Como se compila y ejecuta.
- Crear y ejecutar una instancia MOM con rabbitMQ server
 ```bash
  docker start rabbit-server
```
- Crear desde la interfaz de RabbitMQ: un par de colas queue1 y queue2, un exchange my_exchange y conectarlos por las routing keys: list_files y search_files respectivamente

- Clonar el proyecto en las demas instancias
```bash
  git clone https://github.com/Juanda0/jdecheverv-st0263.git
```
- Ir al directorio del proyecto
```bash
  cd jdecheverv-st0263/reto2
```
- Instalar las dependencias
```bash
  pip3 install -r requirements.txt
```
- Settear las variables de ambiente respecto al ejemplo `.env.example` y modificar el archivo `configs.py`
```bash
  mv .env.example .env
  nano .env
  nano configs.py
```
- Ejecutar api_gw (en su respectiva instancia)
```bash
  python3 api_gw.py
```
- Ejecutar instancia1 (en su respectiva instancia)
```bash
  python3 grpc_server.py
```
- Ejecutar instancia2 (en su respectiva instancia)
```bash
  python3 consumer.py
```
## Descripcion y configuracion del entorno
- Settear Configs.py
```python
  GRPC_RULE = '0.0.0.0:50051' #0.0.0.0 + puerto GRPC
  DIRECTORY = './resources' #Directorio de donde saldran los recurso a extraer
  GRPC_HOST = '34.234.253.43:50051' #Instancia 1, maquina que posee los servicios GRPC a usar
  API_GW_HOST = '0.0.0.0' #Escuchando internet desde el apiGW
  API_GW_PORT = 80 #Puerto del apigw
```

- Settear .env con la credenciales de RabbitMQ
```
  RMQ_HOST = localhost
  RMQ_PORT = 5672
  RMQ_USER = user
  RMQ_PASS = password
  RMQ_EXCHANGE = my_exchange
```
# IP o nombres de dominio en nube o en la máquina servidor.

- **IP MOM**: 54.221.117.48
- **IP E1**: 34.234.253.43
- **IP E2**: 54.152.148.230
- **IP API_GW**: 34.195.66.226

## Guia de usuario
#### listar todos los archivos:

```http
  curl --location '${API_GW_HOST}/list_files'
```

#### Buscar todos los archivos que matchean a un string:

```http
  curl --location '${API_GW_HOST}/search_files?file_name={file_name}'
```

## Resultados
<img width="738" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/397704e4-add8-4a6b-80ce-0f2991b1018e">
<img width="592" alt="image" src="https://github.com/Juanda0/jdecheverv-st0263/assets/61121948/1c0b5b79-cb9b-4d23-b17e-1e4bb024e185">

# Referencias:
- https://www.rabbitmq.com/getstarted.html
- https://github.com/st0263eafit/st0263-232/tree/main 

#### versión README.md -> 1.0 (2023-agosto)
