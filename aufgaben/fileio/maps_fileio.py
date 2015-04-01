#WIP
__author__ = 'dbt'
cfg = {}


def read(string):
    try:
        file = open(string)
        for line in file:
            (key, value) = line.split("=")
            cfg[key] = value
            print("File parsing done. Map: "+str(cfg))
    except FileNotFoundError:
        print("File does not exist. Creating one...")
        try:
            file = open(string, "w")
        except:
            print("Something went wrong.")
        finally:
            file.close()


def write(string):
    try:
        file = open(string, "w")
        for (k) in cfg.keys():
            print(str(k)+"="+str(cfg[k]), file=file)
        print("Writing done.")
    except:
        print("Something went wrong.")
    finally:
        file.close()


def get(key):
    return cfg.get(key)


def put(key, value):
    cfg[key] = value


#Test
filename="ignore_config.txt"

read(filename)
put("testkey", "testvalue")
put("testkeyint", 2)
print("get(\"testkeyint\") = " + str(get("testkeyint")))
print("Whole Dictionary: " + str(cfg))
write(filename)