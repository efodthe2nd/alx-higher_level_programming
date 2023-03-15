#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  return list.filter((item) => item === searchElement).length;
};
