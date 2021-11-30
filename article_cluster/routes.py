from flask import render_template, request, flash
from article_cluster import app

from .utils import predict


@app.route('/', methods=['POST', 'GET'])
def home():
    page_content = 'form'
    outcome = None
    keyword = ''
    if request.method == 'POST':
        keyword = request.form.get('keyword').strip().lower()

        if keyword == '' or keyword == ' ':
            page_content = 'form'
            flash("Empty keyword is not allowed", 'danger')
            return render_template('home.html', title='Article Predict', page_content=page_content)

        else:
            page_content = 'outcome'
            outcome = predict(keyword)
            
    
    return render_template('home.html', title='Article Predict', page_content=page_content, outcome=outcome, keyword=keyword)