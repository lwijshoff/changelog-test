# changelog-test

This repository demonstrates automated changelog generation using [`git-chglog`](https://github.com/git-chglog/git-chglog) and GitHub Actions.

## 📄 Overview

The workflow is configured to automatically generate or update the `CHANGELOG.md` file whenever a [GitHub Release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) is published. It captures conventional commits, groups them by type (e.g., Features, Fixes), and formats them into a human-readable changelog.

## ⚙️ Setup Instructions

### ✅ Repository Settings

To ensure the GitHub workflow has the necessary permissions, make sure to enable **read and write** access for GitHub Actions under your repository settings:

![Repository Settings](assets/image.png)

You can find this setting under:

> **Settings → Actions → General → Workflow permissions → Read and write permissions**

### 🔖 Required Tags

For the workflow to properly label and handle pull requests, ensure these tags exist in your repository:

- `automated-pr`
- `documentation`

You can create them via the GitHub UI under **Issues → Labels**, or use the GitHub CLI:

```bash
gh label create automated-pr --color FFAB00 --description "Automatically generated pull requests"
gh label create documentation --color 0366D6 --description "Documentation-related changes"
```

## 🚀 Workflow Highlights

- Automatically generates `CHANGELOG.md` upon a release.
- Commits grouped by type (`feat`, `fix`, `refactor`, `perf`).
- Pull request automatically created and merged if changes are detected.
- Follows [Conventional Commits](https://www.conventionalcommits.org/) standard.

## 🧪 Example

To test this setup yourself:

1. Create some commits using the Conventional Commit format (e.g., `feat: add login button`).
2. Tag your release using the format `vX.Y.Z` (e.g., `v1.0.0`).
3. Publish the release via GitHub.
4. The GitHub Actions workflow will trigger, regenerate the changelog, and open a pull request with the update.

## 📘 Additional Resources

- [git-chglog Documentation](https://github.com/git-chglog/git-chglog)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

_This project is intended for demonstration and experimentation purposes._