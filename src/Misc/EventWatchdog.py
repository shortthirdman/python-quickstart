import time, logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def on_created(event):
    print(f"hey, {event.src_path} has been created!")

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
	path = "."
    go_recursively = True

    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
	event_handler.on_created = on_created
	event_handler.on_deleted = on_deleted
	event_handler.on_modified = on_modified
	event_handler.on_moved = on_moved

    observer = Observer()
    observer.schedule(event_handler, path, recursive=go_recursively)
	observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()