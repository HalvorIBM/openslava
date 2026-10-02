# Bobathon Guide

A practitioner guide for IBM Client Engineers and Forward Deployed Engineers to plan, build, and deliver a successful Bobathon.

## Local Development

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000

## Build

```bash
mkdocs build
```

## Deploy (GitHub Pages)

Push to `main` — the GitHub Actions workflow in `.github/workflows/deploy.yml` builds and deploys automatically.

## Structure

```
docs/
├── index.md                    # Home page
├── pitch/                      # Pitch & Discovery
├── discovery/                  # Discovery & Scoping
├── planning/                   # Planning & Preparation
├── labs/                       # Use Cases & Labs
├── delivery/                   # Day-of Guide
├── followup/                   # Follow-Up & Pilot
└── resources.md                # Resource directory
```
