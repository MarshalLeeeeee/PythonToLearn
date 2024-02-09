class P(object):

    d = {}

    def get_instance_d(self):
        return self.d

    @classmethod
    def get_class_d(cls):
        return cls.d

    @staticmethod
    def get_static_d():
        return {}

p = P()
P.d = {'P':'P'}
p.d = {'p':'p'}
print(p.get_instance_d()) # {'p':'p'}, Instance method can see the members ownered by instance
print(p.get_class_d()) # {'P':'P'}, Class method can only see the members ownered by the type of instance
print(p.get_static_d()) # {}, Static method can see no members ownered by instance