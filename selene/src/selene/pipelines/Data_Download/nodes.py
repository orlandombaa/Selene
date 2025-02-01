"""
This is a boilerplate pipeline 'Data_Download'
generated using Kedro 0.19.10
"""

# Importación de librerrías
import os
import ee
import geemap
import pandas as pd
from datetime import datetime


# Create a specific date and time
start_date = datetime(year=2024, month=10, day=1)  # Year, Month, Day, con un digito las que son de 1

# end date
end_date = datetime(year=2025, month=1, day=8)

# Extración de fechas
start_year = start_date.year
start_month = start_date.month
start_day = start_date.day

end_year = end_date.year
end_month = end_date.month
end_day = end_date.day

# 1) Descarga de datos desde Sentinel
def Sentinel(a):
    print(a)


