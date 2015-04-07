import pickle


class MapFile(dict):

    def __init__(self, path):
        self.path = path

    def put(self, key, value):
        self[key] = value

    def read(self):
        try:
            with open(self.path) as file:
                for line in file:
                    (key, value) = line.split("=")
                    self[key] = value
        except FileNotFoundError:
            print("File does not exist.")

    def write(self):
        try:
            with open(self.path, "w") as file:
                for (k) in self.keys():
                    print(str(k)+"="+str(self[k]), file=file)
        except:
            print("Something went wrong.")

    def read_pickle(self):
        try:
            with open(self.path, "rb") as file:
                self.clear()
                self.update(pickle.load(file))
        except FileNotFoundError:
            print("File does not exist.")

    def write_pickle(self):
        try:
            with open(self.path, "wb") as file:
                pickle.dump(self, file)
        except:
            print("Can't write to "+self.path+".")


# testing code
def test1(mapfile: MapFile):
    mapfile.read()
    mapfile.put("testkey", "testvalue")
    mapfile["testkeyint"] = 2
    print(mapfile)
    cmd = "mapfile.get(\"testkeyint\")"
    print(cmd + " = " + str(eval(cmd)))
    mapfile.write()


def test2(mapfile: MapFile):
    mapfile.put("testkey1", "testvalue1")
    mapfile.put("testkey2", "testvalue2")
    mapfile.write_pickle()
    tmp = MapFile("ignore_config.dat")
    tmp.read_pickle()
    print(tmp)


# running code
test1(MapFile("ignore_config.txt"))
test2(MapFile("ignore_config.dat"))