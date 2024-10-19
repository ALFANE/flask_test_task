from flask import Blueprint, jsonify
from controllers.brand_controller import get_all_brands, get_brand_by_id
from controllers.manufacturer_controller import (
    get_all_manufacturers,
    get_manufacturer_by_id,
)

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/brands", methods=["GET"])
def brands_list():
    brands = get_all_brands()
    return jsonify([brand.name for brand in brands])


@api_blueprint.route("/brands/<int:brand_id>", methods=["GET"])
def brand_detail(brand_id):
    brand = get_brand_by_id(brand_id)
    return jsonify(
        {"id": brand.id, "name": brand.name, "description": brand.description}
    )


@api_blueprint.route("/manufacturers", methods=["GET"])
def manufacturers_list():
    manufacturers = get_all_manufacturers()
    return jsonify([manufacturer.name for manufacturer in manufacturers])


@api_blueprint.route("/manufacturers/<int:manufacturer_id>", methods=["GET"])
def manufacturer_detail(manufacturer_id):
    manufacturer = get_manufacturer_by_id(manufacturer_id)
    return jsonify(
        {
            "id": manufacturer.id,
            "name": manufacturer.name,
            "description": manufacturer.description,
            "country": manufacturer.country,
            "certificates": manufacturer.certificates,
        }
    )
