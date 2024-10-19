# Automatización de Formularios con Selenium

## Descripción
Este proyecto utiliza Selenium para automatizar el llenado de formularios en línea. El script accede a un sitio web específico, extrae información sobre propiedades y completa un formulario de Google automáticamente. Este enfoque elimina la necesidad de intervención manual, ahorrando tiempo y reduciendo errores en el proceso de recolección de datos.

## Proceso de Automatización
1. **Acceso al Sitio Web**:  
   El script inicia un navegador web utilizando ChromeDriver. Se accede a la página que contiene la información de las propiedades.

2. **Extracción de Información**:  
   Se utilizan selectores de elementos para buscar y extraer información relevante sobre las propiedades, como precio, ubicación y características.

3. **Llenado del Formulario**:  
   Con los datos extraídos, el script navega al formulario de Google y lo llena automáticamente.

4. **Envío del Formulario**:  
   Finalmente, el script envía el formulario y puede mostrar un mensaje de confirmación.

## Requisitos
- Python 3.x
- Selenium
- ChromeDriver compatible con la versión de Chrome instalada

## Instalación
1. Clona este repositorio:

