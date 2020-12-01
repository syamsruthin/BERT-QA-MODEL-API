
#Loading all the endpoints written in endpoints dir
from q_a_api import app
from q_a_api.endpoints.ml_endpoints import predict

if __name__ == "__main__":
    app.run()
    print("Server started")
