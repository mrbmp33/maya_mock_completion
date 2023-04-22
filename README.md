# maya_mock_completion

This project is a custom modification over the command/api completion sent by Autodesk through _Maya's Developer Kit_ for Maya 2022.

Developing code for Maya can be a bit sluggish if you need to open the application for anything. This modification of the Python's command completion enables me to create mock objects for testing or just use dummy commands that do nothing for the sake of being able to run your code outside of a maya session.

This is useful for quick UI development or making DCC-agnostic code.

If you are using PyCharm as an IDE for developing code in Maya, you can add this to your interpreter's list of paths and just run maya commads and create API objects that do nothing but allow your code to still run. This in conjunction with patching can be a useful test enviornment to quickly try out new stuff.

# Disclaimer

I just use this for fun, I haven't test this in production so I am not entirely sure how useful it actually is.

Cheers!
