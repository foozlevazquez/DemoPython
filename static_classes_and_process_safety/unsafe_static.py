
import multiprocessing

class UnsafeStaticClass:
    """Please don't use me from more than one Process/Thread!"""

    bff_process = None

    @classmethod
    def use(cls):
        calling_process = multiprocessing.current_process()
        print("calling process = {}".format(calling_process))
        if cls.bff_process:
            if calling_process is not cls.bff_process:
                raise Exception("kaboom.")
        else:
            print("bff process = {}".format(calling_process))
            cls.bff_process = calling_process

        return True


class SubProcess(multiprocessing.Process):
    def run(self):
        UnsafeStaticClass.use()
        print("SubProcess Done")

def main():
    UnsafeStaticClass.use()
    sp = SubProcess()
    sp.start()
    sp.join()
    print("All Done")


if __name__ == '__main__':
    main()
