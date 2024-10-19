from flask import Blueprint, render_template, request, redirect, url_for
from controllers.brand_controller import create_brand, get_all_brands
from controllers.manufacturer_controller import (
    create_manufacturer,
    get_all_manufacturers,
)
from forms.brand_form import BrandForm
from forms.manufacturer_form import ManufacturerForm
from models.model import Brand, Manufacturer

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/brands", methods=["GET", "POST"])
def admin_brands():
    form = BrandForm()
    form.manufacturers.choices = [
        (manufacturer.id, manufacturer.name)
        for manufacturer in Manufacturer.query.all()
    ]
    if form.validate_on_submit():
        create_brand(request.form)
        return redirect(url_for("admin.admin_brands"))
    brands = get_all_brands()
    return render_template("brand_list.html", form=form, brands=brands)


@admin_blueprint.route("/manufacturers", methods=["GET", "POST"])
def admin_manufacturers():
    form = ManufacturerForm()
    form.brands.choices = [(brand.id, brand.name) for brand in Brand.query.all()]

    if form.validate_on_submit():
        create_manufacturer(request.form)
        return redirect(url_for("admin.admin_manufacturers"))
    manufacturers = get_all_manufacturers()
    return render_template(
        "manufacturer_list.html", form=form, manufacturers=manufacturers
    )
