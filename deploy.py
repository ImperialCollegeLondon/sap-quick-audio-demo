# based on examples at https://smarketshq.com/how-to-use-docker-py-307f4029cf
import os
import sys
#from docker import Client
import docker

def deploy(demo_name):
    demo_name = 'audio-demo'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_name = 'webserver-image'
    
    ## do it using APIClient - v1 no checking, have to stop container using command line
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    client.build(path=dir_path, tag=image_name)
    ports = [80]
    port_bindings = {80: 9999}
    host_config = client.create_host_config(
        port_bindings=port_bindings,
    )
    container = client.create_container(
        image=image_name,
        ports=ports,
        host_config=host_config,
        name=demo_name,
    )
    client.start(container)
    
    
    #
    # # check the container isn't already running
    # #print(client.containers)
    #
    # #print('Containers: \n\n' + str(client.containers()))
    # containers = client.containers()
    # for container in containers:
    #         for container_name in container['Names']:
    #             # remove '/' prefix character
    #             container_name = container_name[1:]
    #             print(container_name)
    #             if container_name==demo_name:
    #                 container.stop(container)
    #                 container.remove(container)
    # #containers = client.containers
    # #for container in containers:
    # #  print(container.name)
    #
    # #client = docker.from_env()
    # #output = client.build(path=dir_path, tag=image_name)
    # client.build(path=dir_path, tag=image_name)
    #
    # ports = [80]
    # port_bindings = {80: 9999}
    # host_config = client.create_host_config(
    #     port_bindings=port_bindings,
    # )
    # container = client.create_container(
    #     image=image_name,
    #     ports=ports,
    #     host_config=host_config,
    #     name=demo_name,
    # )
    # client.start(container)
    
if __name__ == "__main__":
    import sys
    demo_name = 'audio-demo'
    # if len(sys.argv) > 0:
    #     demo_name = sys.argv[1]
    #     demo_name = ''.join(demo_name.split()) #endure there is no white space
    # print(demo_name)
    deploy(demo_name)