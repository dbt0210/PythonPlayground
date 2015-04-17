import pickle


class DictFile(dict):

    def __init__(self, path):
        self.path = path

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
def test1(testdict: DictFile):
    testdict.read()
    testdict["testkey"] = "testvalue"
    testdict["testkeyint"] = 2
    print(testdict)
    # by the way, you can also eval("expressions").
    cmd = "mapfile.get(\"testkeyint\")"
    print(cmd + " = " + str(eval(cmd)))
    testdict.write()


def test2(testdict: DictFile):
    testdict["testkey1"] = "testvalue1"
    testdict["testkey2"] = "testvalue2"
    testdict.write_pickle()
    tmp = DictFile("ignore_config.p")
    tmp.read_pickle()
    print(tmp)


# running code
test1(DictFile("ignore_config.txt"))
test2(DictFile("ignore_config.p"))