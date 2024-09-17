import os
from dotenv import load_dotenv
import subprocess

# Load environment variables from .env file
load_dotenv("credentials.env")

# Get the environment variables
app_id = os.getenv("APPLICATIONID")
BACKEND_SECRET = os.getenv("BACKEND_SECRET")
blob_sas_token = os.getenv("BLOB_SAS_TOKEN")
azure_search_name = os.getenv("COG_SERVICES_NAME")
azure_openai_name = os.getenv("AZURE_OPENAI_NAME")
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
sql_server_name = os.getenv("SQL_SERVER_NAME")
sql_server_db = os.getenv("SQL_SERVER_DB")
sql_server_user = os.getenv("SQL_SERVER_USERNAME")
sql_server_password = os.getenv("SQL_SERVER_PASSWORD")
cosmosdb_name = os.getenv("COSMOSDB_NAME")
cosmosdb_container = os.getenv("COSMOSDB_CONTAINER")

# Azure Resource Group and Bicep file path
resource_group = os.getenv("RESOURCE_GROUP", "your-default-resource-group")
bicep_file = "deploy.bicep"  # Path to your Bicep file

# Construct the Azure CLI command to deploy the Bicep template
command = [
    "az", "deployment", "group", "create",
    "--resource-group", resource_group,
    "--template-file", bicep_file,
    "--parameters",
    f"appId={app_id}",
    f"appPassword={BACKEND_SECRET}",
    f"blobSASToken={blob_sas_token}",
    f"azureSearchName={azure_search_name}",
    f"azureOpenAIName={azure_openai_name}",
    f"azureOpenAIAPIKey={azure_openai_api_key}",
    f"SQLServerName={sql_server_name}",
    f"SQLServerDatabase={sql_server_db}",
    f"SQLServerUsername={sql_server_user}",
    f"SQLServerPassword={sql_server_password}",
    f"cosmosDBAccountName={cosmosdb_name}",
    f"cosmosDBContainerName={cosmosdb_container}"
]

# Execute the command
subprocess.run(command)



# Step 2: Deploy application code to the Web App
print("Deploying application code...")
command_deploy_code = [
    "az", "webapp", "deployment", "source", "config-zip",
    "--resource-group", resource_group,
    "--name", app_service_name,
    "--src", zip_file
]

subprocess.run(command_deploy_code)

print("Deployment complete.")