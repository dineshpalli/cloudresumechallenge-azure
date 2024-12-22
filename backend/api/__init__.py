import azure.functions as func
import function_app

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Register routes from function_app.py
app.register_functions(function_app)