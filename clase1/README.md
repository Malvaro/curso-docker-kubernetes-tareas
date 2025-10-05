# Clase 1 - Introducción a Containers y Docker

## Objetivo

Practicar el despliegue de diferentes tipos de aplicaciones usando docker run y documentar el proceso de cada una.

## Opcion seleccionada para desplegar
Opción 1: Apache HTTP Server (httpd)
Despliega un servidor web Apache:

Imagen: httpd
Puerto: 8081
Nombre del container: mi-apache
Verifica accediendo a http://localhost:8081

## Desarrollo
Antes de iniciar se verifica todos los Containers (iniciado y detenidos)

docker ps -a


### 1. Ejecutar el container

```bash
docker run -d -p 8081:80 --name mi-apache httpd
```

**Explicación:** Este comando crea y ejecuta un container con httpd en segundo plano (-d), mapeando el puerto (-p) 8081 de mi mac al puerto 80 del container, ademas se le da el nombre de mi-apache.

**Salida:**
```bash
Unable to find image 'httpd:latest' locally
latest: Pulling from library/httpd
887db3982a68: Pull complete 
e363695fcb93: Pull complete 
4f4fb700ef54: Pull complete 
8c9dc019f7b6: Pull complete 
480284c75fe2: Pull complete 
17aa38de890a: Pull complete 
Digest: sha256:ca375ab8ef2cb8bede6b1bb97a943cce7f0a304d5459c05235b47bc2dccb98cd
Status: Downloaded newer image for httpd:latest
98b17e174b1ff5900e033d534ef491ed1a9c592063f90b5952f973f16deeb6f9
```

### 2. Verificar que está corriendo
Para verificar que el Container esta corriendo se hara listara los contenedores iniciados
```bash
docker ps
```
Que muestra lo siguiente:

**Screenshot:**

![Container corriendo](screenshots/docker-ps-verificacion.png)

Tambien se revisa los logs del Container:
```bash
docker logs mi-apache
```
**Screenshot:**

![Container corriendo](screenshots/docker-logs.png)

### 3. Acceder desde el navegador

Se accede a `http://localhost:8081` y obtuve:

![Container funcionando](screenshots/httpd-localhost.png)

Con todo esto se verifico que el Container se levanto.

### 4. Limpieza
En este apartado se procedera con la limpieza:
Detener el container
```bash
docker stop 98b
```
Se uso los tres (3) primeros caracteres del ID del container dentro del comando.
![Container funcionando](screenshots/docker-stop.png)

Verificar container detenido
```bash
docker ps
```
Verificar container detenido
```bash
docker ps -a
```

La ejecuciòn de los dos comandos se observa en: 

![Container funcionando](screenshots/docker-ps-ps-a.png)


Eliminar Container
```bash
docker rm 98b
```
Verificar eliminacion del Container
```bash
docker ps -a
```

Se uso los tres (3) primeros caracteres del ID del container dentro del comando, se verifica la eliminacion del Container con el comando ps -a esto para listar todos los contenedores.
![Container funcionando](screenshots/docker-rm-ps-a.png)

## Conclusiones

En este ejercicio se aplico: inicio de un contenedor en segundo plano, con un puerto y nombre definifo (docker run -d -p --name), listar contenedores activos (docker ps), todos los contenedores activos e inactivos (docker ps -a), revisar logs del contenedor (docker logs), detener (docker stop) y eliminar el contenedor (docker rm)
