from cg_pro import app

app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
