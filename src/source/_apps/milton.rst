import base64

def encode_script_to_base64(filepath):
  """Encodes a Python script to Base64.

  Args:
    filepath: Path to the Python script.

  Returns:
    The Base64-encoded string of the script.
  """
  with open(filepath, "rb") as script_file:
    script_content = script_file.read()
    encoded_bytes = base64.b64encode(script_content)
    encoded_string = encoded_bytes.decode("utf-8")  # Decode to a string
  return encoded_string

# Example usage:
encoded_script = encode_script_to_base64("my_script.py")
print(encoded_script)