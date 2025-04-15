import docker

client = docker.from_env()
containers = client.containers.list()
container = client.containers.get(containers[0])  # select first container
logs = container.logs()
container.stop()