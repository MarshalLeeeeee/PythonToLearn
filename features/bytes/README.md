# Bytes

In Python3, bytestring and string are treated differently and they are no longer interchangeable without encoding or decoding. 

## Mapping
Encoding: human syntax notation to binary representation

Decoding: binary representation to human syntax notation

 - ASCII: one byte -> 127 actions or characters
 - Latin-1 (ISO  8859-1): extend ASCII to 256
 - GBK2312: Chinese formal standard of encoding. Use two bytes to encode 6763 characters and 682 non-characters.
 - GBKxxxx: Further extension of GBK2312
 - Unicode: To give a standard for cross-language and cross-platform conversion. Include all characters in the world, where every character has its own encoding.

__A.py__

## Storage and transfer
Take Unicode as an example. every character can be aligned to a 4 bytes(UCS-4), To store / transfer character with padding zero can lead to sparse use.

UTF-8
 - 0000 0000-0000 007F | 0xxxxxxx
 - 0000 0080-0000 07FF | 110xxxxx 10xxxxxx
 - 0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
 - 0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

UTF-16 (similar)