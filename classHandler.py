import json

import psutil


class Memory(Resource):
    endpoint = "/memory"

    def get(self):
        return json.dumps({"Memory_Information": {}}, indent=4)

    def update(self):
        pass


class Disk(Resource):
    endpoint = "/disk"

    def get(self):
        # TODO: this will need to be built out with the ability to share information on individual drives
        return json.dumps({"Disk_Information": {}}, indent=4)

    def update(self):
        pass


class Compute(Resource):
    endpoint = "/compute"

    def get(self):
        # Is multi-CPU support really necessary? Probably not
        return json.dumps({"Compute_Inforomation": {}}, indent=4)

    def update(self):
        pass


class Video(Resource):
    endpoint = "/video"

    def get(self):
        """
         It will be interesting to see how I should split information
         depending on whether video is processed integrated or discreet
        """
        return json.dumps({"Video_Information": {}}, indent=4)

    def update(self):
        pass


class Network(Resource):
    endpoint = "/network"
    def get(self):
        # TODO: consider elements to serve, consider some elements may be compromising
        return json.dumps({"Network_Information": {}}, indent=4)

    def update(self):
        pass


# Other resources to consider?
classes = [Memory, Disk, Compute, Video, Network]
