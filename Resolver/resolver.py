import socket
class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if not (self.has_host(host)):
            self._cache[host] = socket.gethostbyname(host)
        print(host + " " +self._cache[host])

    def has_host(self,host):
        if host  in self._cache:
            return True
        return False

    def clear(self):
        self._cache.clear()