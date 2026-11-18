# Bankino

A desktop banking application written in Python with a Tkinter GUI, built by a six-person Scrum team in the course **DIT099 Agile Development** at the University of Gothenburg (Nov 2025 – Jan 2026).

The main goal of the project was to learn to work as an Agile team: sprint planning, a Jira backlog, a shared Definition of Done, and a Git workflow with one branch and ticket per task. It's a learning project, not a real banking system.

## Features

- **Sign up and log in** with a personal number and password. Passwords must meet strength rules and are stored as SHA-256 hashes.
- **Multiple bank accounts per user:** create, lock/unlock and delete accounts.
- **Deposits and transfers** between accounts, with validation that the receiving account exists.
- **Transaction history** for each account.
- **Virtual cards:** generate a card linked to an account, with a unique card number and security code, and view it as a card image.
- **Savings goals** that can be set and removed per account.

## Tech stack

- **Python 3** using only the standard library (`tkinter`, `json`, `hashlib`, `re`, …), so there's nothing to install.
- **JSON files** in `data/` serve as a simple database for users, accounts and cards (schema in [`docs/datastructure.md`](docs/datastructure.md)).

## Getting started

```bash
git clone https://github.com/HermanLarsson/bankino.git
cd bankino
python code/main.py
```

Requires Python 3 with Tkinter, which is included in the standard Python installers for Windows and macOS. On Linux you may need `sudo apt install python3-tk`.

Create a user through **Sign up**, then log in with your personal number and password.

Or log in as the demo user, who already has accounts, a card and transaction history:

| Personal number | Password |
|---|---|
| `209802100538` | `hello` |

## Project structure

```
code/
  main.py        # entry point, switches between logged-out and logged-in state
  pages/         # Tkinter windows (login, landing page, accounts, transfers, cards, savings, …)
  backend/       # logic: data access, account creation, transfers, card generation, password checks
  fonts/         # shared font definitions
data/            # JSON "database" and images
docs/            # data structure, style guide, Git conventions, Scrum documents
```

## How we worked

- **Scrum** with sprints, a product backlog and a Definition of Done ([`docs/`](docs/)).
- **Jira** for the backlog. Every branch and commit is named after its ticket, e.g. `SCRUM-89: …` ([conventions](docs/gitlab_conventions.md)).
- A shared **style guide** for the UI ([`docs/styleguide.md`](docs/styleguide.md)).
- The project was developed on the university's GitLab and is mirrored here.

## Team

Kim Duso Joviken · Farzam Forghanitorbaghan · Filip Andersson · Herman Larsson · Dominic Wooldridge · Isac Bibit Mattsson

### My contributions (Herman Larsson)

- **Account creation:** the "Create new bank account" window and the logic behind it.
- **Virtual cards:** card number and security code generation, the card data structure in JSON, and the window that displays the card.
- **Transfers:** validation that the receiving account exists.
- **Refactoring** in the final sprint: the landing page, the bank account window, the card window, card generation and account creation.
