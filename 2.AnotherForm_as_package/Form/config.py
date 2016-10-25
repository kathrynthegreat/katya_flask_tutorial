import os
import logging

logging.basicConfig(level=logging.INFO)

DATABASE_URL = os.environ["DATABASE_URL"]
DB_URL = os.environ["DB_URL"]