# ==============================================================================
# FILE: /users/mrensselaer/.lib/atbash.py
# DATE: 2105-09-12
# AUTHOR: M.v.R.
# ==============================================================================

def atbash(text):
    """
    Applies an elementary atbash cipher to the input text.
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Get the ASCII code
            code = ord(char)
            
            if char.isupper():
                # 'A' is 65, 'Z' is 90
                # Transformation: 155 - code
                result.append(chr(155 - code))
            else:
                # 'a' is 97, 'z' is 122
                # Transformation: 219 - code
                result.append(chr(219 - code))
        else:
            # Pass punctuation/numbers through untouched
            result.append(char)
            
    return "".join(result)


def main():
    print("ATBASH // VER 0.1a")
    print("INSTRUCTION: Paste the encrypted text (or text to encrypt).")
    print("INSTRUCTION: Type 'EXIT' to kill the process.\n")

    while True:
        try:
            user_input = input(">> INPUT: ")
            
            if user_input.strip().upper() == 'EXIT':
                break
            
            if not user_input:
                continue

            transformed = atbash(user_input)
            
            print(f"<< RESULT: {transformed}")
            print("-" * 40)
            
        except KeyboardInterrupt:
            print("[WARN] Manual interrupt detected. Aborting.")
            break
        
        except Exception as e:
            # Catch-all for whatever weird errors this archaic interpreter throws
            print(f"[ERROR] Logic fault: {e}")

if __name__ == "__main__":
    main()