# Pautas de Desarrollo y Estilo de Código (Equipo Quadtree)

Para garantizar consistencia y facilitar la integración modular de las ramas de desarrollo, todo el equipo debe seguir estas directrices:

1. **Estilo PEP 8:**
   - Indentación estricta de 4 espacios (prohibido el uso de tabs).
   - Longitud máxima de línea: 88–100 caracteres.
   - Nombres de clases en CapWords (ej. `QuadNode`, `Point`, `BoundingBox`).
   - Nombres de funciones, métodos y variables en snake_case (ej. `insert_point()`, `range_query()`).
   - Nombres de constantes en UPPER_SNAKE_CASE (ej. `DEFAULT_SEED`, `MAX_CAPACITY`).

2. **Tipado Estático Obligatorio (Type Hinting):**
   - Todas las funciones y métodos públicos deben declarar los tipos de sus argumentos y retornos usando las bibliotecas estándar `typing` o primitivas de Python 3.10+:
     ```python
     def insert(self, point: Point) -> bool:
         ...
     ```

3. **Documentación:**
   - Emplear docstrings (estilo Google o NumPy) en todas las clases y funciones principales detallando parámetros, retornos y excepciones.

4. **Reproducibilidad:**
   - Nunca utilizar funciones pseudoaleatorias sin fijar previamente una semilla (*seed*), especialmente en pruebas unitarias y benchmarks comparativos. Esto garantiza que las subdivisiones del Quadtree se comporten igual en los entornos de todos los desarrolladores.
