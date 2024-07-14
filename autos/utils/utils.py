import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

class PriceModel():
    def __init__(self,
                 symboling,
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
                 fuel_system):
        
        self.symboling         = symboling
        self.normalized_losses = normalized_losses
        self.wheel_base        = wheel_base
        self.length            = length
        self.width             = width
        self.height            = height
        self.curb_weight       = curb_weight
        self.num_of_cylinders  = num_of_cylinders
        self.engine_size       = engine_size
        self.bore              = bore
        self.stroke            = stroke
        self.compression_ratio = compression_ratio
        self.horsepower        = horsepower
        self.peak_rpm          = peak_rpm
        self.city_mpg          = city_mpg
        self.highway_mpg       = highway_mpg
        self.fuel_type         = fuel_type
        self.aspiration        = aspiration
        self.num_of_doors      = num_of_doors
        self.drive_wheels      = drive_wheels
        self.engine_location   = engine_location
        self.make              = make
        self.body_style        = body_style
        self.engine_type       = engine_type
        self.fuel_system       = fuel_system

    def LoadUtils(self):
        with open(r'utils/cat_encoder.pkl','rb') as f1:
            cat_encoder = pickle.load(f1)
        with open(r'utils/ord_encoder.pkl','rb') as f2:
            ord_encoder = pickle.load(f2)
        with open(r'utils/scaler.pkl','rb') as f3:
            scaler = pickle.load(f3)
        with open(r'utils/model_auto_knn.pkl','rb') as f4:
            model = pickle.load(f4)
        return cat_encoder, ord_encoder, scaler, model

    def PrintValues(self):
        value_list = [
        self.symboling,         
        self.normalized_losses, 
        self.wheel_base,        
        self.length,            
        self.width,             
        self.height,            
        self.curb_weight,       
        self.num_of_cylinders,  
        self.engine_size,       
        self.bore,              
        self.stroke,            
        self.compression_ratio, 
        self.horsepower,        
        self.peak_rpm,          
        self.city_mpg,          
        self.highway_mpg,       
        self.fuel_type,         
        self.aspiration,        
        self.num_of_doors,      
        self.drive_wheels,      
        self.engine_location,   
        self.make,              
        self.body_style,        
        self.engine_type,       
        self.fuel_system,       
        ]
        return value_list

    def PredictPrice(self):
        cat_encoder, ord_encoder, scaler, model = self.LoadUtils()
    
        num_feat = pd.DataFrame(np.array([[eval(self.symboling),
                             eval(self.normalized_losses),
                             eval(self.wheel_base),
                             eval(self.length),
                             eval(self.width), 
                             eval(self.height), 
                             eval(self.curb_weight), 
                             eval(self.num_of_cylinders), 
                             eval(self.engine_size), 
                             eval(self.bore), 
                             eval(self.stroke), 
                             eval(self.compression_ratio), 
                             eval(self.horsepower), 
                             eval(self.peak_rpm), 
                             eval(self.city_mpg),
                             eval(self.highway_mpg)]]),

                             columns=
                             ['symboling', 
                             'normalized-losses', 
                             'wheel-base', 
                             'length', 
                             'width', 
                             'height', 
                             'curb-weight', 
                             'num-of-cylinders', 
                             'engine-size', 
                             'bore', 
                             'stroke', 
                             'compression-ratio', 
                             'horsepower', 
                             'peak-rpm',
                             'city-mpg',
                            'highway-mpg'])
        
        ord_feat = pd.DataFrame([[self.fuel_type,
                             self.aspiration,
                             self.num_of_doors,
                             self.drive_wheels,
                             self.engine_location]],
                             columns=['fuel-type',
                                      'aspiration',
                                      'num-of-doors',
                                      'drive-wheels',
                                      'engine-location']
)
        cat_feat = pd.DataFrame([[self.make,
                                 self.body_style,
                                 self.engine_type,
                                 self.fuel_system]],
                                columns=['make',
                                         'body-style',
                                         'engine-type',
                                         'fuel-system'])
        
        new_cat_features = list(cat_encoder.get_feature_names_out())
        X_cat = pd.DataFrame(cat_encoder.transform(cat_feat).toarray(), columns =  new_cat_features)

        ord_features = list(ord_encoder.get_feature_names_out())
        X_ord = pd.DataFrame(ord_encoder.transform(ord_feat), columns = ord_features)

        num_features = scaler.get_feature_names_out()
        X_num  = pd.DataFrame(scaler.transform(num_feat), columns = num_features)

        X = pd.concat([X_num, X_ord, X_cat], axis=1)

        prediction = int(model.predict(X))
        return prediction

class Values():
    def make(self):
        cars = ['alfa-romero',
            'audi',
            'bmw',
            'chevrolet',
            'dodge',
            'honda',
            'isuzu',
            'jaguar',
            'mazda',
            'mercedes-benz',
            'mercury',
            'mitsubishi',
            'nissan',
            'peugot',
            'plymouth',
            'porsche',
            'renault',
            'saab',
            'subaru',
            'toyota',
            'volkswagen',
            'volvo']
        return cars



    def body(self):
        style = ['convertible',
             'hatchback',
             'sedan',
             'wagon',
             'hardtop']
        return style



    def engine(self):
        eng = ['dohc',
           'ohcv',
           'ohc',
           'l',
           'rotor',
           'ohcf',
           'dohcv']
        return eng



    def aspiration(self):
        asp = ['std',
            'turbo']
        return asp

    def fuel_system(self):
        fuels = ['mpfi',
             '2bbl',
             'mfi',
             '1bbl',
             'spfi',
             '4bbl',
             'idi',
             'spdi']
        return fuels

    def num_cylinders(self):
        cylinders = [2,3,4,5,6,8,12]
        return cylinders


    def num_doors(self):
        doors = ['four', 'two']
        return doors

    def drive_wheels(self):
        drive = ['fwd',
             'rwd',
             '4wd']
        return drive

    def engine_location(self):
        location = ['front', 'rear']
        return location

    def fuel_type(self):
        fuels = ['gas', 'diesel']
        return fuels

    def symboling(self):
        sym = [-3, -2, -1, 0, 1, 2, 3]
        return sym


if __name__ == '__main__':
   import pandas as pd
   df = pd.read_csv('autos_dataset.csv')
   print(df.columns)
   print(df['horsepower'].unique())
#   print(df['engine-size'].unique())