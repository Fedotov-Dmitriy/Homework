from .Haffman import encode_text, decode_text, encode_file, decode_file
import filecmp

def test_text_unicode_code():
    original = "Привет, мир! 😀"
    text, table = encode_text(original)
    decoded = decode_text(text, table)
    assert original == decoded

def test_long_text_code():
    original = ("abc абв 😀 " * 1000).strip()
    text, table = encode_text(original)
    decoded = decode_text(text, table)
    assert original == decoded

def test_small_file_code():
    content = b"small binary data\x00\x01"
    with open("small.bin", "wb") as f:
        f.write(content)
    encode_file("small.bin")
    decode_file("small_encoded", "small_res")
    assert filecmp.cmp("small.bin", "small_res")

def test_extension_preserved():
    content = b"some text data"
    with open("sample.txt", "wb") as f:
        f.write(content)
    encode_file("sample.txt")
    decoded_path = decode_file("sample_encoded")
    assert decoded_path.endswith(".txt")
    assert filecmp.cmp("sample.txt", decoded_path)
