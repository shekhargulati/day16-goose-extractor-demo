from flask import Flask, request, render_template,jsonify
from goose import Goose

app = Flask(__name__)
 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
 
@app.route('/api/v1/extract')
def extract():
	url = request.args.get('url')
	g = Goose()
	article = g.extract(url=url)
	response = {'title' : article.title , 'text' : article.cleaned_text[:250],'image': article.top_image.src}
	return jsonify(response)
 
if __name__ == "__main__":
    app.run(debug=True)



