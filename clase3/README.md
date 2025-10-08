
# APP-3 - NGINX - PostgreSQL - PGADMIN

**Curso:** Docker & Kubernetes - Clase 3
**Estudiante:** Alvaro Chambi

Uso de docker compose para crear dos contenedores con dos servicios, conectados en red, y con un volumen persistente.


## Stack

- **App:** HTML (Estatico)
- **Base de datos:** PostgreSQL

## Ejecución

1. Clonar:
   ```bash
   git clone git clone https://github.com/Malvaro/curso-docker-kubernetes-tareas.git
   cd curso-docker-kubernetes-tareas/clase3
   ```
2. Levantar servicios:
```bash
   docker compose up -d
   
```
Salida:
```bash
   [+] Running 28/28
 ✔ pgadmin Pulled                                                                                                    16.4s 
   ✔ 7033ff54060b Pull complete                                                                                       0.7s 
   ✔ 62da1fa39b79 Pull complete                                                                                       1.8s 
   ✔ cd143414c82f Pull complete                                                                                       2.6s 
   ✔ e658466a1775 Pull complete                                                                                       8.0s 
   ✔ fd7418e95f0b Pull complete                                                                                       1.4s 
   ✔ b7820c72be45 Pull complete                                                                                       8.1s 
   ✔ 249358622cb4 Pull complete                                                                                       8.4s 
   ✔ 547cba8c67b7 Pull complete                                                                                       9.1s 
   ✔ 97d078d99c0d Pull complete                                                                                       8.7s 
   ✔ cf0f9d5e8635 Pull complete                                                                                       1.5s 
   ✔ 378724f09254 Pull complete                                                                                       1.4s 
   ✔ bca4290a9639 Pull complete                                                                                       1.7s 
   ✔ ad209e34b1fd Pull complete                                                                                       2.0s 
   ✔ 8ed7b2b6c5ae Pull complete                                                                                       1.4s 
   ✔ 3ff1dc7483da Pull complete                                                                                       2.0s 
   ✔ c0348ea17019 Pull complete                                                                                       2.0s 
 ✔ db Pulled                                                                                                         14.7s 
   ✔ 7a7edd166a1d Pull complete                                                                                       0.3s 
   ✔ f5a288bc504e Pull complete                                                                                       7.4s 
   ✔ 04822b0e85a9 Pull complete                                                                                       7.4s 
   ✔ 1a214222c267 Pull complete                                                                                       0.5s 
   ✔ c6344925d395 Pull complete                                                                                       0.6s 
   ✔ 5efa8c2fd616 Pull complete                                                                                       1.0s 
   ✔ 80bb30b4ed9b Pull complete                                                                                       0.9s 
   ✔ cf96bfc6eef5 Pull complete                                                                                       0.9s 
   ✔ fbf147f36307 Pull complete                                                                                       0.8s 
   ✔ c349e820a786 Pull complete                                                                                       0.8s 
[+] Running 6/6
 ✔ Network clase3_frontend        Created                                                                             0.0s 
 ✔ Network clase3_backend         Created                                                                             0.0s 
 ✔ Volume "clase3_postgres-data"  Created                                                                             0.0s 
 ✔ Container postgres_db          Started                                                                             0.9s 
 ✔ Container pgadmin_web          Started                                                                             0.4s 
 ✔ Container nginx_web            Started                                                                             0.5s 
   
```



## PRUEBA
Acceder a:

NGINX: http://localhost:3000
PGADMIN: http://localhost:5050 

## Verificación

   1. Servicios corriendo:

      ```bash
      docker compose ps
      ```
      Salida: 

   2. Acceder:

      Nginx: http://localhost:8080
   
      PgAdmin: http://localhost:5050  

   3. Verificar volumen persiste:
      ```bash
      docker compose down
      docker compose up -d
      docker volume ls  # debe seguir existiendo
      ```

## Screenshots
### Git Clone
![git clone](screenshots/services.png)

### Acceso a Tarea 3
![git clone](screenshots/services.png)

### Docker Compose
![docker compose](screenshots/services.png)

### Levantar servicios
![docker ps](screenshots/services.png)

### Nginx
![git clone](screenshots/services.png)

### PGAdmin
![git clone](screenshots/services.png)

### Configuraciòn PgAdmin
![git clone](screenshots/services.png)


6. Conceptos Aplicados
## Conceptos Docker

- Docker Compose con 3 servicios: Nginx, PostgreSQL y Pgadmin
- Red custom: `app-network`
- Volumen: `db-data` (persistencia)
