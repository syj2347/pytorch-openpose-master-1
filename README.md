## pytorch-openpose

### Getting Started

#### Install Requriements

Create a python 3.7 environement, eg:

    conda create -n pytorch-openpose python=3.7
    conda activate pytorch-openpose

Install pytorch by following the quick start guide here (use pip) https://download.pytorch.org/whl/torch_stable.html

Install other requirements with pip

    pip install -r requirements.txt

#### Download the Models

* [dropbox](https://www.dropbox.com/sh/7xbup2qsn7vvjxo/AABWFksdlgOMXR_r5v3RwKRYa?dl=0)
* [baiduyun](https://pan.baidu.com/s/1IlkvuSi0ocNckwbnUe7j-g)
* [google drive](https://drive.google.com/drive/folders/1JsvI4M4ZTg98fmnCZLFM-3TeovnCRElG?usp=sharing)

`*.pth` files are pytorch model, you could also download caffemodel file if you want to use caffe as backend.

Download the pytorch models and put them in a directory named `model` in the project root directory

#### Run the Demo

Run:

    python demo_camera.py


to use a image from the images folder or run 

    python output.py

to process a video file (requires [ffmpeg-python][ffmpeg]).

[ffmpeg]: https://pypi.org/project/ffmpeg-python/

#### Settings

##### demo_camera

line 23

    option : with bg: 0 else 1



line 32

    To avoid duplicate processing of images.


##### output

line 9

    done_set : Folder names that do not require processing.

line 30,31


    st && ed : The starting and ending sequence numbers of the image series that need to be processed in the target folder. This is done to handle the images in batches when there are a large number of them, in order to prevent exceeding the memory limit.
