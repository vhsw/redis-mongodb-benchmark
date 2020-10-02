# Redis vs MongoDB

## Installation

```shell
poetry install
```

## Usage

```shell
pytest --benchmark-histogram --benchmark-sort=fullname
```

## Results

On localhost:
![local host](results/local.svg)

On remote:
![remote host](results/remote.svg)
