# -*- coding: utf-8 -*-


class ObjectCreator(object):
    pass

def echo(ob):
    print(ob)

mObject = ObjectCreator()
print(mObject)
print(ObjectCreator)
echo(ObjectCreator)
objectCreator = ObjectCreator
print(objectCreator)