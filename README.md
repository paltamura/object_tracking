# Object Tracking

_Acá va un párrafo que describa lo que es el proyecto_


## Quick Start Example 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

```Bash
git clone https://github.com/paltamura/object_tracking.git
docker-compose up
```

## Custom Example

> **A:** Because you don't want to test the code, you want to test the *program*.

    .
    ├── ...
    ├── data-io
    │   ├── input
    │   │   ├── integration      <- End-to-end, integration tests (alternatively `e2e`)
    │   │   └── input.mkv        <- Unit tests
    │   └── output
    │       └── output.mkv       <- Unit tests
    └── ...

> **B:** Because you don't want to test the code, you want to test the *program*.
```Bash
docker-compose up
```

## Custom Example

> **B:** Use diagram.
```mermaid
  graph TD;
      main-->MultiTracker;
      main-->Helper;

      MultiTracker-->OpenCV;
      MultiTracker-->H264Writer;
      MultiTracker-->Helper;

      H264Writer-->PIL;
      H264Writer-->subprocess;
      subprocess-->FFmpeg;
      
```

> **D:** Because you don't want to test the code, you want to test the *program*.
<img src="https://user-images.githubusercontent.com/84106110/156944048-a6efe75f-6773-446f-a057-3b9b9442c1fe.png" width=30% height=30%>

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles


---
⌨️ con ❤️ por [paltamura](https://github.com/paltamura) 😊
















