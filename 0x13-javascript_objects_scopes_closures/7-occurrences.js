#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let counter = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { counter++; }
  }
  return counter;
};
