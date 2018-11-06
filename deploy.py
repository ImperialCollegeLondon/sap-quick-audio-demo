# based on examples at https://smarketshq.com/how-to-use-docker-py-307f4029cf
import os
import sys
#from docker import Client
import docker

def deploy(demo_name):
    demo_name = 'audio-demo'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_name = 'webserver-image'
    
    ## do it using from_env() - v2 no checking, have to stop container using command line
    client = docker.from_env()
    client.images.build(path=dir_path, tag=image_name)
    container = client.containers.run(
        image_name,
        ports={80:80},
        name=demo_name,
        detach=True,
    )
    
if __name__ == "__main__":
    import sys
    demo_name = 'audio-demo'
    # if len(sys.argv) > 0:
    #     demo_name = sys.argv[1]
    #     demo_name = ''.join(demo_name.split()) #endure there is no white space
    # print(demo_name)
    deploy(demo_name)