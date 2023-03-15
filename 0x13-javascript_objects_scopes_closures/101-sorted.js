#!/usr/bin/node
const dict = require('./101-data').dict;

function summarizeByValues (objDict) {
  const entries = Object.entried(objDict);
  const newDict = {};
  for (const entry of entries) {
    newDict[entry[1]] = entries
      .filter((value) => value[1] === entry[1])
      .map((value) => value[0]);
  }
  return newDict;
}

console.log(summarizeByValues(dict));
