const lineReader = require('line-reader');
const part1 = require('./part1').fuelRequirements;
const part2 = require('./part1').fuelForFuel;

const inputFile = process.argv[2];
const readInput = () => {
  let totalPart1 = 0;
  let totalPart2 = 0;
  lineReader.eachLine(inputFile, (line, last) => {
    totalPart1 += part1(line);
    totalPart2 += part2(line);
    if (last) {
      console.log(totalPart1);
      console.log(totalPart2);
    }
  });
};

readInput();
