# The input for Star Schema is the pre-processed file "Processed_Chicago_Food_Inspections.csv"

#Importing libraries
import pandas as pd
import numpy as np

#Input File

preprocessed_file = 'Outputs/Processed_Chicago_Food_Inspections.csv'

# Reading the input preprocessed CSV file
chicago_input = pd.read_csv(preprocessed_file)

# Setting the path to store star schema tables

inspections_fact = 'inspections_fact.csv'
establishments_dimension = 'establishments_dimension.csv'
inspection_point_dimension = 'inspection_point_dimension.csv'
violations_dimension = 'violations_dimension.csv'

def star_schema():

    # Creating a Fact Table - 'inspections_fact.csv' with the existing 'inspection_id' as the primary key
    inspections_fact = chicago_input.loc[:,['inspection_id', 'License Number', 'Inspection Date', 'Inspection_Type', 'Results', 'Point_id']]
    inspections_fact.to_csv('inspections_fact.csv', index = False)

    # Creating a Dimension Table - 'establishments_dimension.csv' with the existing 'License Number' as the primary key
    establishments_dimension = chicago_input.loc[ :, ['License Number', 'inspection_id', 'DBA Name', 'AKA Name', 'Facility_Type', 'Risk', 'Address','City', 'State', 'Zip', 'Latitude', 'Longitude']]
    establishments_dimension.to_csv('establishments_dimension.csv', index = False)

    # Creating a Dimension Table - 'inspection_point_dimension.csv' with the existing 'Point_id' as the primary key
    inspection_point_dimension = chicago_input.loc[ : , ['Point_id', 'inspection_id', 'Category', 'Fine', 'Point_level']]
    inspection_point_dimension.to_csv('inspection_point_dimension.csv', index = False)

    # Creating a Dimension Table - 'violations_dimension.csv' with the existing 'inspection_id' as the foreign key
    violations_dimension = chicago_input.loc[ : , ['inspection_id', 'Point_id', 'Fine', 'Violations', 'Inspector_Comments']]
    violations_dimension.to_csv('violations_dimension.csv', index = False)

print("****Dimensions and Fact tables being created!****")



if __name__ == "__main__":
    star_schema()