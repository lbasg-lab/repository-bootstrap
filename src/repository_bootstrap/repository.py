import json
import os
from pathlib import Path

import requests


REPOSITORY_CONFIG_PATH = Path(
    ".github/configuration/repository.json"
)


def load_repository_configuration():
    with open(
        REPOSITORY_CONFIG_PATH,
        encoding="utf-8",
    ) as repository_file:
        return json.load(repository_file)


def get_headers(token):
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def get_repository(owner, repository, token):
    url = f"https://api.github.com/repos/{owner}/{repository}"

    response = requests.get(
        url,
        headers=get_headers(token),
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def repository_needs_update(
    configured_repository,
    current_repository,
):
    for key, value in configured_repository.items():
        if current_repository.get(key) != value:
            return True

    return False


def update_repository(
    owner,
    repository,
    token,
    configuration,
):
    url = f"https://api.github.com/repos/{owner}/{repository}"

    response = requests.patch(
        url,
        headers=get_headers(token),
        json=configuration,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def apply_repository(owner, repository):
    token = os.getenv("GITHUB_TOKEN")

    if token is None:
        raise ValueError(
            "GITHUB_TOKEN environment variable not found."
        )

    configuration = load_repository_configuration()

    current_repository = get_repository(
        owner,
        repository,
        token,
    )

    print(
        f"Repository found: "
        f"{current_repository['full_name']}"
    )

    if repository_needs_update(
        configuration,
        current_repository,
    ):
        print("Updating repository settings...")

        update_repository(
            owner,
            repository,
            token,
            configuration,
        )

        print("Repository settings updated.")

    else:
        print("Repository settings are up to date.")