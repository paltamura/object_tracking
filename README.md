# Object Tracking

A tracking algorithm consists of predicting the position of an object in a given frame knowing the position of said object in the previous frame. In general, in the area of Computer Vision, the position of an object in an image is defined from a rectangle (usually known as a Bounding Box) so that, when the rectangle is drawn on the image, the object is inside. of the rectangle.

This system allows tracking different objects in a video.
The system accepts as input parameters the video, which is going to be processed, and a file in JSON format where the initial state of each of the objects to be tracked is defined.

In the JSON file you will find, among other things, the bounding box of each object in tuple format (x, y, width, height) where x, y represent the coordinates of the pixels in the upper left corner of the bounding box, width y height son is the width and height, in pixels, of the bounding box.
As output, the system generates a video with the data obtained from the tracking. The video shows each frame with the bounding boxes obtained for each of the defined objects.


## Quick Start Example 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

```Bash
git clone https://github.com/paltamura/object_tracking.git
docker-compose up
```

## Custom Data Example

> **A:** To test your data, you need to replace the initial_conditions.json and input.mkv files in the input folder with your own files.

    .
    ├── ...
    ├── data-io
    │   ├── input
    │   │   ├── initial_conditions.json   <- replace with your file
    │   │   └── input.mkv                 <- replace with your file
    │   └── output
    │       └── output.mkv                
    └── ...

> **B:** And then run docker-compose again...
```Bash
docker-compose up
```

## Expected results in one frame of video output 
<img src="https://user-images.githubusercontent.com/84106110/156944048-a6efe75f-6773-446f-a057-3b9b9442c1fe.png" width=30% height=30%>

## Development notes 

To solve the main process (object tracking) it was decided to use the OpenCV Tracker, since it meets the expectations of the project.

The input video file is read and converted to frames with the help of OpenCV. After processing it is compressed and persisted using FFmpeg as a process called from python through subprocess.

All relevant configurations have been identified and added to a configuration file “configuration.ini”, which is handled by configparser.

To handle logging it was decided to use the python logging module directly. The level of verbosity is managed from the configuration file.

To organize the system and python environment prerequisites, the files requirements.system.txt with the system dependencies and requirements.txt with the python dependencies were created.

To simplify the deployment, a Dockerfile was created from where the environment is prepared and the tracking system is executed.

A docker-compose.yml file was also created in which the construction of the docker image is invoked, and a volume is established for the exchange of files between local and container.

## High level usage diagram

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


## Construido con 🛠️

_Herramientas utilizadas para crear este proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

---
⌨️ con ❤️ por [paltamura](https://github.com/paltamura) 😊
















