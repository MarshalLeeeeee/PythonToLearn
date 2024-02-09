# Bool:
When the object is directly used in a condition judgement. It will

 - Return ```__bool__``` if implemented. (In python3)
 - Return ```bool(__len__)``` when ```__bool__``` is not explicitly implemented. 
 - Return True when both ```__len__``` and ```__bool__``` are not explicitly implemented. 
