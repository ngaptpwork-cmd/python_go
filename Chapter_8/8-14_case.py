def make_car(manufacturer, model, **car):
    car["manufacturer_name"] = manufacturer
    car["model_name"] = model
    return car


car = make_car("ferrari", "XL300C", year_of_manufacturer="2025", color="blue saphire")
print(car)
