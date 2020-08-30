import mongoengine

CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster0.vxluc.mongodb.net/core?retryWrites=true&w=majority"


def init():
    print("Init mongodb...")

    db = mongoengine.connect("core", alias="core", host=CONNECTION_STRING)

    # mongoengine.register_connection(alias='core', name='food_ordering_system')
    print("mongodb initialized")



