from flask import Blueprint, render_template, request
from utils import utils
from utils.utils import PriceModel

main = Blueprint('main', __name__)

values = utils.Values()

MAKE = values.make()
BODY = values.body()
ENGINE = values.engine()
FUELSYS = values.fuel_system()
ASPIRATION = values.aspiration()
CYLINDERS = values.num_cylinders()
DOORS = values.num_doors()
DRIVE = values.drive_wheels()
LOCATION = values.engine_location()
FUELS = values.fuel_type()
SYMBOLING = values.symboling()

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        symboling         = request.form["symboling"]
        normalized_losses = request.form["normalized_losses"]
        wheel_base        = request.form["wheel_base"]
        length            = request.form["length"]
        width             = request.form["width"]
        height            = request.form["height"]
        curb_weight       = request.form["curb_weight"]
        num_of_cylinders  = request.form["num_of_cylinders"]
        engine_size       = request.form["engine_size"]
        bore              = request.form["bore"]
        stroke            = request.form["stroke"]
        compression_ratio = request.form["compression_ratio"]
        horsepower        = request.form["horsepower"]
        peak_rpm          = request.form["peak_rpm"]
        city_mpg          = request.form["city_mpg"]
        highway_mpg       = request.form["highway_mpg"]
        fuel_type         = request.form["fuel_type"]
        aspiration        = request.form["aspiration"]
        num_of_doors      = request.form["num_of_doors"]
        drive_wheels      = request.form["drive_wheels"]
        engine_location   = request.form["engine_location"]
        make              = request.form["make"]
        body_style        = request.form["body_style"]
        engine_type       = request.form["engine_type"]
        fuel_system       = request.form["fuel_system"]
        model = PriceModel(symboling,
                            normalized_losses,
                            wheel_base,
                            length,
                            width,
                            height,
                            curb_weight,
                            num_of_cylinders,
                            engine_size,
                            bore,
                            stroke,
                            compression_ratio,
                            horsepower,
                            peak_rpm,
                            city_mpg,
                            highway_mpg,
                            fuel_type,
                            aspiration,
                            num_of_doors,
                            drive_wheels,
                            engine_location,
                            make,
                            body_style,
                            engine_type,
                            fuel_system)
        result = model.PredictPrice()
        printable = model.PrintValues()
        print(printable)
        output = f"${result}"
        return render_template('predict.html',
                           make=MAKE,
                           body=BODY,
                           engine=ENGINE,
                           fuelsys = FUELSYS,
                           aspiration=ASPIRATION,
                           cylinders = CYLINDERS,
                           doors = DOORS,
                           drive = DRIVE,
                           location = LOCATION,
                           fuels = FUELS,
                           symboling=SYMBOLING,
                           output=output)
        
    return render_template('predict.html',
                           make=MAKE,
                           body=BODY,
                           engine=ENGINE,
                           fuelsys = FUELSYS,
                           aspiration=ASPIRATION,
                           cylinders = CYLINDERS,
                           doors = DOORS,
                           drive = DRIVE,
                           location = LOCATION,
                           fuels = FUELS,
                           symboling=SYMBOLING)