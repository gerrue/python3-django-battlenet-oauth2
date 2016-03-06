from battlenet.community import Community

class Profile(Community):

    ENDPOINT = '/sc2/profile/%d/1/%s/'

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)

    def get(self, id=None, name=None):
        if name:
            self.name = name
        else:
            if not self.name:
                raise ValueError('Name required.')
        if id:
            self.id = id
        else:
            if not self.id:
                raise ValueError('ID is required')

        return self.make_request(self.ENDPOINT % (self.id, self.name))
