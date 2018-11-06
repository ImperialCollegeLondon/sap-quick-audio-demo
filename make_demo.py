import sys
import make_html
import webbrowser
import deploy

def main(source_path,demo_title):
    image_name='audio-demo'
    make_html.make_html(source_path,demo_title)
    deploy.deploy(image_name)
    #docker build -t webserver-image:v1 .
    #docker run -d -p 80:80 --rm --name audio-demo webserver-image:v1 
    webbrowser.open_new_tab('http://localhost')

if __name__ == "__main__":
    demo_title = 'audio demo'
    if len(sys.argv) < 2:
        print("Usage python make_demo.py path_to_audio [demo_title]")
    else:
        source_path = sys.argv[1]
        if len(sys.argv) >= 2:
            demo_title = sys.argv[2]
        main(source_path,demo_title)