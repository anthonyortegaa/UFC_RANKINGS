from fastapi import FastAPI
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to UFC Rankings (Backend)"}

# Rankings endpoint
@app.get("/rankings/")
def get_rankings():
    # Temporary mock data
    return {
        "divisions": [
            {
                "division": "Lightweight",
                "fighters": [
                    {"rank": 1, "name": "Islam Makhachev"},
                    {"rank": 2, "name": "Charles Oliveira"},
                ]
            }
        ]
    }