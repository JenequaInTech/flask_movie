from app import create_app

print(create_app)  # Add this line to see if the import is successful

app = create_app()

@app.route('/')
def home():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)