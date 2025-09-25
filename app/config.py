import os
from dotenv import load_dotenv
from neomodel import config

load_dotenv()

NEO4J_BOLT_URL = os.getenv("NEO4J_BOLT_URL")
config.DATABASE_URL = NEO4J_BOLT_URL
