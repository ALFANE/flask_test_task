from models.model import Brand, Manufacturer
from extensions import db


def get_all_brands():
    return Brand.query.all()


def get_brand_by_id(brand_id):
    return Brand.query.get_or_404(brand_id)


def create_brand(data):
    data_dict = data.to_dict()
    data_dict.pop("csrf_token", None)
    data_dict.pop("submit", None)

    manufacturer_ids = data_dict.pop("manufacturers", [])
    if isinstance(manufacturer_ids, str):
        manufacturer_ids = [int(manufacturer_ids)]
    else:
        manufacturer_ids = list(map(int, manufacturer_ids))

    manufacturers = Manufacturer.query.filter(
        Manufacturer.id.in_(manufacturer_ids)
    ).all()

    new_brand = Brand(**data_dict)
    new_brand.manufacturers = manufacturers

    db.session.add(new_brand)
    db.session.commit()
    return new_brand
