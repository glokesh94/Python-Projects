import random

aplh = "abcdefghijklmnopqrstuvwxyz"
integer = "1234567890"
mix = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z"

def generator():
	while True:
		print("=>which password you want".upper())
		que = input("=>numerical(n),aplhabatical(a),mix(m)?->").lower().strip()
		if que == "n":
			while True:
				num = input("Enter the length->")
				if num.isdigit():
					for i in range(int(num)):
						print(random.choice(integer),end='')
					break
				else:
					print("Please enter an integer")			
			break

		elif que == "a":
			while True:
				apl = input("Enter the length->")
				if apl.isdigit():
					for i in range(int(apl)):
						print(random.choice(aplh),end='')
					break
				else:
					print("Please enter an integer")
			break
		elif que == "m":
			while True:
				mixx = input("Enter the length->")
				if mixx.isdigit():
					for i in range(int(mixx)):
						print(random.choice(mix),end='')
					break
				else:
					print("Please enter an integer")
			break
		
		else:
			print("Please enter a valid value!")		


generator()