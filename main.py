firstDigit = int(float(input("Enter the resistance point: ")) + 5.76) #not actually sure how to handle this, might get better results by properly rounding (same as adding 6.26 instead of 5.76)
print("The first digit is: " + str(firstDigit))
modulo = firstDigit%4
print("The modulo 4 is " + str(modulo))
lockPoint1 = int(input("Enter the first lock point: "))
lockPoint2 = int(input("Enter the second lock point: "))
potentialThirds = []
for i in range(4):
  potentialThirds.append((lockPoint1 + (i*10))%40)
  potentialThirds.append((lockPoint2 + (i*10))%40)
print("Potential third digits: " + str(potentialThirds))
potentialThirds = [x for x in potentialThirds if x%4 == modulo]
print("Potential third digits with the correct modulo: " + str(potentialThirds))
thirdDigit = int(input("Enter the correct Third Digit: "))
modulo = (modulo+2)%4
potentialSeconds = [x for x in range(40) if x%4 == modulo and abs(x-thirdDigit) > 4]
print("Potential second digits: " + str(potentialSeconds))
