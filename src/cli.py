import argparse
from src.session_logger import SessionLogger

logger = SessionLogger()


def main():
    parser = argparse.ArgumentParser(prog="devtrack")
    subparsers = parser.add_subparsers(dest="command")

    # START
    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("--project", required=True)
    start_parser.add_argument("--desc", default="")
    start_parser.add_argument("--tags", nargs="*", default=[])

    # STOP
    subparsers.add_parser("stop")

    # STATUS
    subparsers.add_parser("status")

    args = parser.parse_args()

    if args.command == "start":
        logger.start_session(
            project_name=args.project,
            description=args.desc,
            tags=args.tags
        )

    elif args.command == "stop":
        logger.end_session()

    elif args.command == "status":
        session = logger.get_active_session()

        if not session:
            print("No active session.")
        else:
            print("Active session:")
            print(f"Project: {session['project']}")
            print(f"Started: {session['start_time']}")
            print(f"Running for: {session['running_minutes']} minutes")
            print(f"Description: {session['description']}")
            print(f"Tags: {', '.join(session['tags'])}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()