# html-ofuscator

This obfuscator takes an input HTML file, reads the contents of the file, and replaces the names of all HTML tags with randomly generated strings. The mapping from each input tag name to the corresponding obfuscated tag name is random and different each time the obfuscator is run. The obfuscated HTML is then written to the specified output file.

To use this obfuscator, you would call it like this:

obfuscate_file("input.html", "output.html")

This would read the contents of the file input.html, generate a randomly obfuscated version of the HTML, and write the obfuscated HTML to the file output.html. The exact output would be different each time the obfuscator is run, depending on the random choices made by the random.choices function.

