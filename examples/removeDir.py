import swaglib
# removes the swaglib_dir directory
swaglib.removeDir("swaglib_dir")

# will throw out an error
swaglib.removeDir("swag")
