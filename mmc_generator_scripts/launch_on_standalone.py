import sys
import argparse
import pathlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch Maya in standalone mode.")
    parser.add_argument(
        "--script",
        type=str,
        help="Path to a Python script to execute after launching Maya.",
    )
    args = parser.parse_args()

    project_root = pathlib.Path(__file__).parent.parent
    to_remove = []
    for path in sys.path:
        if project_root.as_posix() in pathlib.Path(path).as_posix():
            to_remove.append(path)
    for path in to_remove:
        sys.path.remove(path)

    from maya import standalone
    standalone.initialize(name="python")
    print("Launching Maya in standalone mode...")

    if args.script:
        with open(args.script, "r") as f:
            exec(f.read())

    standalone.uninitialize()
