#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const n = parseInt(process.argv[2]);
  let i = 0;
  while (i < n) {
    console.log('X'.repeat(n));
    i++;
  }
}
