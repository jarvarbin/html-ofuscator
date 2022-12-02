import re

def obfuscate_file(input_filename, output_filename):
  # Read the input HTML file
  with open(input_filename, "r") as input_file:
    html_string = input_file.read()

  # Use a regular expression to find all HTML tag names in the input string
  tag_names = re.findall(r"<\/?(\w+)", html_string)

  # Create a dictionary mapping each tag name to a randomly generated string
  tag_map = {}
  for tag_name in tag_names:
    tag_map[tag_name] = "".join(random.choices(string.ascii_letters, k=10))

  # Use the tag mapping to create the obfuscated HTML string
  output_html = ""
  for match in re.finditer(r"<\/?(\w+)", html_string):
    output_html += html_string[match.start():match.end()].replace(match.group(1), tag_map[match.group(1)])

  # Write the obfuscated HTML string to the output file
  with open(output_filename, "w") as output_file:
    output_file.write(output_html)
