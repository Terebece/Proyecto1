# Proyecto1: Chat con Python

Universidad Nacional Autónoma de México

Facultad de Ciencias

Modelado y Programación

Becerril Torres Teresa

Número de cuenta: 315045132

En este proyecto se realizará un chat en Python, para el cual crearemos
un cliente-servidor utilizando sockets y threadings, basandose en el patrón MVC.

## Requisitos

* Lenguaje: Python
* Versión: 3.7.0
* Pruebas Unitarias: unittest
* interfaz gráfica: Tkinter

## Clonar chat
Para clonar el chat utilice el siguiente comando

    https://github.com/Terebece/Proyecto1.git

## Ejecutar chat
Una vez que lo haya clonado, para ejecutar el chat lo primero que tiene que
ejecutar es el servidor utilizando el siguiente comando

    ./server.sh 

A continuación, cada vez que quiera ejecutar un cliente utilice el siguiente
comando

    ./client.sh
    
    Enter host: 0.0.0.0
    Enter port: 1234

En host puede ir cualquier dirección IP, ya que el servidor esta adaptado para
aceptar cualquier dirección IP.

## Documentación

La documentación se generará con el siguiente comando

    ./doc.sh

## Pruebas Unitarias

Para ejecutar las pruebas unitarias utilice el comando

    ./test.sh
