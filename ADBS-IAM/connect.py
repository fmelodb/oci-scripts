import oracledb.plugins.oci_tokens
from dotenv import load_dotenv
import os

load_dotenv()

token_based_auth = {                             
    "auth_type": "ConfigFileAuthentication",    
    "profile": "DEFAULT",                       
    "file_location": "[ocicli config path]",             
}

connection = oracledb.connect(
    dsn="[ADB service name]",
    config_dir="[unziped wallet.zip path]",
    wallet_location="[unziped wallet.zip path]",
    wallet_password="password",
    extra_auth_params=token_based_auth)

cursor = connection.cursor()
cursor.execute("SELECT SYS_CONTEXT('USERENV', 'AUTHENTICATED_IDENTITY'), SYS_CONTEXT('USERENV', 'SESSION_USER')")

for row in cursor:
    print(row)
    
cursor.close()
connection.close()

