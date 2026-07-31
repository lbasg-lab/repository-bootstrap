import sys

from repository_bootstrap.rulesets import apply_rulesets
from repository_bootstrap.repository import apply_repository


def main():
    if len(sys.argv) < 2:
        print("Usage: repository-bootstrap <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "apply-rulesets":
        if len(sys.argv) != 4:
            print(
                "Usage: repository-bootstrap "
                "apply-rulesets <owner> <repository>"
            )
            sys.exit(1)

        apply_rulesets(
            sys.argv[2],
            sys.argv[3],
        )

    elif command == "apply-repository":
        if len(sys.argv) != 4:
            print(
                "Usage: repository-bootstrap "
                "apply-repository <owner> <repository>"
            )
            sys.exit(1)

        apply_repository(
            sys.argv[2],
            sys.argv[3],
        )

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()