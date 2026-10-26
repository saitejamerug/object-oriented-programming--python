# Access Modifiers
# Write a class Config with protected_settings dict and private_secret_key. Demonstrate: (a) public attribute
# access, (b) protected access with a warning comment, (c) private access via name mangling
# (and explain why you should NOT do this in real code), (d) a safe public method get_setting(key) as the
# correct approach.

class Config:
    def __init__(self):
        self.system_name = "sys"
        self._settings = {'mode':  'dark',
                          'RAM' : 4,
                          'ROM': 12}
        self.__secret_key = "PY21"
    def get_setting(self,key):
        return self._settings[key]
c1 = Config()
print(c1.system_name)
print(c1._settings)  #this is a protected property use getter..
print(c1._Config__secret_key)
print(c1.get_setting('mode'))

