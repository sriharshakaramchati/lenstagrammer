from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
	<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <title>Claim Lens Handle</title>
        <style>
            body {
		font-family: 'Inter', sans-serif;
                background-color: #272E29; /* Pastel green background */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                display: flex;
                width: 80%;
        	height: 80%; /* Adjusted height */
	        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
            .text-side {
                flex: 1;
                background-color: #FFEBB8; /* Pastel yellow */
                padding: 20px;
                text-align: center;
                border-top-left-radius: 20px;
                border-bottom-left-radius: 20px;
            }
            .qr-side {
                flex: 1;
		justify-content: center;
  		align-items: center;
                padding: 20px;
                text-align: center;
                border-top-right-radius: 20px;
                border-bottom-right-radius: 20px;
            }
            img {
                border-radius: 15px; /* Curved corners for QR code */
            }
            button {
                background-color: #272E29; /* Pastel pink */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px; /* Curved corners for button */
            }
       	    h2 {
            font-weight: bold; /* Makes headline bold */
       	    }
            p, .text-side {
            font-weight: 300; /* Makes text thinner */
            }

        </style>
    </head>
    <body>
        <div class="container">
            <div class="text-side">
		<h2>Congratulations</h2>
                <p>You're now a Lenstagrammer!</p>
		<button>Harsha.lens</button>
            </div>
            <div class="qr-side">
                <img src="{{ url_for('static', filename='happy.png') }}" alt="QR Code" width="300">
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)

