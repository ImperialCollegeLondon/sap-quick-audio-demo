# based on examples at https://smarketshq.com/how-to-use-docker-py-307f4029cf
import os
import sys
#from docker import Client
import docker

def cleanup(image_instance):
    client = docker.from_env()
    try:
        container = client.containers.get(image_instance)
        print("Found container")
    except docker.errors.NotFound:
        print("Didn't find the container - OK")
    except docker.errors.APIError as e:
        print("APIError - Server returned an error")
        raise(e)
    else:
        container.stop() # using autoremove option so this should be enough to reuse the name
        print("Called stop.")


def deploy(image_instance):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_name = 'webserver-image'
    
    ## do it using from_env() - v3 stop before writing container
    cleanup(image_instance)
    
    client = docker.from_env()
    try:
        client.images.build(path=dir_path, tag=image_name)
    except docker.errors.BuildError: 
        print("Build error")
        raise
        
    container = client.containers.run(
        image_name,
        ports={80:80},
        name=image_instance,
        detach=True,
        auto_remove=True,
        volumes={os.path.join(dir_path,'html'): {'bind': '/usr/share/nginx/html', 'mode': 'ro'}},
    )
    
if __name__ == "__main__":
    import sys
    image_instance = 'audio-demo'
    cleanup(image_instance)
    deploy(image_instance)