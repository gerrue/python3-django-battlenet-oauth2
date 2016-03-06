from battlenet.community import Community

class Profile(Community):

    ENDPOINT = '/sc2/profile/%d/1/%s/'

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.idsc = kwargs.get('idsc', None)
        self.name = kwargs.get('name', None)

    def get(self, idsc=None, name=None):
        if name:
            self.name = name
        else:
            if not self.name:
                raise ValueError('Name required.')
        if idsc:
            self.idsc = idsc
        else:
            if not self.idsc:
                raise ValueError('ID is required, us idsc to set this value')

        return self.make_request(self.ENDPOINT % (self.idsc, self.name))
