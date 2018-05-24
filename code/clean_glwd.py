# Takes *** seconds to run this script

print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)

if not os.path.isdir("../data/"): # Create the output directory if it doesn't exist
    os.makedirs("../data/")

print "Launching ArcGIS"
import arcpy

print "Enabling the Spatial Analyst extension"
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

print "Setting the environment"
arcpy.env.overwriteOutput = True # Allow the overwriting of the output files
arcpy.env.workspace = "../b_temp/b_temp.gdb" # Set the working directory. Some geoprocessing tools (e.g. Extract By Mask) cannot save the output unless the workspace is a geodatabase.

### Define the main function ###
def main():
  try:
    # Input
    input = "../orig/glwd_1.shp"
    projection = arcpy.SpatialReference(4326) # WGS 1984. See http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/pdf/geographic_coordinate_systems.pdf
    # Output
    output = "../data/glwd1.shp"
    # Process
    print "Copying the input file, to avoid the next tool from overwriting the original file"
    arcpy.CopyFeatures_management(input, output)
    print "Assigning the projection"
    arcpy.DefineProjection_management(output, projection)

    print "All done."

  # Return geoprocessing specific errors
  except arcpy.ExecuteError:
    print arcpy.GetMessages()
  # Return any other type of error
  except:
    print "There is non-geoprocessing error."
  # Check in extensions
  finally:
    arcpy.CheckInExtension("spatial")

# subfunctions



### Execute the main function ###
if __name__ == "__main__":
    main()
