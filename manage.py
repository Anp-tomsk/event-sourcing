from entry_point import run_app

if __name__ == "__main__":
    try:
        run_app(8088)
    except RuntimeError:
        print("Runtime exception")

