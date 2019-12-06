
const fuelRequirements = (mass) => Math.floor(mass / 3) - 2;

const solution = (input) => {
  console.log(input);
  return input.reduce((prev, curr) => prev + fuelRequirements(curr), 0);
};

const fuelForFuel = (mass, total = 0) => {
  const newMass = fuelRequirements(mass);
  if (newMass <= 0) {
    return total;
  }
  return fuelForFuel(newMass, total + newMass);
};

const solutionPart2 = (input) => {
  console.log(input);
  return input.reduce((prev, curr) => prev + fuelForFuel(curr), 0);
};

module.exports = {
  fuelRequirements, solution, fuelForFuel, solutionPart2,
};
