from ideas import db


class PMPapers(db.Model):
    __tablename__ = "pm_papers"
    pm_id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    dbname = db.Column(db.Text, unique=True)
    paper_title = db.Column(db.Text, unique=True)
    authors_list = db.Column(db.Text, unique=True)
    affiliations = db.Column(db.Text, unique=True)

    DOI_text = db.Column(db.Text, unique=True)
    Abstract = db.Column(db.Text, unique=True)
    url_content = db.Column(db.Text, unique=True)
    date_time = db.Column(db.DateTime, unique=True)

    def __init__(self, dic):
        self.pm_id = dic[0]
        self.dbname = dic[1]
        self.paper_title = dic[2]
        self.authors_list = dic[3]
        self.affiliations = dic[4]
        self.DOI_text = dic[5]
        self.Abstract = dic[6]
        self.url_content = dic[7]
        self.date_time = dic[8]

    def __repr__(self):
        return '<Paper %r>' % self.paper_title

