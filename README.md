# semantic-hallucinations-utils
Python package with basic utils

### Intallation using pip 
```bash
pip install git+https://github.com/semantic-hallucinations/semantic-hallucinations-utils.git
```

### Installation using requirements
```
organisation_utils @ git+https://github.com/semantic-hallucinations/semantic-hallucinations-utils.git
```

### Using logger
```python
from organisation_utils.logging_config import logger_factory

logger = logger_factory.get_logger("logger_name")
logger.info("logger initiated")
```
