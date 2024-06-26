from flask import Flask, render_template_string

app = Flask(__name__)

# Define the HTML content for the home page
home_page_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Home Page</h1>
    <p>This is a simple home page created using Flask.</p>
    <p>Adding something different</>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(home_page_html)

if __name__ == '__main__':
    app.run(debug=True)
