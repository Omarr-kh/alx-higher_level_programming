#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const rep = parseInt(process.argv[2]);
  let i = 0;
  while (i < rep) {
    console.log('C is fun');
    i++;
  }
}
