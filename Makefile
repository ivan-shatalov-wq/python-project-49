install:
	uv sync

brain-games:
	uv run brain-games

make lint:
    uv run ruff check brain_games