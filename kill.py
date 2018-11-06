# based on examples at https://smarketshq.com/how-to-use-docker-py-307f4029cf
import sys
from deploy import cleanup

def kill(image_instance):
    cleanup(image_instance)
    
if __name__ == "__main__":
    import sys
    image_instance = 'audio-demo'
    kill(image_instance)
    