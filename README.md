# Object Tracking

_Acá va un párrafo que describa lo que es el proyecto_


## Quick Start Example 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

```Bash
git clone 
docker-compose up
```

> **A:** Because you don't want to test the code, you want to test the *program*.

    .
    ├── ...
    ├── data-io                  # Test files (alternatively `spec` or `tests`)
    │   ├── input                # Load and stress tests
    │   │   ├── integration      # End-to-end, integration tests (alternatively `e2e`)
    │   │   └── input.mkv        # Unit tests
    │   └── output               # Unit tests
    │       └── output.mkv       # Unit tests
    └── ...
    


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

> **C:** Because you don't want to test the code, you want to test the *program*.
<img src="https://user-images.githubusercontent.com/84106110/156943548-1ee3ff9e-1e21-4caa-8e47-fd871d818f19.png" width=30% height=30%>

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
















