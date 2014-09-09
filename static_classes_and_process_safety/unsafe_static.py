
import multiprocessing

class UnsafeStaticClass:
    """Please don't use me from more than one Process/Thread!"""

    bff_process = None

    @classmethod
    def use(cls):
        calling_process = multiprocessing.current_process()

        if bff_process:
            if calling_process is not cls.bff_process:
                raise Exception("kaboom.")
        else:
            cls.bff_process = calling_process

        return True
