import copy
import json
import os
from pathlib import Path

import requests

RULESETS_PATH = Path(".github/configuration/rulesets")


def load_rulesets():
    rulesets = []

    for file in RULESETS_PATH.glob("*.json"):
        with open(file, encoding="utf-8") as ruleset_file:
            rulesets.append(json.load(ruleset_file))

    return rulesets


def get_headers(token):
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def normalize_ruleset(ruleset):
    normalized = copy.deepcopy(ruleset)

    fields_to_remove = [
        "id",
        "node_id",
        "source",
        "source_type",
        "created_at",
        "updated_at",
        "current_user_can_bypass",
        "_links",
    ]

    for field in fields_to_remove:
        normalized.pop(field, None)

    return normalized


def ruleset_needs_update(configured_ruleset, repository_ruleset):
    configured = normalize_ruleset(configured_ruleset)
    repository = normalize_ruleset(repository_ruleset)

    return configured != repository


def get_repository(owner, repository, token):
    url = f"https://api.github.com/repos/{owner}/{repository}"

    response = requests.get(
        url,
        headers=get_headers(token),
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def get_rulesets(owner, repository, token):
    url = f"https://api.github.com/repos/{owner}/{repository}/rulesets"

    response = requests.get(
        url,
        headers=get_headers(token),
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def get_ruleset(owner, repository, ruleset_id, token):
    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repository}/rulesets/{ruleset_id}"
    )

    response = requests.get(
        url,
        headers=get_headers(token),
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def create_ruleset(owner, repository, token, ruleset):
    url = f"https://api.github.com/repos/{owner}/{repository}/rulesets"

    response = requests.post(
        url,
        headers=get_headers(token),
        json=ruleset,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def update_ruleset(owner, repository, token, ruleset_id, ruleset):
    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repository}/rulesets/{ruleset_id}"
    )

    response = requests.put(
        url,
        headers=get_headers(token),
        json=ruleset,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def get_matching_ruleset(configured_ruleset, repository_rulesets):
    for repository_ruleset in repository_rulesets:
        if repository_ruleset["name"] == configured_ruleset["name"]:
            return repository_ruleset

    return None


def apply_rulesets(owner, repository):
    token = os.getenv("GITHUB_TOKEN")

    if token is None:
        raise ValueError(
            "GITHUB_TOKEN environment variable not found."
        )

    repository_data = get_repository(
        owner,
        repository,
        token,
    )

    print(f"Repository found: {repository_data['full_name']}")

    configured_rulesets = load_rulesets()

    repository_rulesets = get_rulesets(
        owner,
        repository,
        token,
    )

    for configured_ruleset in configured_rulesets:
        repository_ruleset = get_matching_ruleset(
            configured_ruleset,
            repository_rulesets,
        )

        if repository_ruleset is None:
            print(
                f"Creating ruleset "
                f"'{configured_ruleset['name']}'..."
            )

            create_ruleset(
                owner,
                repository,
                token,
                configured_ruleset,
            )

            print("Done.")

            continue

        repository_ruleset = get_ruleset(
            owner,
            repository,
            repository_ruleset["id"],
            token,
        )

        if ruleset_needs_update(
            configured_ruleset,
            repository_ruleset,
        ):
            print(
                f"Updating ruleset "
                f"'{configured_ruleset['name']}'..."
            )

            update_ruleset(
                owner,
                repository,
                token,
                repository_ruleset["id"],
                configured_ruleset,
            )

            print("Done.")

        else:
            print(
                f"Ruleset '{configured_ruleset['name']}' "
                "is up to date."
            )