# Calculadora de Subnetting

Este programa permite calcular la información relevante sobre una red IP, tomando como entrada una dirección IP y un prefijo de máscara de subred. Utiliza la librería `ipaddress` de Python para calcular y mostrar los detalles esenciales de la red.

## Funcionalidades

### 1. Cálculos Básicos sobre la Red

- **Dirección de red**: Identifica la dirección que representa la red.
- **Máscara de subred**: Muestra la máscara de subred asociada al prefijo.
- **Dirección de broadcast**: Proporciona la dirección de broadcast, utilizada para enviar mensajes a todos los dispositivos en la red.
- **Rango de direcciones IP disponibles**: Muestra las primeras y últimas direcciones IP que se pueden asignar a dispositivos en la red, excluyendo la dirección de red y la dirección de broadcast.
- **Número de hosts disponibles**: Calcula cuántos dispositivos (hosts) se pueden conectar a la red, excluyendo las direcciones de red y broadcast.

### 2. Funcionalidades Adicionales (Valor Agregado)

#### 2.1 Validación Automática del Rango IP (Privada o Pública)

- **Descripción**: Verifica si la dirección IP ingresada es **privada** (utilizada en redes internas) o **pública** (accesible a través de Internet).
- **Valor Agregado**: Permite identificar rápidamente si la IP es adecuada para un entorno interno (red doméstica o LAN) o si debe ser enroutable a través de Internet. Además, ayuda a detectar posibles errores en la elección de direcciones.

#### 2.2 Clasificación de la Dirección IP por Clase (A, B, C, etc.)

- **Descripción**: El programa determina la **clase de la dirección IP** (A, B, C, D o E) basándose en el primer octeto de la dirección IP y proporciona una descripción del uso típico de esa clase.
- **Valor Agregado**: Ayuda a los usuarios a comprender cómo se clasifica la dirección en función del tamaño de la red o su propósito (por ejemplo, redes privadas, redes grandes de empresas, multicast, etc.). También contextualiza la dirección IP dentro de un sistema de clasificación bien conocido en redes.

#### 2.3 Exportación de Resultados a un Archivo CSV

- **Descripción**: Después de calcular la información de la red, el programa guarda los resultados en un archivo **CSV** que contiene datos como la dirección IP, el prefijo, la dirección de red, la máscara de subred, la dirección de broadcast, el rango de IPs disponibles y el número de hosts.
- **Valor Agregado**: Permite a los usuarios guardar y documentar los resultados de manera ordenada, facilitando la reutilización de la información en otros proyectos o análisis. Los archivos CSV también son fácilmente accesibles para herramientas de análisis y procesamiento de datos.


