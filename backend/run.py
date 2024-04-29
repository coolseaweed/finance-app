import os
import uvicorn
from dotenv import load_dotenv
import argparse

load_dotenv()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--port",
        default=8080,
        type=int,
        help="uvicorn port",
    )

    parser.add_argument(
        "-w",
        "--workers",
        default=1,
        type=int,
        help="uvicorn worker",
    )

    parser.add_argument(
        "--root-path",
        default="",
        type=str,
        help="root path",
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        type=str,
        help="host",
    )

    parser.add_argument(
        "--reload",
        action="store_true",
        help="host",
    )

    return parser.parse_args()


if __name__ == "__main__":

    args = get_args()

    uvicorn.run(
        "source.app:wrapped_app",
        host=args.host,
        port=args.port,
        root_path=args.root_path,
        workers=args.workers,
        reload=args.reload,
    )
