import thread

def mt(func):
    thread.start_new_thread(func,())
