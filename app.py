from appflask import app


@app.before_first_request
def create_tables():
    # db.reflect()
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vagrant:vagrant@192.168.1.19:5432/flaskapp'
    from appflask.db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=80)
