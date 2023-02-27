from manage import db, app


class URLData(db.Model):
    # simple model.. very simple (without repr)
    # but as basic template (for test) is okay

    id = db.Column(db.Integer, primary_key=True)
    request_url = db.Column(db.String)
    status_code = db.Column(db.Integer)
    final_url = db.Column(db.String)
    final_status_code = db.Column(db.Integer)
    title = db.Column(db.String)
    domain_name = db.Column(db.String)


def save_db(request_url, status_code, final_url,
            final_status_code, domain_name, title):
    # method for save parse data from url in database

    instance = URLData(request_url=request_url,
                       status_code=status_code,
                       final_url=final_url,
                       final_status_code=final_status_code,
                       domain_name=domain_name,
                       title=title)
    db.session.add(instance)
    db.session.commit()
    app.logger.info("Create new row")
    return True
