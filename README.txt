# Video Evolution

## What is it ?

Video Evolution is a python program that allows you to detect moving pixels in videos.

Video | Output image
- | -
[![Video](https://img.youtube.com/vi/cG_7OxVTfgc/0.jpg)](https://www.youtube.com/watch?v=cG_7OxVTfgc) | ![Output image](https://i.imgur.com/bLwxt2j.jpg)

## How to use it ?

To run Video Evolution, you need to go to the folder where main.py is located and run:
```
python main.py dog.mp4 -j 100 -t 20
```
The jump [-j] and threshold [-t] parameter are not required, which means you can also do:
```
python main.py dog.mp4
```

## Requirements

- [openCV](https://pypi.org/project/opencv-python/)
