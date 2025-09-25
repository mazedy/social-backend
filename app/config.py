import os
from dotenv import load_dotenv
from neomodel import config

load_dotenv()

NEO4J_BOLT_URL = os.getenv("NEO4J_BOLT_URL")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Correct Aura connection string
config.DATABASE_URL = f"{NEO4J_BOLT_URL}://{NEO4J_USER}:{NEO4J_PASSWORD}@e0791f27.databases.neo4j.io"
