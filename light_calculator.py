class light:
    speedoflight = 3e8
    planck = 6.626e-34
    def __init__(self, wavelength, frequency, energy):
        self.wavelength = wavelength
        self.frequency = frequency
        self.energy = energy
    def setWavelength(self, wavelength):
        self.wavelength = wavelength
    def setFrequency(self, frequency):
        self.frequency = frequency
    def setEnergy(self, energy):
        self.energy = energy
    def getWavelength(self):
        return self.wavelength
    def getFrequency(self):
        return self.frequency
    def getEnergy(self):
        return self.energy
    def solveWave(self):
        self.frequency = light.speedoflight/self.wavelength
        self.energy = self.frequency*light.planck
        return "The frequency is "+str(self.frequency)+" hertz.\nThe energy is "+str(self.energy)+" joules."
    def solveFreq(self):
        self.wavelength = light.speedoflight/self.frequency
        self.energy = self.frequency*light.planck
        return "The wavelength is "+str(self.wavelength)+" meters.\nThe energy is "+str(self.energy)+" joules."
    def solveEnergy(self):
        self.frequency = self.energy/light.planck
        self.wavelength = light.speedoflight/self.frequency
        return "The wavelength is "+str(self.wavelength)+" meters.\nThe frequency is "+str(self.frequency)+" hertz."

l1 = light(1, 1, 1)
print("0 = end, 1 = wavelength (meters), 2 = frequency (hertz), 3 = energy (joules)")
while True:
    inpt = int(input("What information do you have? "))
    if inpt == 0:
        break
    if inpt == 1:
        wavelength = float(input("What is the wavelength? "))
        l1.setWavelength(wavelength)
        print(l1.solveWave())
    if inpt == 2:
        frequency = float(input("What is the frequency? "))
        l1.setFrequency(frequency)
        print(l1.solveFreq())
    if inpt == 3:
        energy = float(input("What is the energy? "))
        l1.setEnergy(energy)
        print(l1.solveEnergy())