const {
  fuelRequirements, solution, fuelForFuel, solutionPart2,
} = require('./part1.js');

it('is true', () => expect(true).toBe(true));

describe('part1', () => {
  it('is not null', () => {
    expect(fuelRequirements).not.toBe('null');
  });

  describe('fuel for mass', () => {
    const masses = [
      [12, 2],
      [14, 2],
      [1969, 654],
      [100756, 33583],
    ];

    masses.forEach(([mass, expected]) => {
      it(`can calculate mass for ${mass}`, () => {
        expect(fuelRequirements(mass)).toEqual(expected);
      });
    });

    it('can calculate multiple masses', () => {
      expect(solution([12, 14, 1969, 100756])).toEqual(34241);
    });
  });
});

describe('part2', () => {
  it('is not null', () => {
    expect(fuelRequirements).not.toBe('null');
  });

  describe('fuel for mass', () => {
    const masses = [
      [12, 2],
      [14, 2],
      [1969, 966],
      [100756, 50346],
    ];

    masses.forEach(([mass, expected]) => {
      it(`can calculate mass for ${mass}`, () => {
        expect(fuelForFuel(mass)).toEqual(expected);
      });
    });

    it('can calculate multiple masses', () => {
      expect(solutionPart2([12, 14, 1969, 100756])).toEqual(51316);
    });
  });
});
