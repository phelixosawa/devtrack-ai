import argparse
from src.session_logger import SessionLogger
from src.analytics import Analytics

logger = SessionLogger()


def main():
    parser = argparse.ArgumentParser(prog="devtrack")
    subparsers = parser.add_subparsers(dest="command")

    # start
    start_parser = subparsers.add_parser("start")
    start_parser.add_argument("--project", required=True)
    start_parser.add_argument("--desc", default="")
    start_parser.add_argument("--tags", nargs="*", default=[])

    # stop
    subparsers.add_parser("stop")

    # status
    subparsers.add_parser("status")

    # stats
    subparsers.add_parser("stats")

    args = parser.parse_args()

    try:
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

        elif args.command == "stats":
            analytics = Analytics()
            stats = analytics.today_stats()

            if not stats:
                print("No sessions recorded today.")
            else:
                print("Today's Stats:")
                print(f"Total time: {stats['total_minutes']} minutes")
                print(f"Sessions: {stats['session_count']}")
                print(f"Average session: {stats['average_minutes']} minutes")
                print(f"Longest session: {stats['longest_minutes']} minutes")

        else:
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()