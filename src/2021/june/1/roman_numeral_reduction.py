# Have the function RomanNumeralReduction(str) read str which will be a string of roman numerals in decreasing order. The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000.
# Your program should return the same number given by str using a smaller set of roman numerals. For example: if str is "LLLXXXVVVV" this is 200, so your program should return CC because this is the shortest way to write 200 using the roman numeral system given above. If a string is given in its shortest form, just return that same string.

def roman_numeral_reduction(str):
  roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
  i = 0
  num = 0
  while i < len(str):
    if i+1<len(str) and str[i:i+2] in roman:
        num+=roman[str[i:i+2]]
        i+=2
    else:
        num+=roman[str[i]]
        i+=1
  integer = int(num)
  val = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
  ]
  syb = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
  ]
  roman_num = ''
  i = 0
  while  num > 0:
    for _ in range(num // val[i]):
      roman_num += syb[i]
      num -= val[i]
    i += 1
  return roman_num





  

