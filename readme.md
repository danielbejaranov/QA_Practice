# Instrucciones para Ejecutar las Pruebas Automatizadas

## Descripción del Repositorio
Este repositorio contiene dos proyectos de automatización de pruebas: uno basado en Selenium y otro en Cypress.

## Proyecto 1: Selenium [E2E]

### Descripción
Este proyecto automatiza un flujo de compra en la aplicación web [SauceDemo](https://www.saucedemo.com/). La prueba incluye la autenticación, la adición de productos al carrito, la verificación de precios, y la finalización de una compra, con capturas de pantalla tomadas en varios pasos clave.

### Requisitos Previos
1. **Python 3.x** debe estar instalado en el sistema.
2. **ChromeDriver** debe estar instalado y en el `PATH` del sistema para que Selenium pueda interactuar con el navegador Chrome.

### Instalación de Dependencias
Antes de ejecutar la prueba, asegúrese de que todas las dependencias necesarias estén instaladas. Puede hacerlo ejecutando:

```bash
pip install selenium
```

### Ejecución de las Pruebas
Para ejecutar las pruebas automatizadas en Selenium, siga estos pasos:

1. Navegue al directorio donde se encuentra el script de Selenium.
2. Ejecute el script utilizando Python:
   ```bash
   python test_purchases.py
   ```
3. Las capturas de pantalla generadas durante la prueba se guardarán en la carpeta `screenshots`.

### Archivos Importantes
- **test_report.txt**: Archivo de reporte generado por el proyecto de Selenium, que registra cada paso de la prueba y sus resultados.
- **screenshots/**: Carpeta donde se almacenan las capturas de pantalla tomadas durante la ejecución de la prueba.

---

## Proyecto 2: Cypress [APIs]

### Descripción
Este proyecto realiza pruebas de la API de PetStore, cubriendo escenarios como añadir una mascota, buscarla por ID, actualizar su estado, y verificar su información por estado.

### Requisitos Previos
1. **Node.js** debe estar instalado en el sistema.
2. **Cypress** debe estar instalado. Puede hacerlo ejecutando el siguiente comando en la terminal:

   ```bash
   npm install cypress --save-dev
   ```

### Instalación de Dependencias
Para instalar Cypress y las dependencias necesarias, navegue al directorio del proyecto y ejecute:

```bash
npm install
```

### Ejecución de las Pruebas
Para ejecutar las pruebas automatizadas en Cypress, siga estos pasos:

1. Navegue al directorio del proyecto Cypress.
2. Ejecute Cypress en modo consola:
   ```bash
   npx cypress run
   ```
3. Los reportes y capturas de pantalla generados se guardarán en la carpeta `cypress/reports` y `cypress/screenshots` respectivamente.

### Archivos Importantes
- **cypress/reports/**: Carpeta donde se almacenan los reportes generados por Cypress.
- **cypress/screenshots/**: Carpeta donde se almacenan las capturas de pantalla tomadas durante la ejecución de las pruebas.

---
