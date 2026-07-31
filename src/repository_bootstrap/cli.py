import sys

from repository_bootstrap.rulesets import apply_rulesets


def main():
    if len(sys.argv) < 2:
        print("Usage: repository-bootstrap <command>")
        return

    command = sys.argv[1]

    if command == "apply-rulesets":
        if len(sys.argv) < 4:
            print(
                "Usage: repository-bootstrap "
                "apply-rulesets <owner> <repository>"
            )
            return

        owner = sys.argv[2]
        repository = sys.argv[3]

        apply_rulesets(owner, repository)

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()