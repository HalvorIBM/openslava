# Example GitHub Feature Request for the Finance Dashboard Lab

## Example Pull Request / Issue Request

**Title:** Add a graph for a user-selected company

### Business Request
The existing finance dashboard compares IBM with a fixed set of competitors.  
We now want users to indicate a company symbol and see an additional graph for that company without removing the existing dashboard views.

### Expected Behavior
- the user can enter or select a ticker symbol
- the application validates the symbol input
- the application loads data for the selected company
- a new graph appears for the selected company
- the existing IBM and competitor dashboards remain visible

### Suggested Acceptance Criteria
- support at least one new user-provided valid ticker symbol
- show a loading state while retrieving data
- show an error state for invalid or unavailable symbols
- keep the original dashboards intact
- add tests or validation covering the new behavior

---

## Example Prompt to Bob

Fetch the GitHub issue or PR for the user-selected company graph feature. Analyze the request, identify the code areas that need to change, implement the feature, run validation, review the diff, and prepare the branch for push.

---

## Example GitHub Workflow Narrative

1. A contributor or product owner opens the request
2. Bob reviews the issue or PR context
3. Bob updates the finance dashboard implementation
4. Bob runs tests and build checks
5. Bob summarizes the change for the PR
6. A maintainer merges or closes the PR after review

---

## Why This Example Matters

This example demonstrates the key promise of the lab:
- Bob can respond to GitHub-driven change requests
- Bob can evolve an existing application, not just generate a new one
- Bob can help move work from request to validated branch update in a structured engineering flow