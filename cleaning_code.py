#keeping for future reference
ATMOS_DATA_2 = ATMOS_DATA.drop(["Geopotential \n height above MSL.1", "Static pressure.1", "Temperature Lapse Rate.1"], axis=1)
ATMOS_DATA_2 = ATMOS_DATA_2.drop(0)
ATMOS_DATA_2 = ATMOS_DATA_2.set_axis(["subscript", "geopotential_height_above_msl", "static_pressure", "standard_temperature", "temperature_lapse_rate"], axis=1)
ATMOS_DATA_2 = ATMOS_DATA_2.set_axis(ATMOS_DATA_2.subscript)
ATMOS_DATA_2 = ATMOS_DATA_2.drop("subscript", axis=1)
ATMOS_DATA_2.head()
ATMOS_DATA_2.to_csv("cleaned_atmos_data.csv")

from google.colab import files
files.download('cleaned_atmos_data.csv')
