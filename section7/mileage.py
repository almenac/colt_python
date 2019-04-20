print("How many kms did you cycle today?")
kms = input()
miles = float(kms)/1.60934

#f-string kääntää itse stringiksi. Pyöristää voi format specifierilla tai round()-funktiolla.
print(f"Ok, that's {miles:.2f} miles!")

#tai kankeammin concatenationilla
# miles_str = str(miles)
# print("Ok, that's " + miles_str + " miles!")
