# sap-quick-audio-demo
Make and serve a webpage to compare audio files. Uses docker to wrap everything in a standalone container. Tested using python 3.

##Installation

```
git clone https://github.com/ImperialCollegeLondon/sap-quick-audio-demo.git
cd sap-quick-audio-demo
pip3 install -r requirements.txt
```

##Run
```
python3 make_demo.py <source_dir> <demo_title> 
```
where `source_dir` is the path to a folder containing the wav files to be included and `demo_title` is an optional string.

##Finish
```
python3 kill.py 
```