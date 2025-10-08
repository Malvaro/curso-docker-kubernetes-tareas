1. Encabezado
# APP-3 - NGINX - PostgreSQL

**Curso:** Docker & Kubernetes - Clase 3
**Estudiante:** Alvaro Chambi

Uso de docker compose para crear dos contenedores con dos servicios, conectados en red, y con un volumen persistente.

2. Stack Tecnológico
## Stack

- **App:** HTML (Estatico)
- **Base de datos:** PostgreSQL

3. Cómo Ejecutar
## Ejecución

1. Clonar:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
Levantar servicios:

docker compose up -d
Acceder:

API: http://localhost:3000

### 4. Cómo Probar

```markdown
## Verificación

1. Servicios corriendo:
   ```bash
   docker compose ps
Acceder a la web: http://localhost:XXXX

Verificar volumen persiste:

docker compose down
docker compose up -d
docker volume ls  # debe seguir existiendo

### 5. Capturas de Pantalla

```markdown
## Screenshots

### Servicios corriendo
![compose ps](screenshots/services.png)

### API funcionando
![API](screenshots/api.png)
6. Conceptos Aplicados
## Conceptos Docker

- Docker Compose con 2 servicios
- Red custom: `app-network`
- Volumen: `db-data` (persistencia)
- Variables de entorno