#3 in Python 3.7 Documentation
#--------
# An Informal Introduction to Python

# 1.2. Strings

print('3.1.2. Strings\n')

print('	Strings can be printed with either:')
print("		'single quotes' \n		\"double quotes\"\n")
print(r'	Write a new line with \n'+'\n')
print(r'	Preface a string with r to use as raw string'+'\n')
print("""\
	Use triple quotes ('''...''') to write 
	a string that spans multiple lines
""")
print('	Adjacent string literals will'
	  ' be concatenated\n')

#7 in Python 3.7 Documentation
#--------
# Input and Output Formatting #

# 1. Fancy output formatting

print('\n7.1. Formatted string literals: prefae string with f or F\n')

year = 2018 ; event = 'Midterms'
print('	Results of the {year} {event}:')
print(f'	Results of the {year} {event}:\n')

