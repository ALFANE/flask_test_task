from extensions import db

brand_manufacturer = db.Table(
    "brand_manufacturer",
    db.Column("brand_id", db.Integer, db.ForeignKey("brand.id")),
    db.Column("manufacturer_id", db.Integer, db.ForeignKey("manufacturer.id")),
)


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(64))
    certificates = db.Column(db.Text)
    brands = db.relationship(
        "Brand", secondary=brand_manufacturer, backref="manufacturer_brands"
    )


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(128))
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text)
    manufacturers = db.relationship(
        "Manufacturer", secondary=brand_manufacturer, backref="brand_manufacturers"
    )
