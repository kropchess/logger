# Logger Package

## Installation

```bash
pip install git+https://github.com/kropchess/logger.git
```

## Usage

```python

from src import logger

logger.init(demo=True, colored=True)  # init module

logger.init(colored=True)  # init module with colored output

logger.init(demo=True)  # demo output

logger.init(demo=True, colored=True)  # demo with colored

logger.log.info('Foo', 'Bar')  # [INFO][Bar] Foo
logger.log.warning('Foo', 'Bar')  # [WARNING][Bar] Foo
logger.log.error('Foo', 'Bar')  # [ERROR][Bar] Foo
```

## Links
> [Github](https://github.com/kropchess/logger/)
