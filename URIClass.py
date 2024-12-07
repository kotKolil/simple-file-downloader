class URIClass(object):
    """
    this class needs for parsing URI and saving data in class as an object
    """

    def __init__(self, raw_url):

        self.URI = raw_url

        if "://" not in raw_url:
            self.protocol = 'http'
            self.domain = raw_url.split("/")[0]
        else:
            self.protocol = raw_url.split('/')[0]
            self.domain = raw_url.split('/')[2]
        if "#" in raw_url:
            self.fragment = raw_url.split("#")[-1]
        else:
            self.fragment = ""
        self.path = ("/" + "/".join(raw_url.split("/")[3:-1]) + "/").replace("//", "/")
        self.query_param = {}
        for i in raw_url.split("#")[0].split("?"):
            if "=" in i:
                raw_parameter = i.split("=")
                param_name = raw_parameter[0]
                param_value = ''.join([char for char in raw_parameter[1] if char != "&"])
                self.query_param[param_name] = param_value
