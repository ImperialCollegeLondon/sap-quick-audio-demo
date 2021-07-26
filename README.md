# sap-quick-audio-demo
Make and serve a webpage to quickly compare audio files.  This is really handy when you want to listen to different processing treatments applied an audio file with having to fire up a DAW.

The core functionality of the generated webpage is provided by the excellent [trackswitch project](https://github.com/audiolabs/trackswitch.js). Here we use python to grab all the audio files in a particular folder, create the html and then use docker to wrap everything in a standalone container. Tested using python 3 on macOS but should work in other operating systems.

## Pre-requisites
Install and run the Docker daemon using [these instructions](https://docs.docker.com/install/).

Install anaconda using [these instructions](https://docs.anaconda.com/anaconda/install/index.html). This step is probably overkill but is an easy way to make sure all the correct dependencies are satisfied.



## Install
Follow these steps in the terminal

```
git clone https://github.com/ImperialCollegeLondon/sap-quick-audio-demo.git
cd sap-quick-audio-demo
conda env create -n sapdemo -f=conda_env.yml
conda activate sapdemo
```

## Run
```
python make_demo.py <source_dir> <demo_title> 
```

where

`<source_dir>` is the path to a folder containing the wav files to be included, and

`<demo_title>` is an optional string added to the webpage tab

## Finish
```
python kill.py 
```