from deta import Deta
from dotenv import load_dotenv

load_dotenv()

# __init__
deta = Deta()

database = deta.Base('fast-api-auth')