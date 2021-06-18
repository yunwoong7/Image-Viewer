<h2 align="center">
  Image Viewer
</h2>

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.8-blue.svg"/>
  <img src="https://img.shields.io/badge/PyQt5-v5.15.4-blue.svg"/>
  <img src="https://img.shields.io/badge/opencv-v4.5.2.54-blue.svg"/>
  <img src="https://img.shields.io/badge/numpy-v1.20.3-blue.svg"/>
</div>

## Description

Image-Viewer 프로그램을 협업하여 개발하는 공간입니다.



## GUI Draft

Viewer 의 다양한 기능에 따라 GUI 형태는 변경 될 수 있으며 아래 그림은 단순히 시안이라고 보시면 됩니다.



시안1)

<div align="center">
  <img src="/images/draft/image_viewer1.jpg" width="100%">
</div>

시안2)

<div align="center">
  <img src="/images/draft/image_viewer2.jpg" width="100%">
</div>

시안3)

<div align="center">
  <img src="/images/draft/image_viewer3.jpg" width="100%">
</div>



## Features

- [ ] 이미지 파일 열기

- [ ] 폴더 열기

- [ ] 확대/축소

- [ ] 이미지 Fit Size

- [ ] Status bar (image size)

- [ ] 파일 리스트 (Tree Widget)

- [ ] 파일 목록 필터

- [ ] Drag & Drop 으로 이미지 파일 열기

  

## Structure

```
Image-Viewer/
├── libs/         
|  └── utils.py                              # 일반적으로 사용되는 편의 기능 모음
├── widgets/   
|  └── image_canvas.py                       # image를 보여주는 widget
├── UI/
|  └── image_viewer.ui                       # image_viewer ui 파일
├── main.py                                  # main 
├── res_rc.py                                # pyqt Resource File
└── config.ini                               # config file

```

