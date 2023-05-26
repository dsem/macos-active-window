from AppKit import NSWorkspace


def run():
    print(
        NSWorkspace.sharedWorkspace().activeApplication()["NSApplicationName"])


if __name__ == "__main__":
    run()
