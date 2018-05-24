# takes 379 seconds
print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)
print work_dir

if not os.path.isdir("../orig/"): # Create the output directory if it doesn't exist
    os.makedirs("../orig/")

if not os.path.isdir("../temp/"): # Create the temporary file directory if it doesn't exist
    os.makedirs("../temp/")

if not os.path.isdir("../docs/"): # Create the temporary file directory if it doesn't exist
    os.makedirs("../docs/")

### Define the main function ###
def main():
    try:
        # Setting input and output
        url = "https://c402277.ssl.cf1.rackcdn.com/publications/16/files/original/GLWD-level1.zip?1343838522"
            # Linked from https://www.worldwildlife.org/publications/global-lakes-and-wetlands-database-large-lake-polygons-level-1
        downloaded_zip = "../temp/" + "lakes.zip"
        # Process
        # download_data(url, downloaded_zip)

        print "Extract all files" # Extracting only necessary files (the .extract() function) does not work. So we extract all and then delete those unnecessary.
        # Setting input and output
        input_zip = downloaded_zip
        outdir = "../temp/"
        # uncompress_zip(input_zip, outdir)

        print "Moving unzipped files to relevant folders"
        for file in os.listdir("../temp/"):
            if file[-3:] == "pdf":
                os.rename("../temp/" + file, "../docs/" + file)
            else:
                os.rename("../temp/" + file, "../orig/" + file)

        print "Deleting the temporary file directory"
        for file in os.listdir("../temp"):
            print file
            os.remove("../temp/"+file)
        os.rmdir("../temp/")

        print "All done."

    # Return any other type of error
    except:
        print "There is an error."

### Define the subfunctions ###
def download_data(url, output):
    print "...downloading and saving the file"
    import wget
    wget.download(url, output)

def uncompress_zip(in_zip, outdir):
    print "...launching zipfile module" # See http://stackoverflow.com/questions/9431918/extracting-zip-file-contents-to-specific-directory-in-python-2-7
    import zipfile
    print "...reading the zip file"
    zip_ref = zipfile.ZipFile(in_zip, 'r')
    print "...extracting the zip file"
    zip_ref.extractall(outdir)
    print "...closing the zip file"
    zip_ref.close()
    print "...deleting the zip file"
    os.remove(in_zip)

### Execute the main function ###
if __name__ == "__main__":
    main()
