from models.model import Manufacturer, Brand
from extensions import db


def get_all_manufacturers():
    return Manufacturer.query.all()


def get_manufacturer_by_id(manufacturer_id):
    return Manufacturer.query.get_or_404(manufacturer_id)


def create_manufacturer(data):

    data_dict = data.to_dict()

    data_dict.pop("csrf_token", None)
    data_dict.pop("submit", None)
    brand_ids = data_dict.pop("brands", [])
    if isinstance(brand_ids, str):
        brand_ids = [int(brand_ids)]
    else:
        brand_ids = list(map(int, brand_ids))

    brands = Brand.query.filter(Brand.id.in_(brand_ids)).all()

    new_manufacturer = Manufacturer(**data_dict)
    new_manufacturer.brands = brands

    db.session.add(new_manufacturer)
    db.session.commit()
    return new_manufacturer
