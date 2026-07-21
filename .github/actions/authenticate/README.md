# Authenticate

Authenticate as the Engineering Lab GitHub App and generate a GitHub App Installation Token.

## Purpose

This Composite Action provides a reusable authentication mechanism for GitHub Actions workflows within the Engineering Lab ecosystem.

It generates a GitHub App Installation Token that can be used to authenticate subsequent GitHub API calls without relying on Personal Access Tokens (PATs).

## Inputs

| Name           | Required | Description                                                                                                               |
| -------------- | :------: | ------------------------------------------------------------------------------------------------------------------------- |
| `app-id`       |    Yes   | GitHub App ID.                                                                                                            |
| `private-key`  |    Yes   | GitHub App private key in PEM format.                                                                                     |
| `owner`        |    Yes   | GitHub account or organization where the GitHub App is installed.                                                         |
| `repositories` |    No    | Comma-separated list of repositories to scope the installation token. If omitted, the default installation scope is used. |

## Outputs

| Name    | Description                    |
| ------- | ------------------------------ |
| `token` | GitHub App Installation Token. |

## Usage

```yaml
- name: Authenticate as GitHub App
  id: authenticate
  uses: ./.github/actions/authenticate
  with:
    app-id: ${{ secrets.ENGINEERING_LAB_APP_ID }}
    private-key: ${{ secrets.ENGINEERING_LAB_APP_PRIVATE_KEY }}
    owner: ${{ github.repository_owner }}

- name: Display authenticated user
  env:
    GH_TOKEN: ${{ steps.authenticate.outputs.token }}
  run: |
    gh api /user
```

## Requirements

* A registered GitHub App.
* The GitHub App must be installed for the target owner.
* The workflow must provide the GitHub App ID and private key.
* The GitHub App must have the required permissions for the operations performed after authentication.


