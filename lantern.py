import argparse
from tasks import add_task, list_tasks

# Create the main parser
parser = argparse.ArgumentParser(
    description="Lantern Task Tracker"
)

# Create subcommands
sub = parser.add_subparsers(dest="command")

# Add command
add_parser = sub.add_parser("add")
add_parser.add_argument("title")

# List command
list_parser = sub.add_parser("list")
# add argument sort
list_parser.add_argument("--sort", action="store_true", help="sort tasks by title")
list_parser.add_argument(
    "--done",
    action="store_true",
    help="Show only completed tasks"
)

if __name__ == "__main__":
    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Task added: {task['title']}")
    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            # check if the --sort is passed in args
            if args.sort:
                # sort the tasks by sorted algo
                tasks = sorted(tasks, key=lambda x: x.get("title", ""))
            for task in tasks:
                print(task)
