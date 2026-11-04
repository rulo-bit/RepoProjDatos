## Configuración del Proyecto y Entorno

### Requisitos Previos
* **Python 3.10+** (recomendado Python 3.11 o 3.12).
  * *Justificación:* Proporciona un rendimiento optimizado en la máquina virtual de Python, mejor tipado estático (typing con operadores de unión nativos tipo `int | float`), y mensajes de error sintáctico más precisos para depuración en equipo.

### Instalación
Clona el repositorio y configura un entorno virtual aislado para no afectar tus paquetes globales:

```bash
# Crear y activar entorno virtual
python -m venv .venv
# En Windows: .venv\Scripts\activate
# En macOS/Linux: source .venv/bin/activate
```
# Dependencias base para cálculo matricial y graficación
numpy>=1.26.0,<2.0.0
matplotlib>=3.8.0,<4.0.0

# Herramientas de pruebas y validación estática
pytest>=7.4.0
mypy>=1.5.0
black>=23.7.0
